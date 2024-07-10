def input_data_mahasiswa():
    data_mahasiswa = []

    while True:
        nim = input("Masukan NIM: ")
        nama = input("Masukan Nama: ")
        data_mahasiswa.append({"NIM": nim, "Nama": nama})
        
        lagi = input("Ingin tambah lagi? (YA/TIDAK): ").lower()
        if lagi != 'ya':
            break

    print("\nData Mahasiswa:")
    for mahasiswa in data_mahasiswa:
        print(f"NIM: {mahasiswa['NIM']}, Nama: {mahasiswa['Nama']}")

if __name__ == "__main__":
    input_data_mahasiswa()