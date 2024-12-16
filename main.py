import sys
import numpy as np
import matplotlib

from physic_functions import GENERATOR_MAP  # Ensure GENERATOR_MAP is properly imported

matplotlib.use("Qt5Agg")  # Use the PyQt5 backend for Matplotlib
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QDoubleSpinBox, QLabel, QHBoxLayout, QComboBox
)
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        # Initialize a Matplotlib Figure and Axes
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

        # Start animation
        self.animation = FuncAnimation(
            self.canvas.fig, self.update_animation, frames=100, interval=50, blit=True
        )

    def __setup_lables_limits(self):
        self.canvas.ax.set_xlim(0, 20)
        self.canvas.ax.set_ylim(-2.5, 2.5)
        self.canvas.ax.set_xlabel("X")
        self.canvas.ax.set_ylabel("Y")

    def __init_animation_parameters(self):
        self.x = np.linspace(0, 20, 500)
        self.A = self.a_input.value() # Amplitude
        self.N = self.n_input.value() # Harmonic number
        self.L = self.l_input.value() # Length
        self.T = self.t_input.value() # Tension
        self.M = self.m_input.value() # Mass
        self.line, = self.canvas.ax.plot([], [], 'r-', lw=2)

    def __add_controls(self, layout):
        control_layout = QHBoxLayout()
        layout.addLayout(control_layout)
        self.__add_a_controller(control_layout)
        self.__add_n_controller(control_layout)
        self.__add_l_controller(control_layout)
        self.__add_t_controller(control_layout)
        self.__add_m_controller(control_layout)
        self.__add_generator_controller(control_layout)  # Add the generator controller

    def __add_n_controller(self, control_layout):
        control_layout.addWidget(QLabel("Harmonic number:"))
        self.n_input = QDoubleSpinBox()
        self.n_input.setRange(1, 10)
        self.n_input.setSingleStep(0.1)
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
        self.l_input.setRange(0.1, 10.0)  # Set range for A
        self.l_input.setSingleStep(0.1)
        self.l_input.setValue(4.0)  # Default A value
        self.l_input.valueChanged.connect(self.update_l)
        control_layout.addWidget(self.l_input)

    def __add_t_controller(self, control_layout):
        control_layout.addWidget(QLabel("Tension(kg/m):"))
        self.t_input = QDoubleSpinBox()
        self.t_input.setRange(1, 500)
        self.t_input.setSingleStep(5)
        self.t_input.setValue(100)
        self.t_input.valueChanged.connect(self.update_t)
        control_layout.addWidget(self.t_input)

    def __add_m_controller(self, control_layout):
        control_layout.addWidget(QLabel("Linear mass density(kg):"))
        self.m_input = QDoubleSpinBox()
        self.m_input.setRange(0.1, 10.0)
        self.m_input.setSingleStep(0.1)
        self.m_input.setValue(4.0)
        self.m_input.valueChanged.connect(self.update_m)
        control_layout.addWidget(self.m_input)

    def __add_generator_controller(self, control_layout):
        """Add a dropdown to choose a generator from GENERATOR_MAP."""
        control_layout.addWidget(QLabel("Select Generator:"))
        self.generator_selector = QComboBox()
        self.generator_selector.addItems(GENERATOR_MAP.keys())  # Add generator names
        self.generator_selector.currentTextChanged.connect(self.update_generator)
        control_layout.addWidget(self.generator_selector)

    def __setup_main_window(self):
        self.setWindowTitle("Animated Generator Selector with Input Control")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        return layout

    def _get_formula(self):
        return self.current_generator.get_formula().format(k=(self.B * np.pi) / self.current_generator.get_length(), omega=2 * np.pi * self.B)

    def update_a(self, value):
        self.A = value
        self.canvas.draw()

    def update_n(self, value):
        self.N = value
        self.canvas.draw()

    def update_l(self, value):
        self.L = value
        self.canvas.draw()

    def update_t(self, value):
        self.T = value
        self.canvas.draw()

    def update_m(self, value):
        self.M = value
        self.canvas.draw()
    
    def update_generator(self, generator_name):
        """Change the current generator based on the selected name."""
        if generator_name in GENERATOR_MAP:
            self.current_generator = GENERATOR_MAP[generator_name]()
            self.canvas.ax.set_title(f"Generator: {generator_name}")
            self.canvas.draw()

    def update_animation(self, i):
        """Update function for animation."""
        y = self.current_generator.generate_y(self.x, i, self.A, self.N, self.L, self.T, self.M)
        self.line.set_data(self.x, y)    # Update line data
        return self.line,

# Main entry point
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnimationWindow()
    window.show()
    sys.exit(app.exec_())
