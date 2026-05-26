class Node:
    def __init__(self, score, player):
        self.score = score
        self.player = player
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, root, score, player):
        if root is None:
            return Node(score, player)

        if score < root.score:
            root.left = self.insert(root.left, score, player)
        else:
            root.right = self.insert(root.right, score, player)

        return root

    def search(self, root, score):
        if root is None:
            return None

        if root.score == score:
            return root

        if score < root.score:
            return self.search(root.left, score)

        return self.search(root.right, score)

    def leaderboard(self, root):
        if root:
            self.leaderboard(root.right)
            print(f"{root.player} : {root.score}")
            self.leaderboard(root.left)


def main():
    game = BST()

    while True:
        print("\n=== RANKING GAME BST ===")
        print("1. Tambah pemain")
        print("2. Cari skor")
        print("3. Tampilkan leaderboard")
        print("4. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            player = input("Nama pemain: ")
            score = int(input("Masukkan skor: "))

            game.root = game.insert(game.root, score, player)

            print("Data berhasil ditambahkan")

        elif pilih == "2":
            score = int(input("Masukkan skor yang dicari: "))

            result = game.search(game.root, score)

            if result:
                print(f"Pemain ditemukan: {result.player}")
            else:
                print("Skor tidak ditemukan")

        elif pilih == "3":
            print("\n=== LEADERBOARD ===")

            if game.root is None:
                print("Belum ada data")
            else:
                game.leaderboard(game.root)

        elif pilih == "4":
            print("Program selesai")
            break

        else:
            print("Menu tidak valid")


if __name__ == "__main__":
    main()