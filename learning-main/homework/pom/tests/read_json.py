import json


with open('json_data', 'r') as json_file:
    content = json_file.read()
parsed_content = json.loads(content)
print(content)
print(parsed_content)
print(parsed_content['bla'])