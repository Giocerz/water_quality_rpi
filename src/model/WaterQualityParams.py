from typing import Optional

class WaterQualityParams:
    def __init__(self,
                 name: str,
                 device_id: str,
                 latitude: float,
                 longitude: float,
                 date: str,
                 hour: str,
                 sample_origin: str,
                 it_rained: str,
                 upload_state: int,
                 lote_id: int,
                 id: Optional[int] = None,
                 conductivity: Optional[float] = None,
                 oxygen: Optional[float] = None,
                 ph: Optional[float] = None,
                 tds: Optional[float] = None,
                 temperature: Optional[float] = None,
                 turbidity: Optional[float] = None,
                 battery: Optional[float] = None
                 ):
        
        self.id: Optional[int] = id
        self.name: str = name
        self.device_id: str = device_id
        self.latitude: float = latitude
        self.longitude: float = longitude
        self.date: str = date
        self.hour: str = hour
        self.conductivity: Optional[float] = conductivity
        self.oxygen: Optional[float] = oxygen
        self.ph: Optional[float] = ph
        self.tds: Optional[float] = tds
        self.temperature: Optional[float] = temperature
        self.turbidity: Optional[float] = turbidity
        self.battery: Optional[float] = battery
        self.sample_origin: str = sample_origin
        self.it_rained: str = it_rained
        self.upload_state: int = upload_state
        self.lote_id: int = lote_id

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'device_id': self.device_id,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'date': self.date,
            'hour': self.hour,
            'conductivity': self.conductivity,
            'oxygen': self.oxygen,
            'ph': self.ph,
            'tds': self.tds,
            'temperature': self.temperature,
            'turbidity': self.turbidity,
            'battery': self.battery,
            'sample_origin': self.sample_origin,
            'it_rained': self.it_rained,
            'upload_state': self.upload_state,
            'lote_id': self.lote_id
        }