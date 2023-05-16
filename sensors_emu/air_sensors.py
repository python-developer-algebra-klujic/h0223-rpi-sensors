from sense_emu import SenseHat
from sensors_emu.measurements import AirMeasurements


def get_current_measurements() -> AirMeasurements:
    sense = SenseHat()
    current_measurement = AirMeasurements(
        current_temperature=round(sense.get_temperature(), 2),
        current_pressure=round(sense.get_pressure(), 2),
        current_humidity=round(sense.get_humidity(), 2)
    )

    return (current_measurement)
