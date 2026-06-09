class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMapSeparateChaining:
    def __init__(self, size=10):
        self.SIZE = size
        self.table = [None] * self.SIZE

    def hash_function(self, key):
        return (key % self.SIZE + self.SIZE) % self.SIZE

    def insert(self, key, value):
        index = self.hash_function(key)
        current = self.table[index]

        while current is not None:
            if current.key == key:
                current.value = value
                print("Data berhasil diperbarui.")
                return
            current = current.next

        new_node = Node(key, value)
        new_node.next = self.table[index]
        self.table[index] = new_node
        print("Data berhasil ditambahkan.")

    def search(self, key):
        index = self.hash_function(key)
        current = self.table[index]

        while current is not None:
            if current.key == key:
                return current
            current = current.next

        return None

    def remove_key(self, key):
        index = self.hash_function(key)
        current = self.table[index]
        prev = None

        while current is not None:
            if current.key == key:
                if prev is None:
                    self.table[index] = current.next
                else:
                    prev.next = current.next
                return True

            prev = current
            current = current.next

        return False

    def display(self):
        print("\nIsi Hash Table:")
        for i in range(self.SIZE):
            print(f"Index {i}: ", end="")
            current = self.table[i]

            while current is not None:
                print(f"[Key: {current.key}, Value: {current.value}] -> ", end="")
                current = current.next

            print("NULL")


def main():
    hashmap = HashMapSeparateChaining()

    while True:
        print("\n=== MENU HASHMAP ===")
        print("1. Insert Data")
        print("2. Hapus Data")
        print("3. Cari Data")
        print("4. Display Data")
        print("5. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            try:
                key = int(input("Masukkan key: "))
                value = input("Masukkan value: ")
                hashmap.insert(key, value)
            except ValueError:
                print("Key harus berupa angka.")

        elif pilihan == "2":
            try:
                key = int(input("Masukkan key yang ingin dihapus: "))
                if hashmap.remove_key(key):
                    print("Data berhasil dihapus.")
                else:
                    print("Data tidak ditemukan.")
            except ValueError:
                print("Key harus berupa angka.")

        elif pilihan == "3":
            try:
                key = int(input("Masukkan key yang ingin dicari: "))
                hasil = hashmap.search(key)

                if hasil is not None:
                    print(f"Data ditemukan: Key = {hasil.key}, Value = {hasil.value}")
                else:
                    print("Data tidak ditemukan.")
            except ValueError:
                print("Key harus berupa angka.")

        elif pilihan == "4":
            hashmap.display()

        elif pilihan == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()