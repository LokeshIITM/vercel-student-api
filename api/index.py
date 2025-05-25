import json

def handler(request, response):
    response.headers["Access-Control-Allow-Origin"] = "*"

    with open("q-vercel-python.json", "r") as f:
        data = json.load(f)

    query_names = request.query.getlist("name")

    name_to_mark = {student["name"]: student["marks"] for student in data}
    marks = [name_to_mark.get(name, None) for name in query_names]

    return response.json({ "marks": marks })
