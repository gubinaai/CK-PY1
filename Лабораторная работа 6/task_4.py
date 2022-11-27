import json

INPUT_FILE = "input_2.csv"

def csv_to_list_dict(file) -> list[dict]:
    list_dict = []
    list_rows = []
    with open(file, 'r') as f:
        rows = f.readlines()
        headers = rows[0].rstrip().split(sep=',')
        for row in rows[1:]:
            list_rows.append(row.rstrip().split(sep=','))
        for i in list_rows:
            i = {k:v for k, v in zip(headers, i)}
            list_dict.append(i)
    return list_dict

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))
