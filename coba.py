umur = int(input("masukkan umur anda: "))
if umur < 5:
    print("Balita")
elif umur < 10:
    print("Anak-Anak")
elif umur < 15:
    print("Remaja")
elif umur < 28:
    print("Dewasa")
else:
    print("Lansia")