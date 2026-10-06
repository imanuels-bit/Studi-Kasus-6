import csv
nmfilecsv = "nilai.csv"
def tMenu():
    print("===== MENU PENCATATAN NILAI MAHASISWA =====")
    print("1. Tampilkan data")
    print("2. Tambahkan data")
    print("3. Keluar")
 
def tData():
    print("=== Data Mahasiswa ===")
    datanilai = []
    with open(nmfilecsv) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        for rw in csv_reader:
            datanilai.append(rw)
 
    if len(datanilai) <= 1:
        print("belum ada data yang terdefinisi")
    else:
        Wnomor = 1
        for rw in datanilai[1:]:
            print(f"{Wnomor} | {rw[0]} | {rw[1]} | {rw[2]} | {rw[3]}")
            Wnomor = Wnomor + 1
 
def Mdata():
    print("=== Masukkan data ===")
    nama = input("Masukkan Nama : ")
    nim = input("Masukkan Nim : ")
    Matkul = input("Masukkan mata kuliah : ")
    nilai = input("Masukkan nilai (0-100) : ")
 
    if nama == "" or nim == "" or Matkul == "":
        print("Data Tidak boleh kosong")
    elif not nilai.isdigit():
        print("Harus berupa angka......")
    elif int(nilai) > 100:
        print("Nilai maksimal 100")
    else:
        with open(nmfilecsv, mode="a", newline="") as csv_file:
            writer = csv.writer(csv_file, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerow([nama, nim, Matkul, nilai])
        print("Data nilai berhasil ditambahkan dan disimpan..")
 
 
def Wmain():
    while True:
        print()
        tMenu()
        pilihan = input("Pilih menu (1/2/3): ")
 
        if pilihan == "1":
            tData()
        elif pilihan == "2":
            Mdata()
        elif pilihan == "3":
            print("Terima kasih, program selesai...")
            break
        else:
            print("Pilihan tidak valid, coba lagi")
Wmain()