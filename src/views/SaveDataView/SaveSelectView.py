from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon
from src.views.ui_SaveSelect import Ui_MainWindow
from src.views.SaveDataView.SaveDataView import SaveDataView
from src.package.Navigator import Navigator
from src.model.SensorData import SensorData
from typing import Optional

class SaveSelectView(QMainWindow):
    def __init__(self, context, capture_samples: list[SensorData]):
        super().__init__()
        self.context = context
        self.capture_samples : list[SensorData] = capture_samples

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui_components()

        self.ui.allCheckBox.mousePressEvent = self.on_press_all_checkbox
        self.ui.meanCheckBox.mousePressEvent = self.on_pres_mean_checkbox
        self.ui.continueBtn.clicked.connect(self.on_continue_clicked)

    def ui_components(self):
        icon = QIcon('./src/resources/icons/back.png')
        self.ui.backBtn.setIcon(icon)
        self.ui.backBtn.setIconSize(QSize(30, 30))
        self.ui.continueBtn.hide()
        self.averaged_samples: SensorData = self.calculate_average()

        text = f"Promedio: Temp: {self.averaged_samples.temperature}"

        if self.averaged_samples.oxygen is not None:
            text += f", OD: {self.averaged_samples.oxygen}"

        if self.averaged_samples.tds is not None:
            text += f", TDS: {self.averaged_samples.tds}"

        if self.averaged_samples.conductivity is not None:
            text += f", CE: {self.averaged_samples.conductivity}"

        if self.averaged_samples.ph is not None:
            text += f", pH: {self.averaged_samples.ph}"

        if self.averaged_samples.turbidity is not None:
            text += f", Turbidez: {self.averaged_samples.turbidity}"

        self.ui.meanLbl.setText(text)
        self.ui.allLbl.setText(F'Total de muestras: {len(self.capture_samples)}')
        self.ui.allCheckBox.setChecked(True)
        self.ui.meanCheckBox.setChecked(False)
        self.ui.continueBtn.show()

    def on_press_all_checkbox(self, event):
        """ Maneja el evento de clic en allCheckBox, desmarcando meanCheckBox si es necesario. """
        if self.ui.allCheckBox.isChecked():
            self.ui.allCheckBox.setChecked(False)
        else:
            self.ui.allCheckBox.setChecked(True)
            self.ui.meanCheckBox.setChecked(False)  # Desmarca el otro checkbox

    def on_pres_mean_checkbox(self, event):
        """ Maneja el evento de clic en meanCheckBox, desmarcando allCheckBox si es necesario. """
        if self.ui.meanCheckBox.isChecked():
            self.ui.meanCheckBox.setChecked(False)
        else:
            self.ui.meanCheckBox.setChecked(True)
            self.ui.allCheckBox.setChecked(False)  # Desmarca el otro checkbox

    def on_continue_clicked(self):
        if self.ui.allCheckBox.isChecked():
            view =  SaveDataView(context= self.context, capture_samples=self.capture_samples)
        else:
            view =  SaveDataView(context= self.context, capture_samples=self.averaged_samples)
        Navigator.pushReplacement(context=self.context, view=view)

    def calculate_average(self) -> SensorData:
        """ Calcula el promedio de cada parámetro en capture_samples, ignorando valores None """
        def average(values: list[Optional[float]]) -> Optional[float]:
            if values[0] is None:  # Solo verifica el primer elemento
                return None
            valid_values = [v for v in values if v is not None]
            return round(sum(valid_values) / len(valid_values) , 2) if valid_values else None

        return SensorData(
            temperature=average([sample.temperature for sample in self.capture_samples]),
            ph=average([sample.ph for sample in self.capture_samples]),
            tds=average([sample.tds for sample in self.capture_samples]),
            conductivity=average([sample.conductivity for sample in self.capture_samples]),
            oxygen=average([sample.oxygen for sample in self.capture_samples]),
            turbidity=average([sample.turbidity for sample in self.capture_samples]),
            battery=average([sample.battery for sample in self.capture_samples])
        )
