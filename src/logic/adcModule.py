import board
import busio
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

class ADCModule():
    def __init__(self):
        super(ADCModule, self).__init__()
        i2c = busio.I2C(board.SCL, board.SDA)
        self.ads = ADS.ADS1115(i2c)
        self.ads.gain = 2/3

    def channel(self, channel:int) -> AnalogIn:
        if(channel == 0):
            return AnalogIn(self.ads, ADS.P0)
        elif (channel == 1):
            return AnalogIn(self.ads, ADS.P1)
        elif(channel == 2):
            return AnalogIn(self.ads, ADS.P2)
        else:
            return AnalogIn(self.ads, ADS.P3)
    



