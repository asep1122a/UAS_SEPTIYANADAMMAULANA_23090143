nilai_mahasiswa = [
    ["Mahasiswa 1", "Algoritma dan Struktur Data 2", 90, "Matematika Diskrit", 80],
    ["Mahasiswa 2", "Algoritma dan Struktur Data 2", 50, "Matematika Diskrit", 60],
    ["Mahasiswa 3", "Algoritma dan Struktur Data 2", 65, "Matematika Diskrit", 70]
]

def hitung_rata_rata(nilai):
    return sum(nilai) / len(nilai)

mata_kuliah = ["Algoritma dan Struktur Data 2", "Matematika Diskrit"]
nilai_rata_rata_mata_kuliah = {}
for mk in mata_kuliah:
    nilai_mk = []
    for nilai in nilai_mahasiswa:
        if nilai[1] == mk:
            nilai_mk.append(nilai[2])
        elif nilai[3] == mk:
            nilai_mk.append(nilai[4])
    nilai_rata_rata_mata_kuliah[mk] = hitung_rata_rata(nilai_mk)

print("\nNilai Rata-Rata Setiap Mata Kuliah:")
for mk, nilai in nilai_rata_rata_mata_kuliah.items():
    print(f"{mk}: {nilai:.2f}")

nilai_rata_rata_mahasiswa = {}
for nilai in nilai_mahasiswa:
    nama_mahasiswa = nilai[0]
    nilai_mk = [nilai[2], nilai[4]]
    nilai_rata_rata_mahasiswa[nama_mahasiswa] = hitung_rata_rata(nilai_mk)

print("\nNilai Rata-Rata Setiap Mahasiswa:")
for nama, nilai in nilai_rata_rata_mahasiswa.items():
    print(f"{nama}: {nilai:.2f}")