# Sistem Pencatatan Nilai Mahasiswa

Program berbasis terminal yang dibuat menggunakan Python untuk membaca, menampilkan, dan menambahkan data nilai mahasiswa. Data disimpan dalam file **CSV**, sehingga dapat digunakan kembali setelah program ditutup

## Fitur

- **Menampilkan data mahasiswa** dari file `nilai.csv` menggunakan modul bawaan `csv`. Setiap data ditampilkan dengan nomor urut, nama, NIM, mata kuliah, dan nilai

  ```python
  with open(nmfilecsv) as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=",")
      for rw in csv_reader:
          datanilai.append(rw)
  ```

- **Menampilkan pesan saat data masih kosong.** Baris pertama CSV digunakan sebagai header. Jika file hanya berisi header, program memberi tahu bahwa belum ada data yang terdefinisi

  ```python
  if len(datanilai) <= 1:
      print("belum ada data yang terdefinisi")
  ```

- **Menambahkan data nilai mahasiswa** melalui input nama, NIM, mata kuliah, dan nilai

  ```python
  nama = input("Masukkan Nama : ")
  nim = input("Masukkan Nim : ")
  Matkul = input("Masukkan mata kuliah : ")
  nilai = input("Masukkan nilai (0-100) : ")
  ```

- **Memvalidasi input sebelum penyimpanan.** Nama, NIM, dan mata kuliah tidak boleh berupa string kosong. Nilai harus berupa digit dan tidak melebihi 100 `isdigit()`

  ```python
  if nama == "" or nim == "" or Matkul == "":
      print("Data Tidak boleh kosong")
  elif not nilai.isdigit():
      print("Harus berupa angka......")
  elif int(nilai) > 100:
      print("Nilai maksimal 100")
  ```

- **Menyimpan data secara permanen** menggunakan mode append (`"a"`). Data baru ditambahkan di akhir file tanpa menimpa data sebelumnya

  ```python
  with open(nmfilecsv, mode="a", newline="") as csv_file:
      writer = csv.writer(
          csv_file,
          delimiter=",",
          quotechar='"',
          quoting=csv.QUOTE_MINIMAL
      )
      writer.writerow([nama, nim, Matkul, nilai])
  ```

- **Menu interaktif** yang terus ditampilkan hingga pengguna memilih keluar. Pilihan selain `1`, `2`, atau `3` akan menghasilkan pesan bahwa pilihan tidak valid

## Menu Program

```text
===== MENU PENCATATAN NILAI MAHASISWA =====
1. Tampilkan data
2. Tambahkan data
3. Keluar
Pilih menu (1/2/3):
```

## Struktur Fungsi

| Fungsi | Tanggung jawab |
| --- | --- |
| `tMenu()` | Menampilkan pilihan menu |
| `tData()` | Membaca CSV dan menampilkan data mahasiswa |
| `Mdata()` | Menerima input, memvalidasi, dan menambahkan data ke CSV |
| `Wmain()` | Mengatur perulangan menu dan menjalankan fungsi sesuai pilihan |

## Ketentuan Data

- Setiap baris data harus memiliki empat kolom: nama, NIM, mata kuliah, dan nilai.
- Baris pertama selalu dianggap sebagai header dan tidak ditampilkan sebagai data.
- Nilai dimasukkan sebagai bilangan bulat dari `0` sampai `100`.
- Pemeriksaan nama, NIM, dan mata kuliah tidak boleh kosong
  ```python
  if nama == "" or nim == "" or Matkul == "":
        print("Data Tidak boleh kosong")
  ```

### Built With
<img src="https://skillicons.dev/icons?i=py,vscode,github" />

## Output
<img width="480" height="483" alt="Screenshot 2026-10-06 210728" src="https://github.com/user-attachments/assets/fa4727ce-8172-4afd-8a07-20fe4001f9f6" />

