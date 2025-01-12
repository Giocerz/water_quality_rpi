import pandas as pd
import os

class CalibrationTurbidityValues:
    def __init__(self):
        file_path = './src/config/calibrationTurbidityValues.txt'
        if not os.path.exists(file_path):
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            default_content = """calibration_values
0.28
108
287
475
"""
            with open(file_path, 'w') as file:
                file.write(default_content)
        self.df = pd.read_csv(file_path)

    def read_values(self) -> list[float]:
        return self.df['calibration_values'].astype(float).tolist()

    def save_values(self, newValues:list):
        for i in range(len(newValues)):
            self.df.loc[i, 'calibration_values'] = newValues[i]
        self.df.to_csv('./src/config/calibrationTurbidityValues.txt', index=False)
        self.df = None



class SaveCalibration:
    def __init__(self):
        file_path = './src/config/calibrationSettings.txt'
        if not os.path.exists(file_path):
            os.makedirs(os.path.dirname(file_path), exist_ok=True)
            default_content = """calibration_values
1.0
1.8662444532609028
15.9755483962
15.9755483962
31.5625
1.681551316873684
-3132.55408
20693.82562
-33606.5574
"""
            with open(file_path, 'w') as file:
                file.write(default_content)
        self.df = pd.read_csv(file_path)
    
    def add_kvalue(self, k_value:float):
        self.df.loc[0, 'calibration_values'] = k_value
    
    def add_ph_offset(self, ph_offset:float):
        self.df.loc[1, 'calibration_values'] = ph_offset
    
    def add_ph_slopes(self, slopes:list):
        self.df.loc[2, 'calibration_values'] = slopes[0]
        self.df.loc[3, 'calibration_values'] = slopes[1]
   
    def add_oxygen(self, oxygen_temperature:float, oxygen_offset:float):
        self.df.loc[4, 'calibration_values'] = oxygen_temperature
        self.df.loc[5, 'calibration_values'] = oxygen_offset
    
    def add_turbidity(self, coeff:list):
        for i in range(len(coeff)):
            self.df.loc[i + 6, 'calibration_values'] = coeff[i]
    
    def save(self):
        self.df.to_csv('./src/config/calibrationSettings.txt', index=False)
        self.df = None
        
