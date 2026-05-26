# Binary Search Tree
## A. Judul Program
Sistem Ranking Game
## B. Deskripsi singkat
Program ini berfungsi untuk mengelola data skor pemain dalam sebuah permainan secara terstruktur dan efisien, Algoritma struktur data yang diterapkan pada program ini adalah Binary Search Tree. BST merupakan struktur data berbentuk pohon biner yang memiliki aturan bahwa nilai pada subtree kiri lebih kecil dari root, sedangkan subtree kanan lebih besar dari root
## C. Source Code
Screenshot code

<img width="822" height="842" alt="image" src="https://github.com/user-attachments/assets/41ad5f80-09e5-4953-9f17-33b30c6960d8" />
<img width="787" height="765" alt="image" src="https://github.com/user-attachments/assets/377d2d38-898a-4693-afe6-82c73a7eb20b" />
<img width="776" height="602" alt="image" src="https://github.com/user-attachments/assets/4382713d-2e01-4f32-917e-3ef1c4b166b1" />


Penjelasan code
1. Class Node

- Digunakan untuk membuat node pada BST
- `self.score` digunakan untuk menyimpan skor pemain
- `self.player` digunakan untuk menyimpan nama pemain
- `self.left` digunakan untuk child kiri
- `self.right` digunakan untuk child kanan

---

2. Class BST

- Digunakan untuk mengelola struktur Binary Search Tree
- Menyimpan seluruh data pemain dalam bentuk tree
- Mengatur proses insert, search, dan traversal

---

3. Fungsi `insert()`

- Digunakan untuk menambahkan data pemain ke BST
- Jika skor lebih kecil maka masuk ke kiri
- Jika skor lebih besar maka masuk ke kanan
- Menggunakan konsep rekursif

---

4. Fungsi search()
- Digunakan untuk mencari skor pemain
- Pencarian dimulai dari root
- Bergerak ke kiri atau kanan sesuai nilai skor

---

5. Fungsi leaderboard()
- Digunakan untuk menampilkan ranking pemain
- Menggunakan traversal:
    right → root → left
- Traversal tersebut menghasilkan urutan skor terbesar ke terkecil

---

6. Fungsi main()
- Digunakan sebagai program utama
- Berisi menu interaktif pengguna
- Mengatur seluruh proses input dan output

## D. Output code

<img width="644" height="648" alt="image" src="https://github.com/user-attachments/assets/fa4e36fa-6aa0-4e71-ab2b-2d34d4f32a7b" />

Penjelasan code
- Saat user memilih menu tambah pemain, program memasukkan data pemain dan skor ke dalam Binary Search Tree menggunakan fungsi `insert()`

- Data skor disimpan sesuai aturan BST:
  - skor lebih kecil masuk ke subtree kiri
  - skor lebih besar masuk ke subtree kanan

- Saat user memilih tampilkan leaderboard, program menampilkan seluruh ranking pemain menggunakan traversal:

```text
right → root → left
```
- Traversal tersebut membuat skor terbesar tampil lebih dulu sehingga sesuai untuk sistem ranking game
- Saat user memilih cari skor, program mencari data mulai dari root BST menggunakan fungsi search()
- Jika skor ditemukan, program menampilkan nama pemain yang memiliki skor tersebut
- Pada output:
`wildan : 100`
menunjukkan bahwa data pemain berhasil disimpan pada BST dan tampil pada leaderboard

Saat pencarian skor:
`Masukkan skor yang dicari: 100`
`Pemain ditemukan: wildan`
program berhasil menemukan node dengan skor `100` pada BST

- Program menggunakan struktur data Binary Search Tree (BST) sehingga proses insert dan search dapat dilakukan lebih cepat dibandingkan list biasa
- BST digunakan agar data ranking tersusun otomatis tanpa perlu melakukan sorting ulang setiap kali data baru ditambahkan

## E. Link YouTube

