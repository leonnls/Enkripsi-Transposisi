def enkripsi(text, key):
    kolom = len(key)
    baris = len(text) // kolom
    if len(text) % kolom != 0:
        baris += 1

    matriks = [[' ' for _ in range(kolom)] for _ in range(baris)]
    index = 0

    for i in range(baris):
        for j in range(kolom):
            if index < len(text):
                matriks[i][j] = text[index]
                index += 1

    hasil = ''
    for k in key:
        kolom_indeks = int(k) - 1
        for i in range(baris):
            hasil += matriks[i][kolom_indeks]

    return hasil

def deskripsi(ciphertext, key):
    kolom = len(key)
    baris = len(ciphertext) // kolom

    matriks = [[' ' for _ in range(kolom)] for _ in range(baris)]
    index = 0

    for k in key:
        kolom_indeks = int(k) - 1
        for i in range(baris):
            matriks[i][kolom_indeks] = ciphertext[index]
            index += 1

    hasil = ''
    for i in range(baris):
        hasil += ''.join(matriks[i])

    return hasil

while True:
    print("1. Enkripsi")
    print("2. Deskripsi")
    print("3. Leave")
    pilihan = input("Pilih opsi: ")

    if pilihan == '1':
        plaintext = input("Masukkan teks yang ingin dienkripsi: ")
        key = input("Masukkan kunci enkripsi (urutan kolom tanpa spasi): ")
        ciphertext = enkripsi(plaintext, key)
        print("Teks terenkripsi: " + ciphertext)
    elif pilihan == '2':
        ciphertext = input("Masukkan teks yang ingin didekripsi: ")
        key = input("Masukkan kunci enkripsi (urutan kolom tanpa spasi): ")
        plaintext = deskripsi(ciphertext, key)
        print("Teks terdekripsi: " + plaintext)
    elif pilihan == '3':
        break
    else:
        print("Opsi tidak valid. Silakan pilih opsi 1, 2, atau 3.")
