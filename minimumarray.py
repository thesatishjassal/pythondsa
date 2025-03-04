array = [10, 12, 94]
minvalue = array[0]

for i in range(0, len(array), 2):
    if array[i] > minvalue:
        minvalue = array[i]

print("Minimum values", minvalue)