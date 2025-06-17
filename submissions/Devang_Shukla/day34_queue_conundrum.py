from collections import deque

def main():
    enqueue_input = input("Enter numbers to enqueue: ").strip()
    enqueue_values = list(map(int, enqueue_input.split()))

    k = int(input("How many values to dequeue? "))

    queue = deque(enqueue_values)

    for _ in range(min(k, len(queue))):
        queue.popleft()

    if queue:
        print("Remaining Queue:", ' '.join(map(str, queue)))
    else:
        print("Remaining Queue: Empty")

if __name__ == "_main_":
    main()