def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    mid = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)
def main():
    arr = list(map(int, input("Enter unsorted numbers (space-separated): ").split()))
    sorted_arr = quick_sort(arr)
    print("Sorted Array:", *sorted_arr)

if __name__ == "_main_":
    main()