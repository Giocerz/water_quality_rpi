from PySide2.QtWidgets import QWidget
from src.views.ui_folder_widget import Ui_Form


class FolderWidget(QWidget):
    def __init__(self, name, description):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.nameLbl.setText(name)
        self.ui.descriptionLbl.setText(description)