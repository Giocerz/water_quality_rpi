from PySide2.QtCore import QTimer

class Timer:
    def __init__(self, duration, callback, repeating=False):
        """
        Constructor base para el Timer.

        :param duration: Duración en milisegundos.
        :param callback: Función a ejecutar cuando el timer expire.
        :param repeating: Si es True, el timer se repite; si es False, se ejecuta una sola vez.
        """
        self.duration = duration
        self.callback = callback
        self.repeating = repeating
        self.timer = QTimer()
        self.timer.timeout.connect(self._on_timeout)

    def _on_timeout(self):
        """Maneja el evento de timeout del timer."""
        self.callback()
        if not self.repeating:
            self.timer.stop()  # Detiene el timer si no es repetitivo

    def start(self):
        """Inicia el timer."""
        if self.repeating:
            self.timer.start(self.duration)  # Timer repetitivo
        else:
            QTimer.singleShot(self.duration, self.callback)  # Timer de una sola vez

    def cancel(self):
        """Cancela el timer."""
        self.timer.stop()

    @classmethod
    def periodic(cls, duration, callback):
        """
        Constructor factory para un timer repetitivo.

        :param duration: Duración en milisegundos.
        :param callback: Función a ejecutar cada vez que el timer expire.
        :return: Instancia de Timer configurada como repetitiva.
        """
        return cls(duration, callback, repeating=True)