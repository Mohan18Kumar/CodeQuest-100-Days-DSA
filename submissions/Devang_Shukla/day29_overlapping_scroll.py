def find_common_elements(list1,list2):
    set1 = set(list1)
    set2 = set(list2)
    common = set1&set2
    if common:
        print("Common elements:",*sorted(common))
    else:
        print("No common elements found!")
list1_input = input("Enter first list: ")
list2_input = input("Enter second list: ")        
list1 = list(map(int,list1_input.strip()))    
list2 = list(map(int,list2_input.strip().split()))
find_common_elements(list1,list2)        