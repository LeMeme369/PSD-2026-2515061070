# SYSTEM STACK & QUEUE
## A. Judul Program
Program Antrean Pesanan
## B. Deskripsi singkat
Program ini digunakan untuk mengelola antrean pesanan pelanggan secara teratur berdasarkan urutan kedatangan. Algoritma yang diterapkan pada program ini adalah Queue (antrian) dengan metode FIFO (First In First Out), yaitu data yang pertama masuk akan menjadi data pertama yang diproses
## C. Source Code
Screenshot code

<img width="727" height="959" alt="image" src="https://github.com/user-attachments/assets/92483133-e430-4724-a92f-dc963858ae79" />
<img width="653" height="807" alt="image" src="https://github.com/user-attachments/assets/3d2449ed-3c55-4bd7-bd25-99e471155382" />
<img width="779" height="735" alt="image" src="https://github.com/user-attachments/assets/c8916bcf-ca34-41ad-b3bf-5e601e03637b" />

Penjelasan code
1. Class Node
- Digunakan untuk membuat node pada linked list
- self.data digunakan untuk menyimpan data pesanan
- self.next digunakan untuk menyimpan alamat node berikutnya
- Setiap node saling terhubung membentuk antrean
2. Class QueuePesanan
- Digunakan untuk membuat sistem antrean pesanan menggunakan struktur data queue
- Queue bekerja dengan konsep FIFO (First In First Out)
- Pesanan yang masuk pertama akan diproses pertama
3. Fungsi __init__()
- Digunakan untuk inisialisasi queue
- front_ptr = None menandakan bagian depan antrean masih kosong
- rear_ptr = None menandakan bagian belakang antrean masih kosong
4. Fungsi is_empty()
- Digunakan untuk mengecek apakah antrean kosong
- Mengembalikan nilai True jika queue kosong
- Mengembalikan nilai False jika queue memiliki data
5. Fungsi enqueue(pesanan)
- Digunakan untuk menambahkan pesanan ke dalam antrean
- new_node = Node(pesanan) membuat node baru
- Jika queue kosong:
- front_ptr dan rear_ptr akan menunjuk node baru
Jika queue tidak kosong:
- rear_ptr.next = new_node menghubungkan node terakhir dengan node baru
- rear_ptr = new_node memindahkan pointer belakang ke node baru
- Pesanan baru selalu masuk ke belakang antrean
6. Fungsi dequeue()
- Digunakan untuk memproses atau menghapus pesanan paling depan
- Jika queue kosong, program menampilkan pesan antrean kosong
- temp = self.front_ptr menyimpan data paling depan sementara
- self.front_ptr = self.front_ptr.next memindahkan antrean depan ke node berikutnya
- Jika semua data habis:
  - rear_ptr diubah menjadi None
- Proses ini mengikuti konsep FIFO
7. Fungsi peek()
- Digunakan untuk melihat pesanan paling depan
- Tidak menghapus data dari antrean
- self.front_ptr.data mengambil data pesanan terdepan
8. Fungsi display()
- Digunakan untuk menampilkan seluruh antrean pesanan
- current = self.front_ptr memulai traversal dari node depan
- Perulangan while current is not None digunakan untuk menampilkan semua node
- current = current.next berpindah ke node berikutnya
- Nomor antrean ditampilkan menggunakan variabel nomor
9. Fungsi main()
- Digunakan untuk mengatur jalannya program
- queue = QueuePesanan() membuat objek queue
- Variabel pilih digunakan untuk menyimpan pilihan menu user
- Perulangan while digunakan agar program terus berjalan sampai user memilih keluar
## D. Output code
<img width="552" height="875" alt="image" src="https://github.com/user-attachments/assets/037158a6-74b8-460d-b5b9-c1fc2aa432db" />
<img width="561" height="940" alt="image" src="https://github.com/user-attachments/assets/6a634745-704b-4751-9c24-4a78d96b4eb7" />

Penjelasan Output
- Saat user memilih menu tambah pesanan, program memasukkan data pesanan ke dalam antrean menggunakan fungsi enqueue()
- Setiap pesanan baru disimpan pada bagian belakang queue sesuai urutan input pelanggan
- Saat user memilih lihat pesanan berikutnya, program menampilkan pesanan paling depan menggunakan fungsi peek()
- Saat user memilih tampilkan antrean, program menampilkan seluruh daftar pesanan dari depan hingga belakang menggunakan traversal linked list
- Saat proses pesanan dijalankan, program mengambil dan menghapus pesanan paling depan menggunakan fungsi dequeue()
- Program menggunakan struktur data Queue dengan metode FIFO (First In First Out), sehingga pesanan yang pertama masuk akan diproses pertama
- Linked List digunakan agar proses penambahan dan peng
## E. Link YouTube
