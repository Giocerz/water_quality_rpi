from PySide2.QtWidgets import QWidget
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize, Qt
from src.views.ui_folder_widget import Ui_Form
from PySide2.QtCore import QTimer


class FolderWidget(QWidget):
    def __init__(self, id:int, name:str, description:str, on_push:callable, type:str = "open"):
        super().__init__()
        self.id:int = id
        self.name:str = name
        self.on_push:callable = on_push
        self.type:str = type
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.__ui_components()
        self.ui.folderBtn.clicked.connect(self.__on_push_handle)
        

    def __ui_components(self):
        self.ui.nameLbl.setText(self.name)
        self.ui.nameLbl.setAlignment(Qt.AlignCenter)
        icon = QIcon('./src/resources/icons/folder.png')
        self.ui.folderBtn.setIcon(icon)
        self.ui.folderBtn.setIconSize(QSize(81, 81))
    
    def __on_push_handle(self):
        icon = QIcon('./src/resources/icons/open_folder.png')
        self.ui.folderBtn.setIcon(icon)
        self.ui.folderBtn.setIconSize(QSize(81, 81))
        QTimer.singleShot(200, self.__on_push_finsih_anim)
    
    def __on_push_finsih_anim(self):
        if(self.type == "open"):
            self.on_push(self.id)
        else:
            self.on_push()
        icon = QIcon('./src/resources/icons/folder.png')
        self.ui.folderBtn.setIcon(icon)
        self.ui.folderBtn.setIconSize(QSize(81, 81))
