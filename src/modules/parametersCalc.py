def calculateTds(temperature:float, voltage:float) -> float:
  kValue = 1.0
  if (voltage > 0.05) :
    tdsFactor = 0.5
    ecValue = (133.42 * voltage * voltage * voltage - 255.86 * voltage * voltage + 857.39 * voltage) * kValue
    ecValue25 = ecValue / (1.0 + 0.02 * (temperature - 25.0))
    tdsValue = ecValue25 * tdsFactor
    return tdsValue
  else:
    return 0.0
  
def calculatePh(voltage:float) -> float:
  offset = 2.162
  if (voltage > offset):
    return 7 - (voltage - offset) / 0.167
  else:
    return 7 + (offset - voltage) / 0.167