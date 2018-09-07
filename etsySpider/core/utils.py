import json


def save_to_json(data):
    with open(data, "a", encoding="utf-8") as fs:
        line = json.dumps(data, ensure_ascci=False) + "\n"
        fs.write(line)


def save_to_mysql(data):
    pass


def save_excel(data):
    pass

