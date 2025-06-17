def push(stack, elem):
    for element in elem :
        stack.append(element)
def pop(stack, count):
    for _ in range(count):
        if stack:
            stack.pop()

def print_stack(stack):
    if stack:
        print("Current stack:",' '.join(map(str,stack)))
    else:
        print("Current stack: Empty")
stack = []
input_command = input("Enter the elements: ")
parts = input_command.split(",")
for part in parts :
    part = part.strip()
    if part.lower().startswith("push"):
        elem_str= part[5:].strip()
        if elem_str:
            elem = list(map(int,elem_str.split()))
        push(stack,elem)
    elif part.lower().startswith("pop"):
        count_str = part[4:].strip()
        if count_str.isdigit():
            pop(stack,int(count_str))


print_stack(stack)