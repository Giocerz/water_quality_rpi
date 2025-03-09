class AppConstants:
    PARAMS_ATTRIBUTES = {
    "conductivity": {
        "name": "Conductividad Eléctrica",
        "maxValue": 2000.0,
        "minValue": 0.0,
        "lowerLimit": None,
        "upperLimit": 1000.0,
        "unit": "µS/cm",
    },
    "oxygen": {
        "name": "Oxigeno Disuelto",
        "maxValue": 10.0,
        "minValue": 0.0,
        "lowerLimit": None,
        "upperLimit": None,
        "stableTolerance": 0.1,
        "unit": ["mg/L", "%"],
    },
    "ph": {
        "name": "pH",
        "maxValue": 14.0,
        "minValue": 0.0,
        "lowerLimit": 6.5,
        "upperLimit": 8.5,
        "stableTolerance": 0.1,
        "unit": "pH",
    },
    "tds": {
        "name": "Sólidos Totales Disueltos",
        "maxValue": 1000.0,
        "minValue": 0.0,
        "lowerLimit": None,
        "upperLimit": 500.0,
        "stableTolerance": 2.0,
        "unit": "ppm",
    },
    "temperature": {
        "name": "Temperatura",
        "maxValue": 40.0,
        "minValue": 0.0,
        "lowerLimit": None,
        "upperLimit": 30.0,
        "unit": ["°C", "°F", "K"],
    },
    "turbidity": {
        "name": "Turbidez",
        "maxValue": 3000.0,
        "minValue": 0.0,
        "lowerLimit": None,
        "upperLimit": 42.0,
        "unit": "NTU",
    },
    }

    MONITORING_STABLE_TDS = {
        'window': 6,
        'threshold': 10.0,
        'repeat': 3,
    }
    
    MONITORING_STABLE_PH = {
        'window': 6,
        'threshold': 0.01,
        'repeat': 2,
    }
    
    MONITORING_STABLE_DO = {
        'window': 6,
        'threshold': 0.1,
        'repeat': 3,
    }
    
    MONITORING_STABLE_TURBIDITY = {
        'window': 6,
        'threshold': 30.0,
        'repeat': 3,
    }
