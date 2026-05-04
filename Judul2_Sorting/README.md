# SYSTEM SORTING
## A. Judul Program
Sytem sorting absen mahasiswa berdasarkan nama
## B. Deskripsi singkat
Program ini berfungsi untuk mengurutkan nama mahasiswa berdasarkan urutan alfabet nama dari A-Z. Untuk algoritma yang digunakan adalah bubble sort yaitu metode pengurutan sederhana dimana elemen dibandingkan dengan elemen selanjutnya dan jika urutannya salah maka akan ditukar.
## C. Source code
Screenshot Source code

<img width="815" height="349" alt="image" src="https://github.com/user-attachments/assets/19bfb9a3-654d-4d9e-9aee-2bc5f565e4ba" />
<img width="818" height="733" alt="image" src="https://github.com/user-attachments/assets/3c66d857-5d55-4408-bcc5-3dc8ce389377" />

Penjelasan kode
1. tukar(arr, i, j)
Fungsi ini bertugas menukar posisi dua elemen dalam list berdasarkan indeks.
Menggunakan teknik Pythonic:
- arr[i], arr[j] = arr[j], arr[i]
- Artinya nilai di indeks i dan j langsung ditukar tanpa variabel sementara.
Makna:
Operasi dasar yang dipakai oleh algoritma sorting untuk memperbaiki urutan data.

2. bubble_sort(arr)
inti algoritma : 
- n = len(arr) → menentukan jumlah data
- Loop luar (for i in range(n - 1)) → jumlah iterasi maksimal
- Loop dalam (for j in range(n - i - 1)) → membandingkan elemen bersebelahan

Bagian penting:

- arr[j].lower() > arr[j + 1].lower()
- Membandingkan dua string secara alfabet tanpa memperhatikan huruf besar/kecil
- Jika kondisi benar → dipanggil tukar()
- Variabel swapped:
    - Jika tidak ada pertukaran dalam satu iterasi → berarti data sudah terurut
    - Loop langsung berhenti (break)

Makna:
Setiap iterasi akan “mendorong” elemen terbesar ke posisi paling kanan.
Optimasi swapped menghindari iterasi yang tidak perlu.

3. input_data()
Fungsi untuk mengambil input dari pengguna.
Validasi jumlah data menggunakan try-except
Jika input bukan angka → program dihentikan

Loop input:
- User memasukkan data satu per satu
- Dicek apakah kosong (nilai.strip() == "")
- Jika valid → disimpan ke list
Makna:
Menjamin data yang diproses tidak kosong dan sesuai jumlah yang diminta.

4. tampilkan(arr)
Fungsi sederhana untuk menampilkan isi list:
- Menggunakan loop for
- Dicetak dalam satu baris
Makna:
Memisahkan logika output dari proses utama → membuat kode lebih modular.

5. main()
Pengatur alur utama program:
- Ambil data dari input_data()
- Jika kosong → hentikan program
- Tampilkan data sebelum sorting
- Jalankan bubble_sort()
- Tampilkan hasil setelah sorting

Makna:
Menggabungkan semua fungsi menjadi satu alur eksekusi yang jelas.

6.if __name__ == "__main__":
    main()
Digunakan untuk memastikan:
main() hanya dijalankan saat file dieksekusi langsung
Tidak dijalankan jika file di-import ke program lain

## D. Output Program
<img width="444" height="316" alt="image" src="https://github.com/user-attachments/assets/988c392f-3971-4c7c-9b7c-25ea254c329c" />

Penjelasan
- saat user menginput jumlah data, program akan menentukan berapa banyak nama yang akan dimasukkan ke dalam list
- saat user memasukkan nama mahasiswa, data akan disimpan ke dalam list secara berurutan sesuai input
- saat proses sorting dijalankan, program akan membandingkan setiap elemen dan menukarnya hingga urut secara alfabet
- saat hasil ditampilkan, program akan menampilkan semua data yang sudah terurut dari A–Z tanpa membedakan huruf besar dan kecil

## E. Link YouTube
