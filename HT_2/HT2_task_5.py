#5. Write a script to remove duplicates from Dictionary

startDict = {
    "Sergii": 32, "Anna": [25, "age"],
    "Max": 30, "Alex": [25, "age"],
    "Alla":32, "Inna":[27, "age"],
    "John": [30, "age"], "Jack": [25, "age"],
}
uniDict = {}

for k,v in startDict.items():
    if v not in uniDict.values():
       uniDict.update({k:v})

print(uniDict)
