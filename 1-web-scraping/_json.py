import json

person_string = '{"name":"Ali","languages":["python", "C#"]}'
person_dict = {"name":"Murat", "languages":["python", "C#"]}

# JSON String to Dictionary
# result = json.loads(person_string)

# result = result["name"]
# result = result["languages"]


# result = person["name"]
# result = person["languages"]
# result = person["languages"][0]

# with open("f15_ileri_seviye_python_modulleri_ve_web_scraping/person.json") as f:
#     data = json.load(f)
#     print(data["name"])
#     print(data["languages"])

# Dictionary to JSON String
result = json.dumps(person_dict) 

# print(result)
# print(result["name"]) # dictionary olmadığı için ulaşamayız.
# print(type(result)) # class str

# with open("f15_ileri_seviye_python_modulleri_ve_web_scraping/person.json","w") as f: # person_dict değişkenini person.json içerisine attık.
#     json.dump(person_dict, f)

person_dict = json.loads(person_string)

result = json.dumps(person_dict, indent= 4, sort_keys = True) # (indent = 4) 4 karakterlik bir girinti oluşturur. (sort_keys=True) kelimeleri sıralar.

print(person_dict)
print(result)