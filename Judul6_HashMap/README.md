# HashMap
## A. Judul Program
Sistem Penyimpanan Data Mahasiswa Menggunakan HashMap
## B. Deskripsi singkat
Program ini menggunakan HashMap separate chaining berfungsi untuk menyimpan, mencari, menghapus, dan menampilkan data mahasiswa berdasarkan key tertentu, misalnya NPM atau ID mahasiswa. Struktur data yang diterapkan adalah HashMap dengan metode Separate Chaining. HashMap menggunakan fungsi hash untuk menentukan posisi penyimpanan data di dalam tabel
## C. Source Code
Screenshot code

<img width="699" height="932" alt="image" src="https://github.com/user-attachments/assets/207a9ee5-2690-448f-8fee-5bee34ad26c2" />
<img width="921" height="768" alt="image" src="https://github.com/user-attachments/assets/026807ae-fa83-4e0f-82bd-b7c949cceb65" />
<img width="802" height="857" alt="image" src="https://github.com/user-attachments/assets/57a7ed61-c3ea-4423-8689-e78f2bae3a5c" />
<img width="940" height="568" alt="image" src="https://github.com/user-attachments/assets/50c87956-dce2-462b-aba7-5ab46e0a8633" />



Penjelasan code

### 1. Class `Node`

- Digunakan untuk membuat **node** pada HashMap
- `self.key` digunakan untuk menyimpan **key**, misalnya NPM atau ID mahasiswa
- `self.value` digunakan untuk menyimpan **data/value**, misalnya nama atau nilai mahasiswa
- `self.next` digunakan sebagai penghubung ke node berikutnya jika terjadi collision
- Class ini dipakai karena HashMap menggunakan metode **Separate Chaining** berbasis linked list

---

### 2. Class `HashMapSeparateChaining`

- Digunakan untuk mengelola struktur data **HashMap**
- Menyimpan data dalam bentuk tabel hash
- Mengatur proses `insert`, `search`, `remove_key`, dan `display`
- Menggunakan metode **Separate Chaining** untuk menangani data yang masuk ke index yang sama

---

### 3. Fungsi `__init__()`

- Digunakan untuk membuat tabel hash pertama kali
- `self.SIZE` digunakan untuk menentukan ukuran tabel hash
- `self.table` digunakan untuk menyimpan seluruh data dalam bentuk list
- Setiap index awalnya berisi `None` karena belum ada data yang dimasukkan

---

### 4. Fungsi `hash_function()`

- Digunakan untuk menentukan posisi index dari sebuah key
- Key akan dihitung menggunakan operasi modulo `%`
- Contohnya jika `key = 111` dan ukuran tabel `10`, maka index-nya adalah `111 % 10 = 1`
- Fungsi ini membuat data bisa langsung diarahkan ke index tertentu dalam tabel hash

---

### 5. Fungsi `insert()`

- Digunakan untuk menambahkan data baru ke dalam HashMap
- Program akan mencari index dari key menggunakan `hash_function()`
- Jika key sudah ada, maka value lama akan diperbarui
- Jika key belum ada, maka node baru akan dibuat
- Jika terjadi collision, node baru akan disambungkan ke rantai linked list pada index tersebut

---

### 6. Fungsi `search()`

- Digunakan untuk mencari data berdasarkan key
- Program akan menentukan index menggunakan `hash_function()`
- Setelah itu, pencarian dilakukan pada rantai node di index tersebut
- Jika key ditemukan, maka data akan dikembalikan
- Jika key tidak ditemukan, maka fungsi mengembalikan `None`

---

### 7. Fungsi `remove_key()`

- Digunakan untuk menghapus data berdasarkan key
- Program mencari posisi key pada index hasil hash
- Jika data berada di node pertama, maka head langsung diganti ke node berikutnya
- Jika data berada di tengah atau akhir rantai, maka node sebelumnya akan disambungkan ke node setelah data yang dihapus
- Jika key berhasil dihapus, fungsi mengembalikan `True`
- Jika key tidak ditemukan, fungsi mengembalikan `False`

---

### 8. Fungsi `display()`

- Digunakan untuk menampilkan seluruh isi HashMap
- Program menampilkan data dari index `0` sampai index terakhir
- Jika pada suatu index terdapat collision, semua node akan ditampilkan secara berurutan
- Jika index kosong, maka akan ditampilkan `NULL`
- Fungsi ini membantu melihat struktur HashMap setelah proses insert atau hapus data

---

### 9. Fungsi `main()`

- Digunakan sebagai fungsi utama untuk menjalankan program
- Berisi menu pilihan seperti insert data, hapus data, cari data, display data, dan keluar
- Input dari user diproses sesuai menu yang dipilih
- Fungsi ini membuat program menjadi interaktif karena user dapat mengelola data secara langsung lewat terminal
- Program akan terus berjalan sampai user memilih menu keluar

## D. Output code


Penjelasan code

## E. Link YouTube
