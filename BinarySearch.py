def halfArray(array, target):
    midPoint = int(len(array)/2)
    if array[midPoint] > target:
        return array[0:midPoint]
    return array[midPoint::]

def binarySearch(data, target):
    while len(data) > 2:
        print(data)
        data = halfArray(data, target)
    if target == data[0] or target == data[1]: print(f"Found: {target}!")
    else: print(f"{target} not found! Closest values: {data}")

binarySearch([0,23,54,100,1232,4324,54903,432000], int(input("Target: ")))
