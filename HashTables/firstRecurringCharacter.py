def firstRecurringCharacter(arr):
    for i in range(0, len(arr)):
        for j in range(i+1, len(arr)):
            if(arr[i]==arr[j]):
                return arr[i]
            
def firstRecurringCharacter2(arr):
    vistos = set()

    for i in arr:
        if i in vistos:
            return i
        vistos.add(i)




# print(firstRecurringCharacter([1,5,3,4,4,6]))
print(firstRecurringCharacter2([1,5,3,4,4,6]))
