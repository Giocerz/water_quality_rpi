from PySide2.QtWidgets import QMainWindow, QStackedLayout
from PySide2.QtCore import QSize, QThread, Signal
from PySide2.QtGui import QIcon
from PySide2 import QtCore
from src.views.ui_Save import Ui_Save
from src.widgets.KeyboardWidget import KeyboardWidget
from src.widgets.PopupWidget import PopupWidgetInfo, LoadingPopupWidget
from src.model.WaterQualityParams import WaterQualityParams
from src.model.WaterQualityDB import WaterDataBase
from datetime import datetime
import time
import subprocess

class LocationdWorker(QThread):
    location_result = Signal(list)

    def __init__(self):
        super(LocationdWorker, self).__init__()

    def run(self):
        self.running_state = True
        subprocess.run("sudo systemctl stop gpsd.socket", shell=True)
        time.sleep(0.5)
        subprocess.run("sudo gpsd /dev/serial0 -F /var/run/gpsd.sock", shell=True)
        time.sleep(0.5)
        import gps
        session = gps.gps(mode=gps.WATCH_ENABLE)
        latitude:float = None
        longitude:float = None
        time_count = 0
        time_period = 2
        while self.running_state:
            try:
                if(time_count * time_period >= 60):
                    self.location_result.emit(['time'])
                report = session.next()

                if report['class'] == 'TPV':
                    if hasattr(report, 'lat') and hasattr(report, 'lon'):
                        latitude = float(report.lat)
                        longitude = float(report.lon)
                        self.location_result.emit([latitude, longitude])
                time.sleep(time_period)
                time_count += 1
            except Exception as e:
                self.location_result.emit(['error'])

    def stop(self):
        self.running_state = False
        self.wait()
    

class SaveDataView(QMainWindow):
    def __init__(self, context, oxygen, ph, temperature, tds, turbidity):
        QMainWindow.__init__(self)
        self.latitude = None
        self.longitude = None
        self.context = context
        self.oxygen = oxygen
        self.ph = ph
        self.temperature = temperature
        self.tds = tds
        self.turbidity = turbidity
        self.ui = Ui_Save()
        self.ui.setupUi(self)
        self.ui_components()

        self.keyboard = KeyboardWidget(self.ui.inputPlace)
        layout = QStackedLayout(self.ui.widgetKeyboard)
        layout.addWidget(self.keyboard)
        self.ui.widgetKeyboard.setLayout(layout)

        self.loading_popup = None

        self.location_worker = LocationdWorker()

        self.ui.backBtn.clicked.connect(self.on_back_clicked)
        self.ui.gpsBtn.clicked.connect(self.on_gps_clicked)
        self.ui.saveBtn.clicked.connect(self.on_save_clicked)

        self.location_worker.location_result.connect(
            self.handle_location_result)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))

    def on_back_clicked(self):
        self.context.removeWidget(self)

    def on_gps_clicked(self):
        self.loading_popup = LoadingPopupWidget(context=self.context, text='Localizando...')
        self.loading_popup.show()
        if not self.location_worker.isRunning():
            self.location_worker.start()

    def show_dialog_error(self, error: str):
        dialog = PopupWidgetInfo(context=self.context, text=error)
        dialog.show()
    
    def handle_location_result(self, location):
        self.location_worker.stop()
        self.loading_popup.close_and_delete()
        if(len(location) == 1):
            if(location[0] == 'error'):
                self.show_dialog_error('Error al intentar localizar.')
                return
            elif(location[0] == 'time'):
                self.show_dialog_error('Tiempo de espera de localización expirado.')
                return
        self.latitude = location[0]
        self.longitude = location[1]
        self.ui.label_4.setText(f'{self.latitude} , {self.longitude}')
        self.ui.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.show_dialog_error('Localización completada.')
        

    def on_save_clicked(self):
        place = self.ui.inputPlace.text()
        sample_origin = self.ui.comboBox.currentText()
        dtatetime_now = datetime.now()
        format_date = dtatetime_now.strftime("%Y-%m-%d")
        hour = dtatetime_now.strftime("%H:%M")
        if (place == ''):
            self.show_dialog_error(error='Ingrese un lugar o nombre valido')
            return
        if (sample_origin == 'Escoja una opción'):
            self.show_dialog_error(error='Seleccione el origen de la muestra')
            return
        if (self.latitude == None):
            self.show_dialog_error(error='Realice la localización antes de guardar.')
            return
        it_rained_check = self.ui.checkBox.checkState()
        it_rained = ''
        if (it_rained_check):
            it_rained = 'Si'
        else:
            it_rained = 'No'

        params = WaterQualityParams(
            name=place, device_id="CAP0003-FC", latitude=self.latitude, longitude=self.longitude,
            date=format_date, hour=str(hour), sample_origin=sample_origin, it_rained=it_rained,
            upload_state=1, lote_id=10, conductivity=self.tds * 2, oxygen=self.oxygen, ph=self.ph, 
            temperature=self.temperature, tds=self.tds, turbidity=self.turbidity
        )
        WaterDataBase.insert(params)
        self.on_back_clicked()