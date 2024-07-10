from Soal_3_Main import AntrianRestoran

def main():
    antrian_restoran = AntrianRestoran()

    while True:
        print("\n1. Tambah pesanan ke antrian")
        print("2. Hapus pesanan dari antrian")
        print("3. Tampilkan antrian saat ini")
        print("4. Keluar")

        pilihan = input("Masukkan pilihan Anda: ")

        if pilihan == '1':
            pesanan = input("Masukkan pesanan: ")
            antrian_restoran.enqueue(pesanan)
        elif pilihan == '2':
            antrian_restoran.dequeue()
        elif pilihan == '3':
            antrian_restoran.tampilkan_antrian()
        elif pilihan == '4':
            print("Keluar dari program.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()