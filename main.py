import pyqtgraph as pg
import design
import sys
from PyQt5 import QtCore, QtWidgets

from ExactSolution import ExactSolution
from Euler import Euler
from ImprovedEuler import ImprovedEuler
from RungeKutta import RungeKutta


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
        self.rungeKutta.stateChanged.connect(self.displayRungeKuttaGraph)
        self.euler_error.stateChanged.connect(self.displayEulerErrorGraph)
        self.improvedEuler_error.stateChanged.connect(self.displayImprovedEulerErrorGraph)
        self.rungeKutta_error.stateChanged.connect(self.displayRungeKuttaErrorGraph)

        # text boxes changing
        self.x0_var.textChanged.connect(self.updateSolutionGraph)
        self.x0_var.textChanged.connect(self.updateEulerGraph)
        self.x0_var.textChanged.connect(self.updateImprovedEulerGraph)
        self.x0_var.textChanged.connect(self.updateRungeKuttaGraph)
        self.x0_var.textChanged.connect(self.updateEulerErrorGraph)
        self.x0_var.textChanged.connect(self.updateImprovedEulerErrorGraph)
        self.x0_var.textChanged.connect(self.displayRungeKuttaErrorGraph)

        self.y0_var.textChanged.connect(self.updateSolutionGraph)
        self.y0_var.textChanged.connect(self.updateEulerGraph)
        self.y0_var.textChanged.connect(self.updateImprovedEulerGraph)
        self.y0_var.textChanged.connect(self.updateRungeKuttaGraph)
        self.y0_var.textChanged.connect(self.updateEulerErrorGraph)
        self.y0_var.textChanged.connect(self.updateImprovedEulerErrorGraph)
        self.y0_var.textChanged.connect(self.updateRungeKuttaErrorGraph)

        self.n_var.textChanged.connect(self.updateEulerGraph)
        self.n_var.textChanged.connect(self.updateImprovedEulerGraph)
        self.n_var.textChanged.connect(self.updateRungeKuttaGraph)
        self.n_var.textChanged.connect(self.updateEulerErrorGraph)
        self.n_var.textChanged.connect(self.updateImprovedEulerErrorGraph)
        self.n_var.textChanged.connect(self.updateRungeKuttaErrorGraph)

        self.b_var.textChanged.connect(self.updateEulerGraph)
        self.b_var.textChanged.connect(self.updateSolutionGraph)
        self.b_var.textChanged.connect(self.updateImprovedEulerGraph)
        self.b_var.textChanged.connect(self.updateRungeKuttaGraph)
        self.b_var.textChanged.connect(self.updateEulerErrorGraph)
        self.b_var.textChanged.connect(self.updateImprovedEulerErrorGraph)
        self.b_var.textChanged.connect(self.updateRungeKuttaErrorGraph)

    def setGraphs(self):
        self.redPen = pg.mkPen(color=(255, 0, 0), width= 3)
        self.greenPen = pg.mkPen(color=(0, 100, 0), width= 3)
        self.bluePen = pg.mkPen(color=(0, 0, 255), width= 3)
        self.yellowPen = pg.mkPen(color=(222, 151, 11), width= 3)

        exactSolution = ExactSolution(self.x0_var.text(), self.y0_var.text(), self.b_var.text())
        self.solutionGraph = self.graphWidget1.plot(exactSolution.x, exactSolution.y, pen = self.redPen)

        eulerGraph = Euler(exactSolution.x0, exactSolution.y0, self.b_var.text(), self.n_var.text())
        self.eulerGraph = self.graphWidget1.plot(eulerGraph.x, eulerGraph.y, pen = self.greenPen)
        self.eulerErrorGraph = self.graphWidget2.plot(eulerGraph.x, eulerGraph.t, pen = self.greenPen)


        improvedEulerGraph  = ImprovedEuler(exactSolution.x0, exactSolution.y0, self.b_var.text(), self.n_var.text())
        self.improvedEulerGraph = self.graphWidget1.plot(improvedEulerGraph.x, improvedEulerGraph.y, pen = self.bluePen)
        self.improvedEulerErrorGraph = self.graphWidget2.plot(improvedEulerGraph.x, improvedEulerGraph.t, pen = self.bluePen)


        rungeKuttaGraph = RungeKutta(exactSolution.x0, exactSolution.y0, self.b_var.text(), self.n_var.text())
        self.rungeKuttaGraph = self.graphWidget1.plot(rungeKuttaGraph.x, rungeKuttaGraph.y, pen = self.yellowPen)
        self.rungeKuttaErrorGraph = self.graphWidget2.plot(rungeKuttaGraph.x, rungeKuttaGraph.t, pen = self.yellowPen)


    def setWidgets(self):
        vBox1 = self.verticalLayout_pg1
        vBox2 = self.verticalLayout_pg2
        vBox3 = self.verticalLayout_pg3

        self.graphWidget1 = pg.PlotWidget()
        self.graphWidget1.showGrid(x=True, y=True)
        self.graphWidget1.setBackground('k')
        vBox1.addWidget(self.graphWidget1)
        self.graphWidget1.plot()

        self.graphWidget2 = pg.PlotWidget()
        self.graphWidget2.showGrid(x=True, y=True)
        self.graphWidget2.setBackground('k')
        vBox2.addWidget(self.graphWidget2)
        self.graphWidget2.plot()

        self.graphWidget3 = pg.PlotWidget()
        self.graphWidget3.showGrid(x=True, y=True)
        self.graphWidget3.setBackground('k')
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
        self.solutionGraph.clear()
        if (self.solution.isChecked()):
            self.solutionGraph = self.graphWidget1.plot(exactSolution.x, exactSolution.y, pen = self.redPen)

    def updateEulerGraph(self):
        exactSolution = ExactSolution(self.x0_var.text(), self.y0_var.text(), self.b_var.text())
        eulerGraph = Euler(exactSolution.x0, exactSolution.y0, self.b_var.text(), self.n_var.text())
        self.eulerGraph.clear()
        if (self.euler.isChecked()):
            self.eulerGraph = self.graphWidget1.plot(eulerGraph.x, eulerGraph.y,  pen = self.greenPen)

    def updateEulerErrorGraph(self):
        exactSolution = ExactSolution(self.x0_var.text(), self.y0_var.text(), self.b_var.text())
        eulerGraph = Euler(exactSolution.x0, exactSolution.y0, self.b_var.text(), self.n_var.text())
        self.eulerErrorGraph.clear()
        if (self.euler_error.isChecked()):
            self.eulerErrorGraph = self.graphWidget2.plot(eulerGraph.x, eulerGraph.t, pen=self.greenPen)

    def updateImprovedEulerGraph(self):
        exactSolution = ExactSolution(self.x0_var.text(), self.y0_var.text(), self.b_var.text())
        improvedEulerGraph = ImprovedEuler(exactSolution.x0, exactSolution.y0, self.b_var.text(), self.n_var.text())
        self.improvedEulerGraph.clear()
        if (self.improvedEuler.isChecked()):
            self.improvedEulerGraph = self.graphWidget1.plot(improvedEulerGraph.x, improvedEulerGraph.y, pen = self.bluePen)

    def updateImprovedEulerErrorGraph(self):
        exactSolution = ExactSolution(self.x0_var.text(), self.y0_var.text(), self.b_var.text())
        improvedEulerGraph = ImprovedEuler(exactSolution.x0, exactSolution.y0, self.b_var.text(), self.n_var.text())
        self.improvedEulerErrorGraph.clear()
        if (self.improvedEuler_error.isChecked()):
            self.improvedEulerErrorGraph = self.graphWidget2.plot(improvedEulerGraph.x, improvedEulerGraph.t, pen = self.bluePen)

    def updateRungeKuttaGraph(self):
        exactSolution = ExactSolution(self.x0_var.text(), self.y0_var.text(), self.b_var.text())
        rungeKuttaGraph = RungeKutta(exactSolution.x0, exactSolution.y0, self.b_var.text(), self.n_var.text())
        self.rungeKuttaGraph.clear()
        if (self.rungeKutta.isChecked()):
            self.rungeKuttaGraph = self.graphWidget1.plot(rungeKuttaGraph.x, rungeKuttaGraph.y, pen = self.yellowPen)

    def updateRungeKuttaErrorGraph(self):
        exactSolution = ExactSolution(self.x0_var.text(), self.y0_var.text(), self.b_var.text())
        rungeKuttaGraph = RungeKutta(exactSolution.x0, exactSolution.y0, self.b_var.text(), self.n_var.text())
        self.rungeKuttaErrorGraph.clear()
        if (self.rungeKutta_error.isChecked()):
            self.rungeKuttaErrorGraph = self.graphWidget2.plot(rungeKuttaGraph.x, rungeKuttaGraph.t, pen = self.yellowPen)


    def displaySolutionGraph(self):
        if self.solution.isChecked():
            self.updateSolutionGraph()
            self.solutionGraph.show()
        else:
            self.solutionGraph.hide()

    def displayEulerGraph(self):
        if self.euler.isChecked():
            self.updateEulerGraph()
            self.eulerGraph.show()
        else:
            self.eulerGraph.hide()

    def displayEulerErrorGraph(self):
        if self.euler_error.isChecked():
            self.updateEulerErrorGraph()
            self.eulerErrorGraph.show()
        else:
            self.eulerErrorGraph.hide()

    def displayImprovedEulerGraph(self):
        if self.improvedEuler.isChecked():
            self.updateImprovedEulerGraph()
            self.improvedEulerGraph.show()
        else:
            self.improvedEulerGraph.hide()

    def displayImprovedEulerErrorGraph(self):
        if self.improvedEuler_error.isChecked():
            self.updateImprovedEulerErrorGraph()
            self.improvedEulerErrorGraph.show()
        else:
            self.improvedEulerErrorGraph.hide()

    def displayRungeKuttaGraph(self):
        if self.rungeKutta.isChecked():
            self.updateRungeKuttaGraph()
            self.rungeKuttaGraph.show()
        else:
            self.rungeKuttaGraph.hide()

    def displayRungeKuttaErrorGraph(self):
        if self.rungeKutta_error.isChecked():
            self.updateRungeKuttaErrorGraph()
            self.rungeKuttaErrorGraph.show()
        else:
            self.rungeKuttaErrorGraph.hide()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = App()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
