

class AirMeasurements():
    def __init__(self,
                 current_temperature: float = -280,
                 current_pressure: float = 0,
                 current_humidity: float = -1) -> None:
        self.current_temperature: float = current_temperature
        self.current_pressure: float = current_pressure
        self.current_humidity: float = current_humidity

    def get_temp_celsius(self):
        if self.current_temperature == -280:
            return f'Senzor temperature ne radi!'
        else:
            return f'{self.current_temperature} C'

    def get_temp_farenheit(self):
        return f'{(self.current_temperature * (9 / 5)) + 32} F'
    
    def get_pressure_mbar(self):
        return f'{self.current_pressure} mbar'

    def get_pressure_hpa(self):
        return f'{self.current_pressure} hPa'
    
    def get_humidity(self):
        return f'{self.current_humidity} %'