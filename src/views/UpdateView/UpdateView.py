from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from src.views.ui_UpdateView import Ui_MainWindow
from src.widgets.PopupWidget import LoadingPopupWidget, PopupWidgetInfo
from src.services.internetService import InternetChecker
from src.package.Navigator import Navigator


class UpdateView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()

        self.internet_checker = InternetChecker()

        self.internet_checker.connection_status.connect(self.internet_check_result)
        self.ui.backBtn.clicked.connect(self.on_back_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))
    
    def on_back_clicked(self):
        if not self.internet_checker.isRunning():
            self.internet_checker.wait()
        Navigator.pop(context= self.context, view=self)
    
    def showEvent(self, event):
        """Muestra el popup de carga después de que la ventana principal sea visible."""
        super(UpdateView, self).showEvent(event)
        self.init_internet_check()
    
    def init_internet_check(self):
        self.loading_popup = LoadingPopupWidget(context=self.context, text="Verificando conexión")
        self.loading_popup.show()
        self.internet_checker.start()
    
    def internet_check_result(self, result):
        self.loading_popup.close_and_delete()
        if result:
            text = "Hay conexion"
        else: 
            text = "No hay conexion"
        popup = PopupWidgetInfo(context=self.context, text=text)
        popup.show()