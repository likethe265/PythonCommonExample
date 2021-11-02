import asyncio
import sys
import time

from PyQt5 import QtWidgets, uic
from asyncqt import QEventLoop, asyncSlot


class MainWindow(QtWidgets.QMainWindow):
    _serial_connected = False
    _serial_connecting = False
    _current_serial_ports = None
    _start_scan = False

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = uic.loadUi('testWindow.ui', self)
        self.ui.show()
        self.pb1.clicked.connect(self.onPb1Clicked)
        self.pb2.clicked.connect(self.onPb2Clicked)

    def onPb1Clicked(self):
        asyncio.ensure_future(do_some_work())

    def onPb2Clicked(self):
        asyncio.ensure_future(do_something_else())

async def do_something_else():
    i = 0
    while i <= 5:
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print('{}   do something else {}'.format(currentTime, i))
        await asyncio.sleep(1)
        i += 1


async def do_some_work():
    i = 0
    while i <= 5:
        await asyncio.sleep(1)
        currentTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print('{}   do some work {}'.format(currentTime, i))
        i += 1


def main():
    app = QtWidgets.QApplication(sys.argv)
    win = MainWindow()
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)
    with loop:
        loop.run_forever()
    # sys.exit(app.exec_())


if __name__ == '__main__':
    main()
