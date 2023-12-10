import json

def save_data(my_data_file,my_garage):
    json_string = json.dumps(my_garage)
    # save the list in a file
    with open(my_data_file, 'w') as file:
        file.write(json_string)

def load_data(my_data_file , my_garage):# load a list from a file
    try:
        with open(my_data_file, 'r') as file:
            json_string = file.read()
        my_garage = json.loads(json_string)
        return my_garage
    except: pass