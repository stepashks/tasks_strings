import json

with open('template.json') as f:
    file_content = f.read()
    template = json.loads(file_content)

print(template)