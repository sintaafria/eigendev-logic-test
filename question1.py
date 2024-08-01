# Terdapat string "NEGIE1", silahkan reverse alphabet nya dengan angka tetap diakhir kata Hasil = "EIGEN1"

def reverse_string(input_char):
    string_char = ""
    number_car = ""

    for char in input_char:
        if(char.isdigit()): number_car += char
        else: string_char = char+string_char

    return string_char + number_car

output = reverse_string("NEGIE1")
print(output)
