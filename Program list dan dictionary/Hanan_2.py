# Latihan 2
list_global = []
setelah_diskon = {}
total = 0
while True:
    print('1. Input barang')
    print('2. Harga setelah diskon')
    print('3. Daftar barang setelah diskon')
    print('4. Total harga')
    print('5. Keluar')

    pilih = int(input('pilih menu: '))
    if pilih == 1:
        barang = input('Masukkan barang: ')
        harga = int(input('masukkan harga barang: '))
        diskon = int(input('masukkan diskon: '))
        list_global.append([barang, harga, diskon])
        print(f'barang {barang} seharga {harga} dengan diskon {diskon} berhasil di-input')
    elif pilih == 2:
        x = input('masukkan nama barang: ')
        for i in list_global:
            if i[0] == x:
                harga_diskon = i[1] * i[2] / 100
                total += harga_diskon
                setelah_diskon[x] = harga_diskon
                print(f'barang {x} setelah diskon menjadi {harga_diskon}')
            else:
                print('nama barang tidak tersedia')
    elif pilih == 3:
        print('Harga setelah diskon: ',setelah_diskon)
    elif pilih == 4:
        print('Total harga setelah diskon: Rp',total)
    else:
        print('keluar dari program')
        break