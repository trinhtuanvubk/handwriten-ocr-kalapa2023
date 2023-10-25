import json

with open('./json_data.txt', 'a+') as o:
    with open("labels.json", 'r') as f:
        data = json.load(f)
        print(data)
        for d in data.values():
            if len(d) > 55:
                d = d[:55].rsplit(",", 1)[0]
            o.write(d + "\n")
