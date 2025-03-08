from PySide2.QtWidgets import QMainWindow, QGridLayout, QWidget, QSizePolicy, QVBoxLayout
from PySide2.QtGui import QIcon
from PySide2.QtCore import QSize, Qt
from src.views.ui_Folders_view import Ui_MainWindow
from src.widgets.FolderWidget import FolderWidget
from src.model.Models import LoteModel
from src.model.WaterQualityDB import WaterDataBase
from src.views.DatosView.DatosView import DatosView
from src.package.Navigator import Navigator
from src.widgets.PopupWidget import PopupWidgetInfo, PopupWidget, LoadingPopupWidget, ProgressPopupWidget
from src.services.internetService import InternetChecker
from src.services.UploadDataService import UploadService

class FoldersView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.folders_list: list[LoteModel] = []
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()
        self.setup_list()

        self.init_workers()
        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.verticalSlider.valueChanged.connect(self.slider_value_changed)

        self.scrollBar.rangeChanged.connect(self.adjust_slider_range)
        self.scrollBar.valueChanged.connect(self.scroll_value_changed)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))
        icon = QIcon('./src/resources/icons/delete.png')
        self.ui.uploadBtn.setIcon(icon)
        self.ui.uploadBtn.setIconSize(QSize(30, 30))
        self.ui.uploadBtn.hide()
        self.scrollBar = self.ui.scrollArea.verticalScrollBar()
        self.ui.verticalSlider.setRange(self.scrollBar.minimum(), self.scrollBar.maximum())
        self.ui.emptyFoldersNoticeLbl.hide()
        self.ui.verticalSlider.hide()

    def load_data(self):
        self.folders_list = WaterDataBase.get_lotes()

    def on_back_clicked(self):
        self.stop_workers()
        Navigator.pop(context=self.context, view= self)

    def on_push_folder_widget(self, id:int, name:str):
        Navigator.push(context= self.context, view= DatosView(context=self.context, lote_id=id, update_folder_view = self.setup_list))
    
    def setup_list(self):
        self.load_data()

        if len(self.folders_list) == 0:
            self.ui.emptyFoldersNoticeLbl.show()
            self.ui.verticalSlider.hide()
            return

        # Crear el contenedor principal y el layout vertical
        container_widget = QWidget()
        main_layout = QVBoxLayout(container_widget)
        main_layout.setAlignment(Qt.AlignTop)  # Alinear contenido en la parte superior
        main_layout.setSpacing(10)

        # Crear el layout en cuadrícula
        grid_layout = QGridLayout()
        grid_layout.setSpacing(10)

        num_cols = 3  # Número de columnas
        for i, folder in enumerate(self.folders_list):
            # Crear y configurar el widget
            product_widget = FolderWidget(id=folder.id, name=folder.name, description=folder.description, on_push=self.on_push_folder_widget)
            product_widget.setFixedSize(133, 100)  # Fijar tamaño del widget
            product_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

            # Calcular la fila y columna
            row = i // num_cols
            col = i % num_cols

            # Establecer tamaño mínimo para filas y columnas
            grid_layout.setRowMinimumHeight(row, 100)
            grid_layout.setColumnMinimumWidth(col, 133)

            # Agregar el widget al layout
            grid_layout.addWidget(product_widget, row, col)

        # Agregar el layout en cuadrícula al layout principal
        main_layout.addLayout(grid_layout)

        # Ajustar el contenedor dentro del ScrollArea
        self.ui.scrollArea.setWidget(container_widget)
        self.ui.scrollArea.setWidgetResizable(True)
        self.ui.uploadBtn.show()


    def slider_value_changed(self, value):
        self.scrollBar.setValue(value)

    def adjust_slider_range(self, min, max):
        self.ui.verticalSlider.show()
        self.ui.verticalSlider.setRange(min, max)    

    def scroll_value_changed(self, value):
        self.ui.verticalSlider.setValue(value) 

    #Metodos de subida
    def init_workers(self):
        self.internet_checker = InternetChecker()
        self.upload_service = UploadService()
        self.internet_checker.connection_status.connect(self.internet_check_result)
        self.upload_service.upload_finished.connect(self.upload_finished_result)
        self.upload_service.progress.connect(self.handle_upload_progress)

    def stop_workers(self):
        pass
        if self.internet_checker.isRunning():
            self.internet_checker.wait()
        if self.upload_service.isRunning():
            self.upload_service.stop()

    def on_upload_clicked(self):
        count_data_no_uploaded =  WaterDataBase.count_samples_not_updated()
        if count_data_no_uploaded == 0:
            popup =  PopupWidget(context=self.context, text='Todos los datos estan<br>sincronizados')
            popup.show()
            return
        if count_data_no_uploaded > 1:
            text = f'Hay {count_data_no_uploaded} muestras sin<br>sincronizar ¿Desea subirlas?'
        else:
            text = f'Hay una muestra sin<br>sincronizar ¿Desea subirla?'
        def yes_callback():
            self.internet_checker.start()
        def no_callback():
            pass
        popup = PopupWidget(context=self.context, text=text, yes_callback=yes_callback, no_callback=no_callback)
        popup.show()
    
    def internet_check_result(self, result):
        if not result:
            popup = PopupWidgetInfo(context=self.context, text='No hay conexion a internet')
            popup.show()
            return
        self.upload_service.start()
        self.progress_popup = ProgressPopupWidget(context=self.context, text='Sincronizando...')
        self.progress_popup.show()

    def handle_upload_progress(self, upload_progress):
        progress =  round(upload_progress[0]/upload_progress[1] * 100)
        self.progress_popup.set_value(progress)

    def upload_finished_result(self, result, error_msg):
        if result:
            text = 'Los datos se sincronizaron<br>exitosamente.'
        else:
            text = error_msg
        self.progress_popup.close_and_delete()
        popup =  PopupWidgetInfo(context=self.context, text=text)
        popup.show()
