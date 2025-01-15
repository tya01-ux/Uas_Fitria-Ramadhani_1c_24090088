import numpy as np

jumlah_siswa = input("Masukkan nama siswa: ")
nilai_siswa = []

for i in range(jumlah_siswa):
    nilai = int(input(f"Masukkan nilai siswa ke-{i + 1}: "))
    nilai_siswa.append(nilai)

nilai_siswa = np.array(nilai_siswa)
rata_rata = np.mean(nilai_siswa)
nilai_tertinggi = np.max(nilai_siswa)
nilai_terendah = np.min(nilai_siswa)
siswa_di_atas_rata_rata = np.sum(nilai_siswa > rata_rata)

print(f"Nilai rata-rata: {rata_rata}")
print(f"Nilai tertinggi: {nilai_tertinggi}")
print(f"Nilai terendah: {nilai_terendah}")
print(f"Jumlah siswa di atas rata-rata: {siswa_di_atas_rata_rata}")

