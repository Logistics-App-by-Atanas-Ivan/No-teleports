from core.application_data import ApplicationData
from core.command_factory import CommandFactory
from core.engine import Engine
import json
from os import path
from models.city_distances import CityDistances

cwd = path.dirname(__file__) 
# file_path = path.join(cwd,'data/app_state.json')
file_path = 'data/app_state.json'

city_distances = CityDistances()

app_data = ApplicationData.load_state(file_path, city_distances)
cmd_factory = CommandFactory(app_data, city_distances)
engine = Engine(cmd_factory, app_data, file_path)

engine.start()