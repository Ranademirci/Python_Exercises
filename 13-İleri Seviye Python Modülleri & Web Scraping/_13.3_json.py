import json
person_string='{"name":"ali","languages":["python,C#"]}'
# #JSON string to dict
# result=json.loads(person_string)
# result=result["name"]

# with open("person.json") as f:
#     data=json.load(f)
#     print(data["name"])

person_dict={
    "name":"ali",
    "languages":["Python","C#"]

}
# dict to json string
# result=json.dumps(person_dict)
# print(result)

with open("person.json","w")as f:
    json.dump(person_dict,f)


person_dict=json.loads(person_string)
result=json.dumps(person_dict,indent=4,sort_keys=True)
print(person_dict)
print(result)