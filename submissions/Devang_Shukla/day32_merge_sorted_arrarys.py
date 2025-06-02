def merge_sorted_arrays(arr1,arr2):
    merged = []
    i = j = 0
    n1,n2 = len(arr1), len(arr2)
    while i<n1 and j < n2:
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i+=1
        else:
            merged.append(arr2[j])
            j+=1
    while i<n1:
        merged.append(arr1[i])
        i+=1
    while j<n2:
        merged.append(arr2[j])
        j+=1
    return merged
arr1 = list(map(int,input("Enter first sorted array:").strip().split()))
arr2 = list(map(int, input("Enter second sorted arrary:").strip().split()))
result = merge_sorted_arrays(arr1,arr2)
print("Merged sorted array:",''.join(map(str,result)))                

