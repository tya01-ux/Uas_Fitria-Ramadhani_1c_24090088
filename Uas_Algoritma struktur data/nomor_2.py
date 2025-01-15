# Data nilai mahasiswa
nilai_mahasiswa = [
    [90, 80],  # Mahasiswa 1
    [50, 60],  # Mahasiswa 2
    [65, 70]   # Mahasiswa 3
]

# Nama mahasiswa
nama_mahasiswa = ["Mahasiswa 1", "Mahasiswa 2", "Mahasiswa 3"]

# Nama mata kuliah
nama_mata_kuliah = ["Algoritma", "Matematika"]

# Menampilkan tabel nilai mahasiswa
print("Nilai Mahasiswa:")
for i in range(len(nilai_mahasiswa)):
    print(f"{nama_mahasiswa[i]}: {nama_mata_kuliah[0]} = {nilai_mahasiswa[i][0]}, {nama_mata_kuliah[1]} = {nilai_mahasiswa[i][1]}")

# Menghitung rata-rata nilai tiap mahasiswa
print("\nRata-rata nilai tiap mahasiswa:")
for i in range(len(nilai_mahasiswa)):
    rata_rata = sum(nilai_mahasiswa[i]) / len(nilai_mahasiswa[i])
    print(f"{nama_mahasiswa[i]}: {rata_rata}")

# Menghitung rata-rata nilai tiap mata kuliah
print("\nRata-rata nilai tiap mata kuliah:")
for j in range(len(nama_mata_kuliah)):
    total = 0
    for i in range(len(nilai_mahasiswa)):
        total += nilai_mahasiswa[i][j]
    rata_rata = total / len(nilai_mahasiswa)
    print(f"{nama_mata_kuliah[j]}: {rata_rata}")
