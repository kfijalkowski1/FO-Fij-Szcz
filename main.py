import sys
import numpy as np
import matplotlib

from phisics_functions import GENERATOR_MAP

matplotlib.use("Qt5Agg")  # Use the PyQt5 backend for Matplotlib
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget, QDoubleSpinBox, QLabel, QHBoxLayout
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

        self.current_generator = list(GENERATOR_MAP.values())[0]()

        # Start animation
        self.animation = FuncAnimation(
            self.canvas.fig, self.update_animation, frames=100, interval=50, blit=True
        )

    def __setup_lables_limits(self):
        self.canvas.ax.set_xlim(0, 10)
        self.canvas.ax.set_ylim(-2.5, 2.5)
        self.canvas.ax.set_xlabel("X")
        self.canvas.ax.set_ylabel("Y = A * sin(Bx)")

    def __init_animation_parameters(self):
        self.x = np.linspace(0, 10, 500)
        self.B = self.b_input.value()
        self.line, = self.canvas.ax.plot([], [], 'r-', lw=2)

    def __add_controls(self, layout):
        control_layout = QHBoxLayout()
        layout.addLayout(control_layout)
        self.__add_b_controller(control_layout)

    def __add_b_controller(self, control_layout):
        control_layout.addWidget(QLabel("Frequency Multiplier (B):"))
        self.b_input = QDoubleSpinBox()
        self.b_input.setRange(0.1, 10.0)  # Set range for B
        self.b_input.setSingleStep(0.1)
        self.b_input.setValue(1.0)  # Default B value
        self.b_input.valueChanged.connect(self.update_b)
        control_layout.addWidget(self.b_input)

    def __setup_main_window(self):
        self.setWindowTitle("Animated A*sin(Bx) with Input Control")
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        return layout

    def update_b(self, value):
        """Update B and redraw the plot."""
        self.B = value
        self.canvas.ax.set_title(f"A*sin({self.B:.1f}x)")
        self.canvas.draw()

    def update_animation(self, i):
        """Update function for animation."""
        y = self.current_generator.generate_y(self.x, i, self.B)
        self.line.set_data(self.x, y)    # Update line data
        return self.line,

# Main entry point
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AnimationWindow()
    window.show()
    sys.exit(app.exec_())
