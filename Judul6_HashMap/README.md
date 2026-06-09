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

<img width="483" height="892" alt="image" src="https://github.com/user-attachments/assets/dabf9a87-ae9e-4bd0-bf3a-5fbe89e33562" />
<img width="359" height="409" alt="image" src="https://github.com/user-attachments/assets/da5e2331-1bcc-40d5-9620-c59b0136153a" />


Penjelasan output

## Penjelasan Output Program

Saat user memilih menu `Insert Data`, program akan memasukkan data ke dalam HashMap menggunakan fungsi `insert()`. Data yang dimasukkan terdiri dari `key` sebagai angka unik penanda data dan `value` sebagai isi data yang disimpan. Pada output, user memasukkan `key = 41` dan `value = josh`, lalu program menampilkan pesan `Data berhasil ditambahkan.`, yang berarti data tersebut berhasil masuk ke dalam HashMap.

Setelah itu, user memilih menu `Display Data` untuk menampilkan isi Hash Table dari `Index 0` sampai `Index 9`. Pada tampilan tersebut, data dengan `key = 41` dan `value = josh` berada di `Index 1` karena hasil perhitungan hash adalah `41 % 10 = 1`. Selain itu, data dengan `key = 14` dan `value = wildan` berada di `Index 4` karena hasil perhitungan hash adalah `14 % 10 = 4`. Index lain yang bernilai `NULL` menunjukkan bahwa belum ada data yang tersimpan pada posisi tersebut.

Kemudian user memilih menu `Hapus Data` dan memasukkan `key = 41`. Program mencari data tersebut menggunakan key, lalu menghapusnya dari HashMap. Pesan `Data berhasil dihapus.` menunjukkan bahwa data dengan key tersebut berhasil ditemukan dan dihapus. Setelah proses hapus, data `josh` tidak lagi tersimpan di dalam HashMap.

Selanjutnya user memilih menu `Cari Data` dan memasukkan `key = 14`. Program mencari data berdasarkan key tersebut menggunakan fungsi `search()`. Output `Data ditemukan: Key = 14, Value = wildan` menunjukkan bahwa data dengan key `14` masih tersimpan di dalam HashMap dan berhasil ditemukan oleh program.

Terakhir, user memilih menu `Keluar`, lalu program menampilkan pesan `Program selesai.`. Hal ini menunjukkan bahwa program berhenti berjalan. Berdasarkan output tersebut, dapat disimpulkan bahwa fitur `insert`, `display`, `hapus`, `cari`, dan `keluar` sudah berjalan dengan baik. Program menggunakan struktur data HashMap dengan metode Separate Chaining agar proses penyimpanan, pencarian, dan penghapusan data dapat dilakukan lebih cepat berdasarkan key. Konsep ini sesuai dengan kode yang menggunakan fungsi `insert()`, `search()`, `remove_key()`, dan `display()`. :contentReference[oaicite:0]{index=0}

## E. Link YouTube
