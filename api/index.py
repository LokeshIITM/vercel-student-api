import json
import os

def handler(request, response):
    response.headers["Access-Control-Allow-Origin"] = "*"

    # Get absolute path to JSON file
    json_path = os.path.join(os.path.dirname(__file__), '..', 'q-vercel-python.json')
    
    with open(json_path, "r") as f:
        data = json.load(f)

    query_names = request.query.getlist("name")
    name_to_mark = {student["name"]: student["marks"] for student in data}
    marks = [name_to_mark.get(name, None) for name in query_names]

    return response.json({ "marks": marks })
