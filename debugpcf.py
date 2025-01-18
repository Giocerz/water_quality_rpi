from src.logic.PCF8574 import PCF8574
import time
if __name__ == "__main__":
    pcf = PCF8574(address=0x20)

    while True:
        for i in range(8):
            estado = pcf.read_pin(i)
            print(f"Pin P{i}: {'Activo' if estado else 'Inactivo'}")
        time.sleep(1)
