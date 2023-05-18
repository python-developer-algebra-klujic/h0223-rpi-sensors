from flask import Flask

from database.db_manager import get_measurements


web_app = Flask(__name__)

@web_app.route('/')
def index():
    measurements_list = get_measurements()
    temp_result = ''
    for measurement in measurements_list:
        #temp_result += str(measurement)
        temp_result += str(measurement.__dict__)
        temp_result += '\n'

    return temp_result


@web_app.route('/about_app')
def about_app():
    return 'Aplikacija za prikaz mjerenja temperature, tlaka i vla=znosti zraka'