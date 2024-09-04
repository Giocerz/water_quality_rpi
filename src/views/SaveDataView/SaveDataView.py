from PySide2.QtWidgets import QMainWindow, QStackedLayout
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from src.views.ui_Save import Ui_Save
from src.widgets.KeyboardWidget import KeyboardWidget

class SaveDataView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.ui = Ui_Save()
        self.ui.setupUi(self)
        self.ui_components()

        self.keyboard = KeyboardWidget(self.ui.inputPlace)
        layout = QStackedLayout(self.ui.widgetKeyboard)
        layout.addWidget(self.keyboard)
        self.ui.widgetKeyboard.setLayout(layout)

        self.ui.backBtn.clicked.connect(self.on_back_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))

    def on_back_clicked(self):
        self.context.removeWidget(self)