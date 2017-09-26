import json

with open('taskdef.json') as data_file:    
    data = json.load(data_file)
   
return data["taskDefinition"]["revision"]
