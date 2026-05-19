class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class QueuePesanan:
    def __init__(self):
        self.front_ptr = None
        self.rear_ptr = None

    def is_empty(self):
        return self.front_ptr is None

    def enqueue(self, pesanan):
        new_node = Node(pesanan)

        if self.is_empty():
            self.front_ptr = new_node
            self.rear_ptr = new_node
        else:
            self.rear_ptr.next = new_node
            self.rear_ptr = new_node

        print(f"Pesanan '{pesanan}' berhasil ditambahkan")

    def dequeue(self):
        if self.is_empty():
            print("Antrean pesanan kosong")
            return

        temp = self.front_ptr
        print(f"Pesanan '{temp.data}' sedang diproses")

        self.front_ptr = self.front_ptr.next

        if self.front_ptr is None:
            self.rear_ptr = None

    def peek(self):
        if self.is_empty():
            print("Antrean pesanan kosong")
            return

        print(f"Pesanan berikutnya: {self.front_ptr.data}")

    def display(self):
        if self.is_empty():
            print("Antrean pesanan kosong")
            return

        print("\nDaftar Antrean Pesanan:")
        current = self.front_ptr
        nomor = 1

        while current is not None:
            print(f"{nomor}. {current.data}")
            current = current.next
            nomor += 1


def main():
    queue = QueuePesanan()
    pilih = 0

    while pilih != 5:
        print("\n=== SISTEM ANTREAN PESANAN ===")
        print("1. Tambah Pesanan")
        print("2. Proses Pesanan")
        print("3. Lihat Pesanan Berikutnya")
        print("4. Tampilkan Antrean")
        print("5. Keluar")

        try:
            pilih = int(input("Pilih menu: "))
        except ValueError:
            print("Input harus angka!")
            continue

        if pilih == 1:
            pesanan = input("Masukkan nama pesanan: ")
            queue.enqueue(pesanan)

        elif pilih == 2:
            queue.dequeue()

        elif pilih == 3:
            queue.peek()

        elif pilih == 4:
            queue.display()

        elif pilih == 5:
            print("Program selesai")

        else:
            print("Pilihan tidak valid!")


if __name__ == "__main__":
    main()