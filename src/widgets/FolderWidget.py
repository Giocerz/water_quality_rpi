from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize, Qt
from src.views.ui_folder_widget import Ui_Form
from PySide2.QtCore import QTimer


class FolderWidget(QWidget):
    def __init__(self, name:str, description:str, on_push):
        super().__init__()
        self.name = name
        self.on_push = on_push
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui_components()
        self.ui.folderBtn.clicked.connect(self.on_push_handle)
        

    def ui_components(self):
        self.ui.nameLbl.setText(self.name)
        self.ui.nameLbl.setAlignment(Qt.AlignCenter)
        icon = QIcon('./src/resources/icons/folder.png')
        self.ui.folderBtn.setIcon(icon)
        self.ui.folderBtn.setIconSize(QSize(81, 81))
    
    def on_push_handle(self):
        icon = QIcon('./src/resources/icons/open_folder.png')
        self.ui.folderBtn.setIcon(icon)
        self.ui.folderBtn.setIconSize(QSize(81, 81))
        QTimer.singleShot(300, self.on_push)
