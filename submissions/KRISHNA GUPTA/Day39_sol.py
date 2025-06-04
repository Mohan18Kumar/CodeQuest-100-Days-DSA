numbers= list(map(int, input("Input:").split()))
def quick_sort(numbers):
    if len(numbers)<=1:
        return numbers
    
    pivot=numbers[0]
    left=[]
    right=[]

    for i in range(1, len(numbers)):
        if numbers[i]<pivot:
            left.append(numbers[i])
        else:
            right.append(numbers[i])

    sort_left=quick_sort(left)
    sort_right=quick_sort(right)

    return sort_left + [pivot] + sort_right
print("Output:", *quick_sort(numbers))