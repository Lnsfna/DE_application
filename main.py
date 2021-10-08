
import pyqtgraph as pg
import design
import sys
from PyQt5 import QtCore, QtWidgets

from ExactSolution import ExactSolution

class App(QtWidgets.QMainWindow, design.Ui_MainWindow):


    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWidgets()
        self.setGraphs()

        self.solution.stateChanged.connect(self.displaySolution)
        self.x0_var.textChanged.connect(self.updateFirstGraph)
        self.y0_var.textChanged.connect(self.updateFirstGraph)


    def setGraphs(self):
        exactSolution =ExactSolution(self.x0_var.text(), self.y0_var.text())
        self.solution_graph = self.graphWidget1.plot(exactSolution.x, exactSolution.y)

    def setWidgets(self):
        vBox1 = self.verticalLayout_pg1
        vBox2 = self.verticalLayout_pg2
        vBox3 = self.verticalLayout_pg3

        self.graphWidget1 = pg.PlotWidget()
        vBox1.addWidget(self.graphWidget1)
        self.graphWidget1.plot()
        self.graphWidget2 = pg.PlotWidget()
        vBox2.addWidget(self.graphWidget2)
        self.graphWidget2.plot()
        self.graphWidget3 = pg.PlotWidget()
        vBox3.addWidget(self.graphWidget3)
        self.graphWidget3.plot()

        self.solution.setChecked(True)
        self.euler.setChecked(True)
        self.improvedEuler.setChecked(True)
        self.rungeKutta.setChecked(True)
        self.euler_error.setChecked(True)
        self.improvedEuler_error.setChecked(True)
        self.rungeKutta_error.setChecked(True)

    def updateFirstGraph(self):
        exactSolution = ExactSolution(self.x0_var.text(), self.y0_var.text())
        self.solution_graph.clear()
        self.solution_graph = self.graphWidget1.plot(exactSolution.x, exactSolution.y)

    def displaySolution(self):
        if self.solution.isChecked():
            self.updateFirstGraph()
            self.solution_graph.show()
        else:
            self.solution_graph.hide()



def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

