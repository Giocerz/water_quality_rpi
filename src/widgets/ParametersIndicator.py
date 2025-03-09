from PySide2.QtWidgets import QWidget
from PySide2.QtCore import Qt
from PySide2.QtGui import QPixmap
from src.views.ui_ParametersIndicator import Ui_Form as Ui_S
from src.views.ui_ParametersIndicatorM import Ui_Form as Ui_M
from src.views.ui_ParametersIndicatorL import Ui_Form as Ui_L


class ParametersIndicator(QWidget):
    def __init__(self, name: str, unit: str, min_value: float = None, max_value: float = None,
                 lower_limit: float = None, upper_limit: float = None, widget_size: str = 'S'):
        super().__init__()
        self.name: str = name
        self.unit: str = unit
        self.min_value: float = min_value if min_value is not None else 0.0
        self.max_value: float = max_value if max_value is not None else 100.0
        self.lower_limit: float = lower_limit if lower_limit is not None else -20000.0
        self.upper_limit: float = upper_limit if upper_limit is not None else 20000.0
        self.widget_size: str = widget_size
        self.__setup_size()
        self.__ui_components()

    def __setup_size(self):
        if self.widget_size == 'S' or self.widget_size == 's':
            self.ui = Ui_S()
        elif self.widget_size == 'M' or self.widget_size == 'm':
            self.ui = Ui_M()
        else:
            self.ui = Ui_L()
        self.ui.setupUi(self)

    def __ui_components(self):
        self.ui.warningLbl.hide()
        self.ui.stableLbl.hide()
        self.ui.nameLbl.setText(self.name)
        self.ui.valueLbl.setText(f'---- {self.unit}',)
        self.ui.valueLbl.setAlignment(Qt.AlignRight)
        warning_pixmap = QPixmap('./src/resources/icons/warning_red.png')
        stable_pixmap = QPixmap('./src/resources/icons/water.png')
        if self.widget_size == 'L' or self.widget_size == 'l':
            warning_pixmap = warning_pixmap.scaled(35, 35)
            stable_pixmap = stable_pixmap.scaled(35, 35)
        else:
            warning_pixmap = warning_pixmap.scaled(21, 21)
            stable_pixmap = stable_pixmap.scaled(21, 21)
        self.ui.warningLbl.setPixmap(warning_pixmap)
        self.ui.stableLbl.setPixmap(stable_pixmap)


    def __acond_value(self, value: float) -> int:
        result = 100.0 / (self.max_value - self.min_value) * \
            (value - self.min_value)
        result = int(result)
        if result < 0:
            result = 0
        elif result > 100:
            result = 100
        return result

    def __verify_limits(self, value:float):
        if value < self.lower_limit or value > self.upper_limit:
            self.ui.warningLbl.show()
        else:
            self.ui.warningLbl.hide()

    def sizeHint(self):
        return self.size()

    def setValue(self, value: float):
        self.ui.valueLbl.setText(f'{value} {self.unit}',)
        self.ui.valueLbl.setAlignment(Qt.AlignRight)
        self.ui.progressBar.setValue(self.__acond_value(value))
        self.__verify_limits(value)

    def setStable(self, is_stable: float):
        if is_stable:
            self.ui.stableLbl.show()
        else:
            self.ui.stableLbl.hide()
