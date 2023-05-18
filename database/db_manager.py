from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.entities.air_measurements import AirMeasurement, Base

db_engine = create_engine('sqlite:///database/db_file/ari-measurements.sqlite')
Session = sessionmaker()
Session.configure(bind=db_engine)
session = Session()

def db_init():
    Base.metadata.create_all(db_engine)


def create_measurement(data: AirMeasurement):
    session.add(data)
    session.commit()


def get_measurements() -> list:
    return session.query(AirMeasurement).all()


def get_measurement(id: int) -> list:
    return (session.query(AirMeasurement)
                .filter(AirMeasurement.id == id)
                .one_or_none())
