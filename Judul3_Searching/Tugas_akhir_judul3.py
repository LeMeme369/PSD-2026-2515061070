def sequential_search(data, nama_cari):
    i = 0

    while i < len(data):
        if data[i]["nama"].lower() == nama_cari.lower():
            return data[i]
        i += 1

    return None


def main():
    data = []

    jumlah = int(input("Masukkan jumlah mahasiswa: "))

    for i in range(jumlah):
        print(f"\nData Mahasiswa ke-{i+1}")

        nama = input("Masukkan nama  : ")
        nilai = int(input("Masukkan nilai : "))

        mahasiswa = {
            "nama": nama,
            "nilai": nilai
        }

        data.append(mahasiswa)

    print("\n=== Data Mahasiswa ===")
    
    for mahasiswa in data:
        print(f"Nama: {mahasiswa['nama']}")

    nama_cari = input("\nMasukkan nama mahasiswa yang ingin dicari: ")

    hasil = sequential_search(data, nama_cari)

    if hasil is not None:
        print(f"\nMahasiswa {hasil['nama']} ditemukan.")
        print(f"Nilainya adalah {hasil['nilai']}")
    else:
        print(f"\nMahasiswa dengan nama {nama_cari} tidak ditemukan.")


if __name__ == "__main__":
    main()