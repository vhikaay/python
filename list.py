def hitung(angka1, angka2, operasi) :
    if operasi  == "*" :
        return angka1 * angka2
    elif operasi == "+" :
        return angka1 + angka2
    elif operasi == "-" :
        return angka1 - angka2
   
print(hitung(2, 4, "*"))
print(hitung(4, 5, "+"))
print(hitung(10, 5, "-"))