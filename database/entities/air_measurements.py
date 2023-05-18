from datetime import datetime as dt
from sqlalchemy import Column, Integer, Float, DateTime
from sqlalchemy.orm import declarative_base


Base = declarative_base()


class AirMeasurement(Base):
    __tablename__ = 'air-measurements'
    id = Column(Integer, primary_key=True, autoincrement=True)
    time_stamp = Column(DateTime, default=dt.now(), nullable=False)
    current_temperature = Column(Float(precision=8, decimal_return_scale=3), nullable=False)
    current_pressure = Column(Float(precision=8, decimal_return_scale=3), nullable=False)
    current_humidity = Column(Float(precision=8, decimal_return_scale=3), nullable=False)


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

    def __str__(self):
        temp = f'Temperatura: {self.current_temperature} C\n'
        temp += f'Tlak: {self.current_pressure} mbar\n'
        temp += f'Vlaznost: {self.current_humidity} %\n'
        return temp

