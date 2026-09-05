BASE_NAMES = {2: "Binary", 8: "Octal", 10: "Decimal", 16: "Hexadecimal"}

def to_base(n, base=2):
    if n == 0:
        return "0"
    digits = "0123456789ABCDEF"
    result = ""
    neg = n < 0
    if neg:
        n = abs(n)
    while n > 0:
        result = digits[n % base] + result
        n //= base
    return ("-" if neg else "") + result

def from_base(num_str, base=2):
    num_str = num_str.strip().upper()
    if not num_str:
        raise ValueError("Input is empty")
    return int(num_str, base)

def decimal_to_binary(n):
    return to_base(n, 2)

def binary_to_decimal(binary_str):
    return from_base(binary_str, 2)

def binary_to_base(binary_str, base):
    return to_base(binary_to_decimal(binary_str), base)

def base_to_binary(num_str, base):
    return to_base(from_base(num_str, base), 2)

def decimal_to_base(n, base):
    return to_base(n, base)

def base_to_decimal(num_str, base):
    return from_base(num_str, base)

def add_binary(b1, b2):
    dec1 = binary_to_decimal(b1)
    dec2 = binary_to_decimal(b2)
    result = dec1 + dec2
    return decimal_to_binary(result)

def subtract_binary(b1, b2):
    dec1 = binary_to_decimal(b1)
    dec2 = binary_to_decimal(b2)
    result = dec1 - dec2
    if result < 0:
        return f"-{decimal_to_binary(abs(result))}"
    return decimal_to_binary(result)

def multiply_binary(b1, b2):
    dec1 = binary_to_decimal(b1)
    dec2 = binary_to_decimal(b2)
    result = dec1 * dec2
    return decimal_to_binary(result)

def divide_binary(b1, b2):
    dec1 = binary_to_decimal(b1)
    dec2 = binary_to_decimal(b2)
    if dec2 == 0:
        return "Error: Division by zero"
    result = dec1 // dec2
    return decimal_to_binary(result)

def modulo_binary(b1, b2):
    dec1 = binary_to_decimal(b1)
    dec2 = binary_to_decimal(b2)
    if dec2 == 0:
        return "Error: Division by zero"
    return decimal_to_binary(dec1 % dec2)

def bitwise_and(b1, b2):
    return decimal_to_binary(binary_to_decimal(b1) & binary_to_decimal(b2))

def bitwise_or(b1, b2):
    return decimal_to_binary(binary_to_decimal(b1) | binary_to_decimal(b2))

def bitwise_xor(b1, b2):
    return decimal_to_binary(binary_to_decimal(b1) ^ binary_to_decimal(b2))

def bitwise_not(b1):
    return decimal_to_binary(~binary_to_decimal(b1))

def text_to_binary(text):
    return " ".join(format(ord(c), "08b") for c in text)

def binary_to_text(binary_str):
    parts = binary_str.strip().split()
    try:
        return "".join(chr(int(b, 2)) for b in parts)
    except ValueError:
        return "Error: Invalid binary input"

def to_base_fractional(n, base=2, precision=10):
    """แปลงเลขทศนิยม (float) เป็น base ที่กำหนด"""
    neg = n < 0
    n = abs(n)
    int_part = int(n)
    frac_part = n - int_part
    int_result = to_base(int_part, base)
    if frac_part == 0:
        return ("-" if neg else "") + int_result
    frac_result = ""
    for _ in range(precision):
        frac_part *= base
        digit = int(frac_part)
        frac_result += "0123456789ABCDEF"[digit]
        frac_part -= digit
        if frac_part == 0:
            break
    return ("-" if neg else "") + f"{int_result}.{frac_result}"

def base_fractional_to_decimal(num_str, base=2):
    """แปลงเลขฐานแบบมีจุดทศนิยมเป็น float (base 10)"""
    neg = num_str.startswith("-")
    if neg:
        num_str = num_str[1:]
    if "." in num_str:
        int_str, frac_str = num_str.split(".")
    else:
        int_str, frac_str = num_str, ""
    decimal = int(int_str, base)
    for i, ch in enumerate(frac_str):
        decimal += int(ch, base) / (base ** (i + 1))
    return -decimal if neg else decimal

def display_menu():
    print("\n===== Number Base System =====")
    print("1. Decimal to Binary")
    print("2. Binary to Decimal")
    print("3. Base to Base (แปลงระหว่างฐาน 2/8/10/16)")
    print("4. Add Binary")
    print("5. Subtract Binary")
    print("6. Multiply Binary")
    print("7. Divide Binary")
    print("8. Modulo (เศษ)")
    print("9. Bitwise (AND/OR/XOR/NOT)")
    print("10. Text to Binary / Binary to Text")
    print("11. Fractional Base Convert (เช่น 10.75)")
    print("0. Exit")

def main():
    while True:
        display_menu()
        choice = input("\nSelect option: ")
        
        if choice == "1":
            dec = int(input("Enter decimal number: "))
            print(f"Binary: {decimal_to_binary(dec)}")
        elif choice == "2":
            binary = input("Enter binary number: ")
            print(f"Decimal: {binary_to_decimal(binary)}")
        elif choice == "3":
            src = int(input("Source base (2/8/10/16): "))
            dst = int(input("Target base (2/8/10/16): "))
            num = input("Enter number: ")
            dec = from_base(num, src)
            print(f"Result ({BASE_NAMES[dst]}): {to_base(dec, dst)}")
        elif choice == "4":
            b1 = input("Enter first binary: ")
            b2 = input("Enter second binary: ")
            print(f"Result: {add_binary(b1, b2)}")
        elif choice == "5":
            b1 = input("Enter first binary: ")
            b2 = input("Enter second binary: ")
            print(f"Result: {subtract_binary(b1, b2)}")
        elif choice == "6":
            b1 = input("Enter first binary: ")
            b2 = input("Enter second binary: ")
            print(f"Result: {multiply_binary(b1, b2)}")
        elif choice == "7":
            b1 = input("Enter first binary: ")
            b2 = input("Enter second binary: ")
            print(f"Result: {divide_binary(b1, b2)}")
        elif choice == "8":
            b1 = input("Enter first binary: ")
            b2 = input("Enter second binary: ")
            print(f"Result: {modulo_binary(b1, b2)}")
        elif choice == "9":
            op = input("Operation (and/or/xor/not): ").lower()
            b1 = input("Enter first binary: ")
            b2 = input("Enter second binary: ")
            if op == "and":
                print(f"Result: {bitwise_and(b1, b2)}")
            elif op == "or":
                print(f"Result: {bitwise_or(b1, b2)}")
            elif op == "xor":
                print(f"Result: {bitwise_xor(b1, b2)}")
            elif op == "not":
                print(f"Result: {bitwise_not(b1)}")
            else:
                print("Invalid operation!")
        elif choice == "10":
            mode = input("Mode (text2bin / bin2text): ").lower()
            if mode == "text2bin":
                text = input("Enter text: ")
                print(f"Binary: {text_to_binary(text)}")
            elif mode == "bin2text":
                binary = input("Enter binary (space separated): ")
                print(f"Text: {binary_to_text(binary)}")
            else:
                print("Invalid mode!")
        elif choice == "11":
            num = input("Enter fractional number (e.g. 10.75): ")
            src = int(input("Source base (2/8/10/16): "))
            dst = int(input("Target base (2/8/10/16): "))
            dec = base_fractional_to_decimal(num, src)
            print(f"Decimal value: {dec}")
            print(f"Result ({BASE_NAMES[dst]}): {to_base_fractional(dec, dst)}")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option!")

if __name__ == "__main__":
    main()
