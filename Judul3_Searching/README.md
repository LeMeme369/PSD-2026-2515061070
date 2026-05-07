# SYSTEM SEARCHING
## A. Judul Program
Program mencari nilai mahasiswa dalam list
## B. Deskripsi singkat
Program ini digunakan untuk menyimpan data mahasiswa berupa nama dan nilai, kemudian melakukan pencarian data berdasarkan nama yang diinput oleh pengguna, Algoritma yang digunakan pada program ini adalah Sequential Search (Linear Search). Algoritma ini bekerja dengan cara memeriksa data satu per satu secara berurutan mulai dari elemen pertama hingga elemen terakhir sampai data yang dicari ditemukan
## C. Source Code
Screenshot Code
<img width="667" height="294" alt="image" src="https://github.com/user-attachments/assets/036750a8-ee3d-4630-953c-123264dd64b7" />
<img width="1008" height="928" alt="image" src="https://github.com/user-attachments/assets/d27ded82-9472-4793-bc8e-92f6bf843b95" />

Penjelasan code
1. Fungsi sequential_search(data, nama_cari)
- Digunakan untuk mencari nama mahasiswa pada list data
- Variabel i digunakan sebagai index awal pencarian
- Menggunakan perulangan while untuk mengecek data satu per satu
- Kondisi i < len(data) memastikan perulangan berjalan selama data masih ada
- data[i]["nama"] mengambil nama mahasiswa pada index tertentu
- .lower() digunakan agar pencarian tidak membedakan huruf besar dan kecil
- Jika nama ditemukan, fungsi mengembalikan data mahasiswa tersebut dengan return data[i]
- i += 1 digunakan untuk berpindah ke data berikutnya
- Jika data tidak ditemukan, fungsi mengembalikan None
2. Fungsi main()
- Digunakan untuk mengatur jalannya program
- data = [] membuat list kosong untuk menyimpan data mahasiswa
- jumlah = int(input(...)) meminta jumlah mahasiswa yang akan dimasukkan
- Perulangan for digunakan untuk input data sebanyak jumlah yang ditentukan
- nama = input(...) digunakan untuk input nama mahasiswa
- nilai = int(input(...)) digunakan untuk input nilai mahasiswa
- data.append(mahasiswa) digunakan untuk menambahkan data ke list
- Perulangan for mahasiswa in data digunakan untuk menampilkan seluruh data mahasiswa
- nama_cari = input(...) meminta nama mahasiswa yang ingin dicari
- hasil = sequential_search(data, nama_cari) memanggil fungsi pencarian
- if hasil is not None mengecek apakah data ditemukan
- Jika ditemukan, program menampilkan nama dan nilai mahasiswa
- Jika tidak ditemukan, program menampilkan pesan bahwa data tidak ada
3. Bagian if __name__ == "__main__":
- Digunakan agar fungsi main() dijalankan saat program dieksekusi langsung
- Mencegah kode otomatis berjalan jika file diimport sebagai modul

## D. Output code
<img width="599" height="645" alt="image" src="https://github.com/user-attachments/assets/b3a6cea8-0228-42aa-abee-569d6d6937a4" />

Penjelasan
- Saat user menginput jumlah mahasiswa, program menentukan berapa banyak data mahasiswa yang akan dimasukkan ke dalam list
- Saat user memasukkan nama dan nilai mahasiswa, setiap data disimpan ke dalam list dalam bentuk dictionary sesuai urutan input
- Saat proses pencarian dijalankan, program memeriksa data mahasiswa satu per satu dari index awal hingga akhir menggunakan algoritma Sequential Search
- Program membandingkan nama mahasiswa pada data dengan nama yang dicari tanpa membedakan huruf besar dan kecil menggunakan .lower()
- Jika nama mahasiswa ditemukan, program menampilkan nama dan nilai mahasiswa tersebut
- Jika nama mahasiswa tidak ditemukan, program menampilkan pesan bahwa data mahasiswa tidak ada dalam list
## E. Link YouTube
https://youtu.be/9hPhnP3_sNE
