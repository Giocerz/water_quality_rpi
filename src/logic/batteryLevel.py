from src.logic.INA219 import INA219
from src.logic.filters import MovingAverageFilter

class BatteryProvider:
    _instance = None  # Singleton

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(BatteryProvider, cls).__new__(cls)
            cls._instance._battery_level = None  # Inicialmente sin valor
            cls._instance.filter = MovingAverageFilter(num=5)  # Filtro con 5 valores
        return cls._instance

    def getBatteryLevel(self):
        """Devuelve el nivel de batería actual, si está disponible."""
        return self._battery_level if self._battery_level is not None else 0  # Evitar None

    def setBatteryLevel(self, level):
        """Asigna el primer valor si es necesario y aplica el filtro."""
        if self._battery_level is None:  # Primera asignación
            self._battery_level = level  
        else:
            level_filtrado = self.filter.add_value(level)  # Aplicar filtro
            self._battery_level = max(0, min(100, round(level_filtrado)))  # Limitar entre 0