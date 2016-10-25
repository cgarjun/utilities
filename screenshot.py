import sys
import argparse
from PyQt4 import QtGui
from PyQt4 import QtCore

app = QtGui.QApplication(sys.argv)

class ScreenShot(QtGui.QWidget):
    def __init__(self):
        super(ScreenShot, self).__init__()
        self.outPath = None
        screen_rect = app.desktop().screenGeometry()
        width, height = screen_rect.width()*2, screen_rect.height()
        self.setGeometry(0, 0, width, height)
        self.setWindowTitle('Screen Capture')
        self.setCursor(QtCore.Qt.CrossCursor)
        self.setWindowOpacity(0.1)
        self.rubberband = QtGui.QRubberBand(QtGui.QRubberBand.Rectangle, self)
        self.setMouseTracking(True)

    def mousePressEvent(self, event):
        self.origin = event.pos()
        self.rubberband.setGeometry(QtCore.QRect(self.origin, QtCore.QSize()))
        self.rubberband.show()
        QtGui.QWidget.mousePressEvent(self, event)

    def mouseMoveEvent(self, event):
        if self.rubberband.isVisible():
            self.rubberband.setGeometry(
                QtCore.QRect(self.origin, event.pos()).normalized())
        QtGui.QWidget.mouseMoveEvent(self, event)

    def mouseReleaseEvent(self, event):
        if self.rubberband.isVisible():
            self.rubberband.hide()
            selected = []
            rect = self.rubberband.geometry()
            desktop = QtGui.QApplication.instance().desktop()
            imgmap = QtGui.QPixmap.grabWindow(desktop.winId(), rect.x(), rect.y(), rect.width(), rect.height())
            imgmap.save(self.outPath)
            sys.exit()
        QtGui.QWidget.mouseReleaseEvent(self, event)

    def launch(self, imagePath):
        self.outPath = imagePath
        self.show()


def captureRegion(outImagePath):
    app = QtGui.QApplication(sys.argv)
    lch = ScreenShot()
    lch.launch(outImagePath)
    sys.exit(app.exec_())


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple tool to take screenshot can be used as a module also')
    parser.add_argument('-o','--out', help='output path for image to be saved', required=True)
    args = parser.parse_args()
    lch = ScreenShot()
    lch.launch(args.out)
    sys.exit(app.exec_())
