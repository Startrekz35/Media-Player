import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QMenuBar, QAction, QSlider, QVBoxLayout, QHBoxLayout, QWidget, QFrame, QSpacerItem, QSizePolicy
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeySequence


#This sets up the main window class
class MediaPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        #Here sets up the title and the size of the window
        self.setWindowTitle('Media Player')
        self.setGeometry(200, 200, 800, 600) #(x, y, width, height)

        #central/main layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        
        
        main_layout = QVBoxLayout(self.central_widget)


        #menu bar list
        menu_bar = self.menuBar()
        file_menu = menu_bar.addMenu("File")
        view_menu = menu_bar.addMenu("View")
        play_menu = menu_bar.addMenu("Play")
        
        
        #Opens File + Actions
        open_file = QAction("Open", self)
        open_file.setShortcut(QKeySequence("Ctrl+O"))
        open_file.triggered.connect(self.open_video)


        #File Menu List
        file_menu.addAction(open_file)
        
        #Opens View + Actions
        open_view = QAction("Full Screen", self)
        open_view.setShortcut(QKeySequence("Ctrl+Enter"))

        #View Menu List
        view_menu.addAction(open_view)

        #The video box itself
        self.video_placeholder = QWidget(self)
        self.video_placeholder.setStyleSheet("background-color: black")
        main_layout.addWidget(self.video_placeholder)
        self.video_placeholder.setMinimumHeight(500)


        main_layout.setStretch(0, 5)

        self.media_control_bar = QFrame(self)
        self.media_control_bar.setFrameShape(QFrame.Box)
        self.media_control_bar.setMinimumHeight(50)
        
        main_layout.setStretch(1, 1)

        main_layout.addWidget(self.media_control_bar)
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