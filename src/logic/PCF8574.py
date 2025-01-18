import smbus

class PCF8574:
    def __init__(self, i2c_bus=1, address=0x20):
        self.bus = smbus.SMBus(i2c_bus)
        self.address = address

    def read_all_pins(self):
        try:
            return self.bus.read_byte(self.address)
        except Exception as e:
            print(f"Error al leer los pines: {e}")
            return 0xFF

    def read_pin(self, pin):
        if pin < 0 or pin > 7:
            raise ValueError("El número de pin debe estar entre 0 y 7.")

        estado = self.read_all_pins()
        return bool((estado >> pin) & 0x01)

    def read_P0(self):
        return self.read_pin(0)

    def read_P1(self):
        return self.read_pin(1)

    def read_P2(self):
        return self.read_pin(2)

    def read_P3(self):
        return self.read_pin(3)

    def read_P4(self):
        return self.read_pin(4)

    def read_P5(self):
        return self.read_pin(5)

    def read_P6(self):
        return self.read_pin(6)

    def read_P7(self):
        return self.read_pin(7)