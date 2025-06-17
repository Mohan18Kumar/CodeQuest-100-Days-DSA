def check_even_parity(binary_signal):
    ones_count = binary_signal.count('1')

    if ones_count % 2 == 0:
        print("Even Parity")
    else:
        print("Odd Parity – Error Detected!")

binary_signal = input("Enter binary signal: ").strip()

if all(bit in ['0', '1'] for bit in binary_signal):
    check_even_parity(binary_signal)
else:
    print("Invalid binary signal! Please enter only 0s and 1s.")