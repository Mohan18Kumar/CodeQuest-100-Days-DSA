def rotate_array(arr, k):
    n = len(arr)
    k = k%n
    return arr[-k:] + arr[:-k] if k != 0 else arr
arr_input = input("Enter numbers:").strip() 
arr = list(map(int,arr_input.splite()))
k = int(input("Enter rotation value (k): "))
rotated = rotate_array(arr,k)
print("Rotated array:",''.join(map(str,rotated)))