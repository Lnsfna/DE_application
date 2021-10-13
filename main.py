import pyqtgraph as pg
import design
import sys
from PyQt5 import QtCore, QtWidgets

from ExactSolution import ExactSolution
from Euler import Euler
from ImprovedEuler import ImprovedEuler


class App(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWidgets()
        self.setGraphs()

        # checkboxes changing
        self.solution.stateChanged.connect(self.displaySolutionGraph)
        self.euler.stateChanged.connect(self.displayEulerGraph)
        self.improvedEuler.stateChanged.connect(self.displayImprovedEulerGraph)


        # text boxes changing
        self.x0_var.textChanged.connect(self.updateSolutionGraph)
        self.x0_var.textChanged.connect(self.updateEulerGraph)
        self.x0_var.textChanged.connect(self.updateImprovedEulerGraph)

        self.y0_var.textChanged.connect(self.updateSolutionGraph)
        self.y0_var.textChanged.connect(self.updateEulerGraph)
        self.y0_var.textChanged.connect(self.updateImprovedEulerGraph)

        self.n_var.textChanged.connect(self.updateEulerGraph)
        self.n_var.textChanged.connect(self.updateImprovedEulerGraph)

        self.b_var.textChanged.connect(self.updateEulerGraph)
        self.b_var.textChanged.connect(self.updateSolutionGraph)
        self.b_var.textChanged.connect(self.updateImprovedEulerGraph)


    def setGraphs(self):
        exactSolution = ExactSolution(self.x0_var.text(), self.y0_var.text(), self.b_var.text())
        self.solution_graph = self.graphWidget1.plot(exactSolution.x, exactSolution.y)
        eulerGraph = Euler(exactSolution.x0, exactSolution.y0, self.b_var.text(), self.n_var.text())
        self.eulerGraph = self.graphWidget1.plot(eulerGraph.x, eulerGraph.y)
        improvedEulerGraph  = ImprovedEuler(exactSolution.x0, exactSolution.y0, self.b_var.text(), self.n_var.text())
        self.improvedEulerGraph = self.graphWidget1.plot(improvedEulerGraph.x, improvedEulerGraph.y)


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

    def updateSolutionGraph(self):
        exactSolution = ExactSolution(self.x0_var.text(), self.y0_var.text(), self.b_var.text())
        self.solution_graph.clear()
        if (self.solution.isChecked()):
            self.solution_graph = self.graphWidget1.plot(exactSolution.x, exactSolution.y)

    def updateEulerGraph(self):
        exactSolution = ExactSolution(self.x0_var.text(), self.y0_var.text(), self.b_var.text())
        eulerGraph = Euler(exactSolution.x0, exactSolution.y0, self.b_var.text(), self.n_var.text())
        self.eulerGraph.clear()
        if (self.euler.isChecked()):
            self.eulerGraph = self.graphWidget1.plot(eulerGraph.x, eulerGraph.y)

    def updateImprovedEulerGraph(self):
        exactSolution = ExactSolution(self.x0_var.text(), self.y0_var.text(), self.b_var.text())
        improvedEulerGraph = ImprovedEuler(exactSolution.x0, exactSolution.y0, self.b_var.text(), self.n_var.text())
        self.improvedEulerGraph.clear()
        if (self.euler.isChecked()):
            self.improvedEulerGraph = self.graphWidget1.plot(improvedEulerGraph.x, improvedEulerGraph.y)

    def displaySolutionGraph(self):
        if self.solution.isChecked():
            self.updateSolutionGraph()
            self.solution_graph.show()
        else:
            self.solution_graph.hide()

    def displayEulerGraph(self):
        if self.euler.isChecked():
            self.updateEulerGraph()
            self.eulerGraph.show()
        else:
            self.eulerGraph.hide()

    def displayImprovedEulerGraph(self):
        if self.improvedEuler.isChecked():
            self.updateImprovedEulerGraph()
            self.improvedEulerGraph.show()
        else:
            self.improvedEulerGraph.hide()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
