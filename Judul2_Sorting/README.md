# SYSTEM SORTING
## A. Judul Program
Sytem sorting absen mahasiswa berdasarkan nama
## B. Deskripsi singkat
Program ini berfungsi untuk mengurutkan nama mahasiswa berdasarkan urutan alfabet nama dari A-Z. Untuk algoritma yang digunakan adalah bubble sort yaitu metode pengurutan sederhana dimana elemen dibandingkan dengan elemen selanjutnya dan jika urutannya salah maka akan ditukar.
## C. Source code
Screenshot Source code

<img width="818" height="338" alt="image" src="https://github.com/user-attachments/assets/bef70200-88a9-4de5-939f-8e634e6d27f4" />
<img width="966" height="777" alt="image" src="https://github.com/user-attachments/assets/6e32be18-8036-4a10-8627-885266e6d222" />

Penjelasan kode
1. Fungsi tukar(arr, i, j)
- Digunakan untuk menukar dua elemen dalam list
- Menyimpan sementara nilai arr[i] ke variabel temp
- Mengganti arr[i] dengan arr[j]
- Mengisi arr[j] dengan nilai dari temp
2. Fungsi bubble_sort(arr, n)
- Berfungsi untuk mengurutkan data menggunakan algoritma Bubble Sort
- Menggunakan dua perulangan (nested loop)
- Loop luar (i) untuk mengontrol jumlah iterasi
- Loop dalam (j) untuk membandingkan elemen yang bersebelahan
- Membandingkan arr[j] dan arr[j+1] secara alfabet
- Menggunakan .lower() agar tidak sensitif huruf besar/kecil
- Jika urutan salah, maka elemen ditukar menggunakan fungsi tukar
- Setiap iterasi akan menempatkan elemen terbesar ke posisi akhir
3. Fungsi main()
- Mengatur jalannya program
- Meminta input jumlah data dari pengguna
- Menggunakan try-except untuk menangani input yang tidak valid
- Membuat list kosong untuk menyimpan data
- Melakukan input nama mahasiswa sebanyak n kali
- Menggunakan validasi agar input tidak kosong
- Menampilkan data sebelum diurutkan
- Memanggil fungsi bubble_sort untuk mengurutkan data
- Menampilkan hasil data setelah diurutkan
4. Bagian eksekusi program
if __name__ == "__main__":
- Memastikan fungsi main() dijalankan hanya saat file dieksekusi langsung
- Mencegah kode otomatis berjalan saat diimpor sebagai modul

## D. Output Program
<img width="670" height="379" alt="image" src="https://github.com/user-attachments/assets/d542582e-90bd-44be-8e49-1c52de5824fa" />

Penjelasan
- Saat user menginput jumlah data, program menentukan berapa banyak nama mahasiswa yang akan dimasukkan ke dalam list
- Saat user memasukkan nama mahasiswa, setiap nama disimpan ke dalam list sesuai urutan input
- Saat proses sorting dijalankan, program membandingkan elemen yang bersebelahan dan menukarnya jika urutannya salah hingga tersusun alfabetis
- Saat hasil ditampilkan, program menampilkan seluruh data yang sudah terurut dari A–Z dengan perbandingan yang tidak membedakan huruf besar dan kecil

## E. Link YouTube
