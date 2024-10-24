import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QMenuBar, QAction
from PyQt5.QtGui import QKeySequence


#This sets up the main window class
class MediaPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        #Here sets up the title and the size of the window
        self.setWindowTitle('Media Player')
        self.setGeometry(200, 200, 800, 600) #(x, y, width, height)


        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        view_menu = menu_bar.addMenu("View")
        
        #Opens File + Actions
        open_file = QAction("Open", self)
        open_file.setShortcut(QKeySequence("Ctrl+O"))
        open_file.triggered.connect(self.open_video)



        #Made the File Menu
        file_menu.addAction(open_file)
        #view_menu.addAction

        

    
    
    def open_video(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Open Video", "", "Video Files (*.mp4 *.avi *.flv *.mkv *.mov *.avchd *.webm *.avi *.wmv)")
        if file_name:
            print(f"Selected video: {file_name}")
def main():
    app = QApplication(sys.argv) #manages app flow and handles and captures cmd arguments
    window = MediaPlayer()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()