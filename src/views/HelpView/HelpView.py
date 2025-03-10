from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon, QPixmap
from src.views.ui_HelpView import Ui_MainWindow
from src.package.Navigator import Navigator

class HelpView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))
        pixmap = QPixmap('./src/resources/images/help_image.jpg')
        self.ui.imageLbl.setPixmap(pixmap)

    def on_back_clicked(self):
        Navigator.pop(context= self.context, view= self)