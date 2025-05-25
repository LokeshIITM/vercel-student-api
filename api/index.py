import json

def handler(request, response):
    # Enable CORS
    response.headers["Access-Control-Allow-Origin"] = "*"

    # Load student data
    with open("q-vercel-python.json", "r") as f:
        data = json.load(f)

    # Get list of names from query
    query_names = request.query.getlist("name")

    # Map names to marks
    name_to_mark = {student["name"]: student["marks"] for student in data}
    marks = [name_to_mark.get(name, None) for name in query_names]

    return response.json({ "marks": marks })
