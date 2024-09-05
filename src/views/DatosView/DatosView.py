from PySide2.QtWidgets import QMainWindow, QTableWidgetItem
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from src.views.ui_Datos import Ui_Datos
from src.model.WaterQualityParams import WaterQualityParams
from src.model.WaterQualityDB import WaterDataBase


class DatosView(QMainWindow):
    def __init__(self, context):
        QMainWindow.__init__(self)
        self.context = context
        self.ui = Ui_Datos()
        self.ui.setupUi(self)
        self.ui_components()

        # Configurar la tabla
        self.ui.tableWidget.setColumnCount(13)
        self.ui.tableWidget.setHorizontalHeaderLabels(
            ['Nombre', 'Fecha', 'Hora', 'Latitud', 'Longitud', 'Temperatura', 'Oxígeno', 'TDS', 'pH', 'Conductividad', 'Turbidez', 'Origen', '¿Llovió?'])

        # Llenar la tabla con los datos de la base de datos
        self.load_table_data()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))

    def on_back_clicked(self):
        self.context.removeWidget(self)

    def load_table_data(self):
        data_list = WaterDataBase.get_water_quality_params()

        self.ui.tableWidget.setRowCount(len(data_list))

        for row_idx, data in enumerate(data_list):
            self.ui.tableWidget.setItem(
                row_idx, 0, QTableWidgetItem(str(data.name)))
            self.ui.tableWidget.setItem(
                row_idx, 1, QTableWidgetItem(str(data.date)))
            self.ui.tableWidget.setItem(
                row_idx, 2, QTableWidgetItem(str(data.hour)))
            self.ui.tableWidget.setItem(
                row_idx, 3, QTableWidgetItem(str(data.latitude)))
            self.ui.tableWidget.setItem(
                row_idx, 4, QTableWidgetItem(str(data.longitude)))

            # Temperatura (si no es None)
            if data.temperature is not None:
                self.ui.tableWidget.setItem(
                    row_idx, 5, QTableWidgetItem(str(data.temperature)))

            # Oxígeno (si no es None)
            if data.oxygen is not None:
                self.ui.tableWidget.setItem(
                    row_idx, 6, QTableWidgetItem(str(data.oxygen)))

            # TDS (si no es None)
            if data.tds is not None:
                self.ui.tableWidget.setItem(
                    row_idx, 7, QTableWidgetItem(str(data.tds)))

            # pH (si no es None)
            if data.ph is not None:
                self.ui.tableWidget.setItem(
                    row_idx, 8, QTableWidgetItem(str(data.ph)))

            # Conductividad (si no es None, calculada como el doble de TDS)
            if data.tds is not None:
                conductividad = data.tds * 2
                self.ui.tableWidget.setItem(
                    row_idx, 9, QTableWidgetItem(str(conductividad)))

            if data.turbidity is not None:
                self.ui.tableWidget.setItem(
                    row_idx, 10, QTableWidgetItem(str(data.turbidity)))

            self.ui.tableWidget.setItem(
                row_idx, 11, QTableWidgetItem(str(data.sample_origin)))
            self.ui.tableWidget.setItem(
                row_idx, 12, QTableWidgetItem(str(data.it_rained)))
