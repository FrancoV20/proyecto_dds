import json

def ficha_alumno_to_json(ficha):
    return json.dumps(ficha, ensure_ascii=False, indent=2)
