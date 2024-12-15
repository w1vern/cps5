import sys
import random
from PySide6 import QtCore, QtWidgets, QtGui, QtAsyncio
from algorithm import algorithm, create_default, save_results
from models import Node, AssemblyUnit, Part

#current_node: Node | None = None
current_assembly_unit: AssemblyUnit | None = None
current_belt: Part | None = None
current_shift_1: Part | None = None
current_shift_2: Part | None = None


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.widget_classes = [StartWidget,  AssemblyUnitWidget, Part1Widget,
                               Part2Widget, Part3Widget, ResultWidget]
        self.current_stage = 0
        self.current_widget = None

        self.inner_layout = QtWidgets.QVBoxLayout(self)
        self.inner_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.load_stage()

    def load_stage(self):
        print("loading stage", self.current_stage)
        if self.current_widget is not None:
            self.inner_layout.removeWidget(self.current_widget)
            self.current_widget.deleteLater()
        self.current_widget = self.widget_classes[self.current_stage]()
        print("loaded", type(self.current_widget))
        self.inner_layout.addWidget(self.current_widget)
        self.current_widget.next_signal.connect(self.load_next_stage)

    @QtCore.Slot()
    def load_next_stage(self):
        self.current_stage += 1
        if self.current_stage >= len(self.widget_classes):
            self.current_stage = 0
        self.load_stage()


class StartWidget(QtWidgets.QWidget):
    next_signal = QtCore.Signal()

    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Начать проектировочный расчет")
        self.button.clicked.connect(self.start)

        self.inner_layout = QtWidgets.QVBoxLayout(self)
        self.inner_layout.addWidget(self.button)

    @QtCore.Slot()
    def start(self):
        global current_node, current_assembly_unit, current_belt, current_shift_1, current_shift_2
        current_node, current_assembly_unit, current_belt, current_shift_1, current_shift_2 = create_default()
        self.next_signal.emit()

""" class NodeWidget(QtWidgets.QWidget):
    next_signal = QtCore.Signal()

    def __init__(self):
        super().__init__()
        if current_node is None:
            return

        available_machine = [
            "Деревообрабатывающее оборудование",
            "Токарные станки и оборудование для типографии",
            "Сверлильные, расточные, шлифовальные, фрезерные, поперечно-строгальные и долбежные станки",
            "Конвейеры ленточные",
            "Вентиляторы, подъемники и текстильное оборудование",
            "Пластинчатый, ковшовый и элеваторный конвейеры",
            "Скребковый и шнековый конвейер"
        ]

        available_mode = [
            "Постоянный",
            "Переменный"
        ]

        self.inner_layout = QtWidgets.QVBoxLayout(self)
        self.inner_layout.addWidget(QtWidgets.QLabel("Введите параметры узла"))
        self.machine_mode = QtWidgets.QComboBox()
        self.machine_mode.addItems(available_machine)
        if current_node.machine_mode is not None:
            self.machine_mode.setCurrentText(current_node.machine_mode)

        self.shift_mode = QtWidgets.QComboBox()
        self.shift_mode.addItems(available_mode)
        if current_node.shift_mode is not None:
            self.shift_mode.setCurrentText(current_node.shift_mode)

        self.inner_layout.addWidget(QtWidgets.QLabel("Тип оборудования:"))
        self.inner_layout.addWidget(self.machine_mode)
        self.inner_layout.addWidget(QtWidgets.QLabel("Режим работы:"))
        self.inner_layout.addWidget(self.shift_mode)
        self.button = QtWidgets.QPushButton("Следующий шаг")
        self.button.clicked.connect(self.next)
        self.inner_layout.addWidget(self.button)

    @QtCore.Slot()
    def next(self):
        if current_node is None:
            return
        current_node.machine_mode = self.machine_mode.currentText()
        current_node.shift_mode = self.shift_mode.currentText()
        self.next_signal.emit()
 """

class AssemblyUnitWidget(QtWidgets.QWidget):
    next_signal = QtCore.Signal()

    def __init__(self):
        super().__init__()
        if current_assembly_unit is None:
            return

        self.inner_layout = QtWidgets.QVBoxLayout(self)
        

        self.inner_layout.addWidget(QtWidgets.QLabel(
            f"Наименование: {current_assembly_unit.NSE}"))
        self.inner_layout.addWidget(QtWidgets.QLabel(
            f"Тип: {current_assembly_unit.TSE}"))
        self.inner_layout.addWidget(QtWidgets.QLabel(
            f"Вид: {current_assembly_unit.VSE}"))
        self.inner_layout.addWidget(QtWidgets.QLabel(
            "Введите параметры сборочной единицы"))
        self.delta = QtWidgets.QLineEdit()
        self.inner_layout.addWidget(QtWidgets.QLabel("Расстояние от зуба ремня до оси металлического троса, delta:"))
        self.inner_layout.addWidget(self.delta)
        self.m = QtWidgets.QLineEdit()
        self.inner_layout.addWidget(QtWidgets.QLabel("Модуль передачи зубчатым ремнем, m:"))
        self.inner_layout.addWidget(self.m)
        

        self.button = QtWidgets.QPushButton("Следующий шаг")
        self.button.clicked.connect(self.next)
        self.inner_layout.addWidget(self.button)

    @QtCore.Slot()
    def next(self):
        if current_assembly_unit is None:
            return
        current_assembly_unit.delta_small = float(self.delta.text())
        current_assembly_unit.m = int(self.m.text())
        self.next_signal.emit()


class Part1Widget(QtWidgets.QWidget):
    next_signal = QtCore.Signal()

    def __init__(self):
        super().__init__()
        if current_belt is None:
            return
        
        self.inner_layout = QtWidgets.QVBoxLayout(self)

        self.inner_layout.addWidget(QtWidgets.QLabel(f"Наименование: {current_belt.ND}"))
        self.inner_layout.addWidget(QtWidgets.QLabel("Введите данные детали"))

        self.N = QtWidgets.QLineEdit()
        self.inner_layout.addWidget(QtWidgets.QLabel("Мощность, передаваемая ремнем, N:"))
        self.inner_layout.addWidget(self.N)
        
        self.cable_type = QtWidgets.QComboBox()
        self.cable_type.addItems(["1x7", "1x21"])
        self.inner_layout.addWidget(QtWidgets.QLabel("Тип троса, cable_type:"))
        self.inner_layout.addWidget(self.cable_type)

        self.phi_p = QtWidgets.QLineEdit()
        self.phi_p.setValidator(QtGui.QIntValidator())
        self.inner_layout.addWidget(QtWidgets.QLabel("Коэффициент ширины ремня, phi_p:"))
        self.inner_layout.addWidget(self.phi_p)
        
        self.button = QtWidgets.QPushButton("Следующий шаг")
        self.button.clicked.connect(self.next)
        self.inner_layout.addWidget(self.button)

    @QtCore.Slot()
    def next(self):
        if current_belt is None:
            return
        current_belt.N = float(self.N.text())
        current_belt.cable_type = self.cable_type.currentText()
        current_belt.phi_p = int(self.phi_p.text())
        self.next_signal.emit()

class Part2Widget(QtWidgets.QWidget):
    next_signal = QtCore.Signal()

    def __init__(self):
        super().__init__()
        if current_shift_1 is None:
            return
        
        self.inner_layout = QtWidgets.QVBoxLayout(self)

        self.inner_layout.addWidget(QtWidgets.QLabel(f"Наименование: {current_shift_1.ND}"))
        self.inner_layout.addWidget(QtWidgets.QLabel(f"Назначение: {current_shift_1.NaD}"))
        self.inner_layout.addWidget(QtWidgets.QLabel("Введите параметры шкива"))

        self.n_1 = QtWidgets.QLineEdit()
        self.inner_layout.addWidget(QtWidgets.QLabel("Частота вращения малого шкива, n_1:"))
        self.inner_layout.addWidget(self.n_1)


        self.button = QtWidgets.QPushButton("Следующий шаг")
        self.button.clicked.connect(self.next)
        self.inner_layout.addWidget(self.button)

    @QtCore.Slot()
    def next(self):
        if current_shift_1 is None:
            return
        current_shift_1.n_1 = float(self.n_1.text())

        self.next_signal.emit()

class Part3Widget(QtWidgets.QWidget):
    next_signal = QtCore.Signal()

    def __init__(self):
        super().__init__()
        if current_shift_2 is None:
            return
        
        self.inner_layout = QtWidgets.QVBoxLayout(self)

        self.inner_layout.addWidget(QtWidgets.QLabel(f"Наименование: {current_shift_2.ND}"))
        self.inner_layout.addWidget(QtWidgets.QLabel(f"Назначение: {current_shift_2.NaD}"))
        self.inner_layout.addWidget(QtWidgets.QLabel("Введите параметры шкива"))

        self.n_2 = QtWidgets.QLineEdit()
        self.inner_layout.addWidget(QtWidgets.QLabel("Частота вращения малого шкива, n_2:"))
        self.inner_layout.addWidget(self.n_2)

        self.button = QtWidgets.QPushButton("Следующий шаг")
        self.button.clicked.connect(self.next)
        self.inner_layout.addWidget(self.button)

    @QtCore.Slot()
    def next(self):
        if current_shift_2 is None:
            return
        current_shift_2.n_2 = int(self.n_2.text())
        algorithm(current_node, current_assembly_unit, current_belt, current_shift_1, current_shift_2) #type: ignore
        self.next_signal.emit()

class ResultWidget(QtWidgets.QWidget):
    next_signal = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self.inner_layout = QtWidgets.QVBoxLayout(self)

        self.inner_layout.addWidget(QtWidgets.QLabel(f"d_a1: {current_shift_1.d_a1:.2f}")) #type: ignore
        self.inner_layout.addWidget(QtWidgets.QLabel(f"d_a2: {current_shift_2.d_a2:.2f}")) #type: ignore

        self.save_button = QtWidgets.QPushButton("Сохранить")
        self.save_button.clicked.connect(self.save)
        self.inner_layout.addWidget(self.save_button)

        self.cancel_button = QtWidgets.QPushButton("Отменить")
        self.cancel_button.clicked.connect(self.cancel)
        self.inner_layout.addWidget(self.cancel_button)

    @QtCore.Slot()
    def save(self):
        if current_node is None or current_assembly_unit is None or current_belt is None or current_shift_1 is None or current_shift_2 is None:
            return
        save_results(current_node, current_assembly_unit, current_belt, current_shift_1, current_shift_2)
        self.next_signal.emit()

    @QtCore.Slot()
    def cancel(self):
        self.next_signal.emit()