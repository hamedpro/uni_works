dictio={}

for i in range (10000):
    entry=input()
    if entry==' ':
        break
    entry=entry.split(':')
    key=entry[0]
    value=entry[1]
    if key not in dictio.keys():
        dictio[key]=[value]
    else :
        dictio[key].append(int(value))

def sort_by_keys(dct: dict) -> dict:
    return {k: dct[k] for k in sorted(dct.keys())}

print(sort_by_keys(dictio))