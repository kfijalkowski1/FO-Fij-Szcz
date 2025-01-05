import sys
import numpy as np
import matplotlib

from physic_functions import GENERATOR_MAP

matplotlib.use("Qt5Agg")  # Use the PyQt5 backend for Matplotlib
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QDoubleSpinBox, QLabel, QHBoxLayout, QComboBox
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        self.fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = self.fig.add_subplot(111)
        super(MplCanvas, self).__init__(self.fig)

class AnimationWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        layout = self.__setup_main_window()

        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        layout.addWidget(self.canvas)

        self.__add_controls(layout)
        self.__init_animation_parameters()
        self.__setup_lables_limits()

        self.current_generator = list(GENERATOR_MAP.values())[0]()  # Default generator
        self.canvas.ax.set_title(self.current_generator.get_formula())

        # Start animation
        self.animation = FuncAnimation(
            self.canvas.fig, self.update_animation, frames=1000, interval=50, blit=True
        )

    def __setup_lables_limits(self):
        self.canvas.ax.set_xlim(0, self.L)
        self.canvas.ax.set_ylim(-2.5, 2.5)
        self.canvas.ax.set_xlabel("X")
        self.canvas.ax.set_ylabel("Y")

    def __init_animation_parameters(self):
        self.A = self.a_input.value() # Amplitude
        self.N = self.n_input.value() # Harmonic number
        self.L = self.l_input.value() # Length
        self.V = self.v_input.value() # Speed
        self.line, = self.canvas.ax.plot([], [], 'r-', lw=2)
        self.x = np.linspace(0, self.L, 500)

    def __add_controls(self, layout):
        control_layout = QHBoxLayout()
        layout.addLayout(control_layout)
        self.__add_a_controller(control_layout)
        self.__add_n_controller(control_layout)
        self.__add_l_controller(control_layout)
        self.__add_v_controller(control_layout)
        self.__add_generator_controller(control_layout)

    def __add_n_controller(self, control_layout):
        control_layout.addWidget(QLabel("Harmonic number:"))
        self.n_input = QDoubleSpinBox()
        self.n_input.setRange(1, 10)
        self.n_input.setSingleStep(1)
        self.n_input.setValue(1)
        self.n_input.valueChanged.connect(self.update_n)
        control_layout.addWidget(self.n_input)

    def __add_a_controller(self, control_layout):
        control_layout.addWidget(QLabel("Amplitude(m):"))
        self.a_input = QDoubleSpinBox()
        self.a_input.setRange(0.1, 2.0)  # Set range for A
        self.a_input.setSingleStep(0.1)
        self.a_input.setValue(1.0)  # Default A value
        self.a_input.valueChanged.connect(self.update_a)
        control_layout.addWidget(self.a_input)

    def __add_l_controller(self, control_layout):
        control_layout.addWidget(QLabel("Length(m):"))
        self.l_input = QDoubleSpinBox()
        self.l_input.setRange(1, 30.0)  # Set range for A
        self.l_input.setSingleStep(1)
        self.l_input.setValue(5)  # Default A value
        self.l_input.valueChanged.connect(self.update_l)
        control_layout.addWidget(self.l_input)

    def __add_v_controller(self, control_layout):
        control_layout.addWidget(QLabel("Speed(m/s):"))
        self.v_input = QDoubleSpinBox()
        self.v_input.setRange(0.1, 5)
        self.v_input.setSingleStep(0.1)
        self.v_input.setValue(0.5)
        self.v_input.valueChanged.connect(self.update_v)
        control_layout.addWidget(self.v_input)

    def __add_generator_controller(self, control_layout):
        """Add a dropdown to choose a generator from GENERATOR_MAP."""
        control_layout.addWidget(QLabel("Select Generator:"))
        self.generator_selector = QComboBox()
        self.generator_selector.addItems(GENERATOR_MAP.keys())
        self.generator_selector.currentTextChanged.connect(self.update_generator)
        control_layout.addWidget(self.generator_selector)

    def __setup_main_window(self):
        self.setWindowTitle("Fala stojąca w strunie")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        return layout

    def update_a(self, value):
        self.A = value
        self.canvas.draw()

    def update_n(self, value):
        self.N = value
        self.canvas.draw()

    def update_l(self, value):
        self.L = value
        self.x = np.linspace(0, self.L, 500)
        self.canvas.ax.set_xlim(0, self.L)
        self.canvas.draw()

    def update_v(self, value):
        self.V = value
        self.canvas.draw()
    
    def update_generator(self, generator_name):
        """Change the current generator based on the selected name."""
        if generator_name in GENERATOR_MAP:
            self.current_generator = GENERATOR_MAP[generator_name]()
            self.canvas.ax.set_title(self.current_generator.get_formula())
            self.canvas.draw()

    def update_animation(self, i):
        """Update function for animation."""
        y = self.current_generator.generate_y(self.x, i, self.A, self.N, self.L, self.V)
        self.line.set_data(self.x, y)
        return self.line,

# Main entry point
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnimationWindow()
    window.show()
    sys.exit(app.exec_())
