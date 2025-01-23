from PySide2 import QtCore
from PySide2.QtWidgets import QMainWindow, QTableWidgetItem
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from src.views.ui_Datos import Ui_MainWindow
from src.model.WaterQualityParams import WaterQualityParams
from src.model.WaterQualityDB import WaterDataBase


class DatosView(QMainWindow):
    ELEMENTS_NUMBER = 5
    def __init__(self, context, lote_id:int):
        QMainWindow.__init__(self)
        self.context = context
        self.lote_id:int = lote_id
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()

        self.table_pages:int = 0
        self.total_data_len:int = 0
        self.current_page:int = 0

        # Configurar la tabla
        self.ui.tableWidget.setColumnCount(13)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['Nombre', 'Fecha', 'Hora', 'Latitud', 'Longitud','Temperatura', 'Oxígeno', 'TDS', 'pH', 'Conductividad', 'Turbidez', 'Origen', '¿Llovió?'])

        # Llenar la tabla con los datos de la base de datos
        self.data_table_controller()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)

        self.ui.horizontalSlider.valueChanged.connect(self.slider_value_changed)

        self.scrollBar.rangeChanged.connect(self.adjust_slider_range)
        self.scrollBar.valueChanged.connect(self.scroll_value_changed)

        self.ui.nextPageBtn.clicked.connect(self.handle_nextPageBtn)
        self.ui.prevPageBtn.clicked.connect(self.handle_prevPageBtn)

    def data_table_controller(self):
        import math
        data_list = WaterDataBase.get_water_quality_params_by_lote(self.lote_id)
        if len(data_list) == 0:
            return
        result = []
        self.total_data_len = len(data_list)
        self.table_pages = math.ceil(self.total_data_len / self.ELEMENTS_NUMBER)
        for i in range(self.table_pages):
            sub_list = []
            for j in range(self.ELEMENTS_NUMBER*i, self.ELEMENTS_NUMBER*(i+1)):
                if(j >= len(data_list)):
                    break
                sub_list.append(data_list[j])
            result.append(sub_list)
        self.data_pages = result
        self.update_page(1)
    
    def handle_nextPageBtn(self):
        self.update_page(self.current_page + 1)

    def handle_prevPageBtn(self):
        self.update_page(self.current_page - 1)
        
    def update_page(self, page):
        self.current_page = page
        if(self.current_page >= len(self.data_pages)):
            label_pages = f"{self.ELEMENTS_NUMBER*self.current_page - (self.ELEMENTS_NUMBER - 1)}-{(self.total_data_len)} de {self.total_data_len}"
        else:
            label_pages = f"{self.ELEMENTS_NUMBER*self.current_page - (self.ELEMENTS_NUMBER - 1)}-{(self.ELEMENTS_NUMBER*self.current_page)} de {self.total_data_len}"
        self.ui.dataCountLbl.setText(label_pages)
        self.ui.dataCountLbl.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.prevPageBtn.setEnabled(not(page == 1))
        self.ui.nextPageBtn.setEnabled(not(page == len(self.data_pages)))
        data = self.data_pages[self.current_page - 1]
        self.load_table_data(data=data)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/arrowr.png')
        self.ui.nextPageBtn.setIcon(icon)
        self.ui.nextPageBtn.setIconSize(QSize(30, 30))
        icon = QIcon('./src/resources/icons/arrowl.png')
        self.ui.prevPageBtn.setIcon(icon)
        self.ui.prevPageBtn.setIconSize(QSize(30, 30))
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))

        self.scrollBar = self.ui.tableWidget.horizontalScrollBar()
        self.ui.horizontalSlider.setRange(self.scrollBar.minimum(), self.scrollBar.maximum())

    def slider_value_changed(self, value):
        self.scrollBar.setValue(value)

    def adjust_slider_range(self, min, max):
        self.ui.horizontalSlider.setRange(min, max)    

    def scroll_value_changed(self, value):
        self.ui.horizontalSlider.setValue(value) 

    def on_back_clicked(self):
        self.context.removeWidget(self)

    def load_table_data(self, data:list[list[WaterQualityParams]]):
        data_list = data

        self.ui.tableWidget.setRowCount(len(data_list))

        for row_idx, data in enumerate(data_list):
            self.ui.tableWidget.setItem(row_idx, 0, QTableWidgetItem(str(data.name)))
            self.ui.tableWidget.setItem(row_idx, 1, QTableWidgetItem(str(data.date)))
            self.ui.tableWidget.setItem(row_idx, 2, QTableWidgetItem(str(data.hour)))
            self.ui.tableWidget.setItem(row_idx, 3, QTableWidgetItem(str(data.latitude)))
            self.ui.tableWidget.setItem(row_idx, 4, QTableWidgetItem(str(data.longitude)))

            # Temperatura (si no es None)
            if data.temperature is not None:
                self.ui.tableWidget.setItem(row_idx, 5, QTableWidgetItem(str(data.temperature)))

            # Oxígeno (si no es None)
            if data.oxygen is not None:
                self.ui.tableWidget.setItem(row_idx, 6, QTableWidgetItem(str(data.oxygen)))

            # TDS (si no es None)
            if data.tds is not None:
                self.ui.tableWidget.setItem(row_idx, 7, QTableWidgetItem(str(data.tds)))

            # pH (si no es None)
            if data.ph is not None:
                self.ui.tableWidget.setItem(row_idx, 8, QTableWidgetItem(str(data.ph)))

            # Conductividad (si no es None, calculada como el doble de TDS)
            if data.tds is not None:
                conductividad = data.tds * 2
                self.ui.tableWidget.setItem(row_idx, 9, QTableWidgetItem(str(conductividad)))
            
            if data.turbidity is not None:
                self.ui.tableWidget.setItem(row_idx, 10, QTableWidgetItem(str(data.turbidity)))

            self.ui.tableWidget.setItem(row_idx, 11, QTableWidgetItem(str(data.sample_origin)))
            self.ui.tableWidget.setItem(row_idx, 12, QTableWidgetItem(str(data.it_rained)))