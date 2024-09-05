import gps

# Crear un objeto gpsd
session = gps.gps(mode=gps.WATCH_ENABLE)

# Bucle para leer los datos del GPS
while True:
    try:
        report = session.next()  # Lee la siguiente información del GPS

        if report['class'] == 'TPV':  # Si el reporte es de tipo TPV (Time-Position-Velocity)
            if hasattr(report, 'lat') and hasattr(report, 'lon'):
                print(f"Latitud: {report.lat}, Longitud: {report.lon}")
            if hasattr(report, 'time'):
                print(f"Hora: {report.time}")
            if hasattr(report, 'speed'):
                print(f"Velocidad: {report.speed}")
    except KeyError:
        pass
    except KeyboardInterrupt:
        print("Interrumpido por el usuario")
        break
    except StopIteration:
        session = None
        print("No hay más datos")
        break
