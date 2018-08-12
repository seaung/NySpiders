import json


def save_to_json(data):
    with open("etsy.json", "a") as fs:
        fs.write(json.dumps(data))


def save_to_mysql(data):
    pass


def save_excel(data):
    pass

