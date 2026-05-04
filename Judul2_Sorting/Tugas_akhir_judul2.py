def tukar(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def bubble_sort(arr, n):
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j].lower() > arr[j + 1].lower():
                tukar(arr, j, j + 1)


def main():
    try:
        n = int(input("Masukkan jumlah mahasiswa: "))
    except ValueError:
        print("Input tidak valid!")
        return

    arr = []
    print("Masukkan nama mahasiswa:")
    for i in range(n):
        while True:
            nama = input(f"Nama mahasiswa ke-{i+1}: ").strip()
            if nama == "":
                print("Nama tidak boleh kosong!")
            else:
                arr.append(nama)
                break

    print("\nData sebelum diurutkan:")
    print(arr)

    bubble_sort(arr, n)

    print("\nData setelah diurutkan (A-Z):")
    for nama in arr:
        print(nama)


if __name__ == "__main__":
    main()