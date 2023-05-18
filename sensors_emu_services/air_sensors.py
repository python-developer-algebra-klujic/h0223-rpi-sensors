from sense_emu import SenseHat
from datetime import datetime as dt
from database.entities.air_measurements import AirMeasurement
from database.db_manager import create_measurement


def get_current_measurements() -> AirMeasurement:
    sense = SenseHat()
    current_measurement = AirMeasurement(
        time_stamp = dt.now(),
        current_temperature=round(sense.get_temperature(), 2),
        current_pressure=round(sense.get_pressure(), 2),
        current_humidity=round(sense.get_humidity(), 2)
    )
    create_measurement(current_measurement)

    return (current_measurement)
