import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

#This sets up the main window class
class MediaPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        #Here sets up the title and the size of the window
        self.setWindowTitle('Media Player')
        self.setGeometry(100, 100, 800, 600) #(x, y, width, height)

def main():
    app = QApplication(sys.argv) #manages app flow and handles and captures cmd arguments
    window = MediaPlayer()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()