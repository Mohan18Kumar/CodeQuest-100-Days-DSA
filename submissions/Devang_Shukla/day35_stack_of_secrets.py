def main():
    push_input = input("Enter numbers to push: ").strip()
    push_values = list(map(int, push_input.split()))

    k = int(input("How many values to pop? "))

    stack = []

    for val in push_values:
        stack.append(val)

    for _ in range(min(k, len(stack))):
        stack.pop()

    if stack:
        print("Current Stack:", ' '.join(map(str, stack)))
    else:
        print("Current Stack: Empty")

if __name__ == "_main_":
    main()