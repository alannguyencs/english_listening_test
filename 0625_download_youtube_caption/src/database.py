from constants import *

def load_database():
    json_database = []
    data = glob.glob(DATABASE_PATH + '*.json')
    for json_path in data:
        with open(json_path) as json_file:
            json_data = json.load(json_file, object_pairs_hook=OrderedDict)
            json_database.append(json_data)
    return json_database

