from dataclasses import dataclass
from typing import Optional

@dataclass
class SensorData:
    temperature: Optional[float] = None
    pH: Optional[float] = None
    TDS: Optional[float] = None
    conductivity: Optional[float] = None
    oxygen: Optional[float] = None
    turbidity: Optional[float] = None
    battery: Optional[float] = None  # Nivel de batería en porcentaje (%)
