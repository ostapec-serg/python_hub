#5. Write a script to remove duplicates from Dictionary

startDict = {
    "Sergii": 32, "Anna": 25,
    "Max": 30, "Alex": 25,
    "Alla":32, "Inna":27
}
uniDict = {}

for k,v in startDict.items():
    if v not in uniDict.values():
       uniDict.update({k:v})

print(uniDict)
