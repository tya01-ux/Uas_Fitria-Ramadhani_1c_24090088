data_mahasiswa = []

while True:
    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    
    data_mahasiswa.append({"NIM": nim, "Nama": nama})
    
    tambah_lagi = input("Ingin tambah lagi? (ya/tidak): ").strip().lower()
    if tambah_lagi != 'ya':
        break

# Menampilkan data mahasiswa
print("\nData Mahasiswa:")
print("===========================")
for i, mahasiswa in enumerate(data_mahasiswa, start=1):
    print(f"{i}. NIM: {mahasiswa['NIM']}, Nama: {mahasiswa['Nama']}")
print("===========================")
