
#https://stackoverflow.com/a/46739609/2403000
# >= 2018
from PySide2 import QtWidgets, QtCore, QtGui
import MaxPlus
import os

class SampleUI(QtWidgets.QDialog):
    def __init__(self, parent=MaxPlus.GetQMaxMainWindow()):
        super(SampleUI, self).__init__(parent)
        self.initUI()

    def initUI(self):
        mainLayout = QtWidgets.QHBoxLayout()
        testBtn = QtWidgets.QPushButton("Test!")
        mainLayout.addWidget(testBtn)
        self.setLayout(mainLayout)

if __name__ == "__main__":
    try:
        ui.close()
    except:
        pass

    ui = SampleUI()
    ui.show()


# < 2018
from PySide import QtGui
import MaxPlus


class _GCProtector(object):
    widgets = []

def make_cylinder():
    obj = MaxPlus.Factory.CreateGeomObject(MaxPlus.ClassIds.Cylinder)
    obj.ParameterBlock.Radius.Value = 10.0
    obj.ParameterBlock.Height.Value = 30.0
    node = MaxPlus.Factory.CreateNode(obj)
    time = MaxPlus.Core.GetCurrentTime()
    MaxPlus.ViewportManager.RedrawViews(time)
    return

app = QtGui.QApplication.instance()
if not app:
    app = QtGui.QApplication([])

def main():     
    MaxPlus.FileManager.Reset(True)

    w = QtGui.QWidget(MaxPlus.GetQMaxWindow())
    _GCProtector.widgets.append( w )
    w.resize(250, 100)
    w.setWindowTitle('PySide Qt Window')

    main_layout = QtGui.QVBoxLayout()
    label = QtGui.QLabel("Click button to create a cylinder in the scene")
    main_layout.addWidget(label)

    cylinder_btn = QtGui.QPushButton("Cylinder")
    cylinder_btn.clicked.connect(make_cylinder)
    main_layout.addWidget(cylinder_btn)

    textEdit = QtGui.QLineEdit()
    textEdit.setText("Edit box")
    main_layout.addWidget(textEdit)

    w.setLayout( main_layout )
    w.show()


if __name__ == '__main__':
    main()