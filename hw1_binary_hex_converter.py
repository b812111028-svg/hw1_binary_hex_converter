import tkinter as tk
hex_digits = "0123456789ABCDEF"

def decimal_to_binary(n):
    if n == 0:
        return "0"
    result = ""

    while n > 0:
        remainder = n % 2
        result = str(remainder) + result
        n = n // 2

    return result


def decimal_to_hexadecimal(n):
    if n == 0:
        return "0"
    result = ""

    while n > 0:
        remainder = n % 16
        result = hex_digits[remainder] + result
        n = n // 16

    return result


def binary_to_decimal(s):
    result = 0
    for ch in s:
        if ch not in ['0', '1']:
            raise ValueError("Invalid binary input")

        bit = 1 if ch == '1' else 0
        result = result * 2 + bit

    return result


def binary_to_hexadecimal(s):
    for ch in s:
        if ch not in ['0', '1']:
            raise ValueError("Invalid binary input")
        
    while len(s) % 4 != 0:
        s = "0" + s

    result = ""

    for i in range(0, len(s), 4):
        group = s[i:i+4]

        value = 0
        for ch in group:
            bit = 1 if ch == '1' else 0
            value = value * 2 + bit

        result = result + hex_digits[value]

    return result.lstrip("0") or "0"   


def hexadecimal_to_decimal(s):
    result = 0
    for ch in s:
        ch = ch.upper()
        found = False
        
        for i in range(len(hex_digits)):
            if hex_digits[i] == ch:
                digit = i
                found = True
                break

        if not found:
            raise ValueError("Invalid hex input")

        result = result * 16 + digit

    return result


def hexadecimal_to_binary(s):
    result = ""
    for ch in s:
        ch = ch.upper()
        found = False
    
        for i in range(len(hex_digits)):
            if hex_digits[i] == ch:
                digit = i
                found = True
                break

        if not found:
            raise ValueError("Invalid hex input")
            
        bits = ""
        temp = digit

        for i in range(4):
            remainder = temp % 2
            bits = str(remainder) + bits
            temp = temp // 2

        result = result + bits

    return result.lstrip("0") or "0" 


def clear_all():
    entry_binary.delete(0, tk.END)
    entry_decimal.delete(0, tk.END)
    entry_hexadecimal.delete(0, tk.END)
    status_label.config(text="")


def convert():
    binary_value = entry_binary.get().strip()
    decimal_value = entry_decimal.get().strip()
    hexadecimal_value = entry_hexadecimal.get().strip()

    filled_count = 0
    if binary_value != "":
        filled_count += 1
    if decimal_value != "":
        filled_count += 1
    if hexadecimal_value != "":
        filled_count += 1

    if filled_count == 0:
        status_label.config(text="Enter one value.")
        return

    if filled_count > 1:
        status_label.config(text="Just fill in one box.")
        return

    try:
        if binary_value != "":
            dec = binary_to_decimal(binary_value)
            hexa = binary_to_hexadecimal(binary_value)

            entry_decimal.delete(0, tk.END)
            entry_decimal.insert(0, str(dec))

            entry_hexadecimal.delete(0, tk.END)
            entry_hexadecimal.insert(0, hexa)

            status_label.config(text="Converted from Binary.")

        elif decimal_value != "":
            dec = int(decimal_value)
            binary = decimal_to_binary(dec)
            hexa = decimal_to_hexadecimal(dec)

            entry_binary.delete(0, tk.END)
            entry_binary.insert(0, binary)

            entry_hexadecimal.delete(0, tk.END)
            entry_hexadecimal.insert(0, hexa)

            status_label.config(text="Converted from Decimal.")

        elif hexadecimal_value != "":
            dec = hexadecimal_to_decimal(hexadecimal_value)
            binary = hexadecimal_to_binary(hexadecimal_value)

            entry_decimal.delete(0, tk.END)
            entry_decimal.insert(0, str(dec))

            entry_binary.delete(0, tk.END)
            entry_binary.insert(0, binary)

            entry_hexadecimal.delete(0, tk.END)
            entry_hexadecimal.insert(0, hexadecimal_value.upper())

            status_label.config(text="Converted from Hexadecimal.")

    except ValueError as error:
        status_label.config(text="Error: " + str(error))


window = tk.Tk()
window.title('Binary / Decimal / Hex Converter')
window.geometry('960x480')
window.resizable(False, False)

title_frame = tk.Frame(window)
title_frame.pack(pady=20)

label_binary = tk.Label(title_frame, text="Binary", font=("Arial", 14))
label_binary.grid(row=0, column=0, padx=35)

label_decimal = tk.Label(title_frame, text="Decimal", font=("Arial", 14))
label_decimal.grid(row=0, column=1, padx=35)

label_hexadecimal = tk.Label(title_frame, text="Hexadecimal", font=("Arial", 14))
label_hexadecimal.grid(row=0, column=2, padx=35)

entry_binary = tk.Entry(title_frame, width=22, font=("Arial", 14), justify="left")
entry_binary.grid(row=1, column=0, padx=8, pady=15)

entry_decimal = tk.Entry(title_frame, width=22, font=("Arial", 14), justify="left")
entry_decimal.grid(row=1, column=1, padx=8, pady=15)

entry_hexadecimal = tk.Entry(title_frame, width=22, font=("Arial", 14), justify="left")
entry_hexadecimal.grid(row=1, column=2, padx=8, pady=15)

button_convert = tk.Button(window, text="Convert", font=("Arial", 16), width=52, command=convert)
button_convert.pack(pady=12)

button_clear = tk.Button(window, text="Clear", font=("Arial", 16), width=52, command=clear_all)
button_clear.pack(pady=12)

status_label = tk.Label(window, text="", font=("Arial", 11), fg="red")
status_label.pack(pady=20)

window.mainloop()



#test
#dec_num = int(input())
#binary_str = str(input())
#hexadecimal_str = str(input())
#print(decimal_to_binary(dec_num))
#print(decimal_to_hexadecimal(dec_num))
#print(binary_to_decimal(binary_str))
#print(binary_to_hexadecimal(binary_str))
#print(hexadecimal_to_decimal(hexadecimal_str))
#print(hexadecimal_to_binary(hexadecimal_str))