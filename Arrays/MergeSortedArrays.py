# Two Pointers

def merge_sorted_arrays(arr1, arr2):
    arr = []
    i = 0
    j = 0

    while(i < len(arr1) and j < len(arr2)):
        if(arr1[i] < arr2[j]):
            arr.append(arr1[i])
            i+=1
        else:
            arr.append(arr2[j])
            j+=1

    arr.extend(arr1[i:])
    arr.extend(arr2[j:])
        
    return arr
    
print(merge_sorted_arrays([1,3,5], [1,2,4,8,12]))