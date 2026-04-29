def menu():  
    print("\n=== TO DO LIST ===")
    print("1. Tambah Tugas")
    print("2. Lihat Tugas")
    print("3. Hapus Tugas")
    print("4. Keluar")

def main():
    tugas = []
    running = True
    while running:
        menu()
        pilih = input("Pilih menu: ")

        if pilih == "1":
            t = input("Masukkan tugas: ")
            tugas.append(t)

        elif pilih == "2":
            for i, t in enumerate(tugas):
                print(f"{i+1}. {t}")

        elif pilih == "3":
            nomor = int(input("Hapus nomor: ")) - 1
            if 0 <= nomor < len(tugas):
                tugas.pop(nomor)
            else:
                print("Nomor tidak valid")

        elif pilih == "4":
            break

        else:
            print("Pilihan tidak ada")

if __name__ == "__main__":
    main()
