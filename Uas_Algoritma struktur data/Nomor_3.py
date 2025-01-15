class RestoranQueue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, pesanan):
        self.queue.append(pesanan)
        print(f"Pesanan '{pesanan}' berhasil ditambahkan ke antrian.")
    
    def dequeue(self):
        if len(self.queue) > 0:
            pesanan = self.queue.pop(0)
            print(f"Pesanan '{pesanan}' berhasil dihapus dari antrian.")
            return pesanan
        else:
            print("Antrian kosong. Tidak ada pesanan yang bisa dihapus.")
            return None
    
    def tampilkan_antrian(self):
        if len(self.queue) > 0:
            print("Antrian saat ini:")
            for i, pesanan in enumerate(self.queue, start=1):
                print(f"{i}. {pesanan}")
        else:
            print("Antrian kosong.")

antrian_restoran = RestoranQueue()

while True:
    print("\nPilihan:")
    print("1. Tambah Pesanan (Enqueue)")
    print("2. Hapus Pesanan (Dequeue)")
    print("3. Tampilkan Antrian")
    print("4. Keluar")
    
    pilihan = input("Masukkan pilihan: ")
    
    if pilihan == '1':
        pesanan = input("Masukkan nama pesanan: ")
        antrian_restoran.enqueue(pesanan)
    elif pilihan == '2':
        antrian_restoran.dequeue()
    elif pilihan == '3':
        antrian_restoran.tampilkan_antrian()
    elif pilihan == '4':
        print("Terima kasih. Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
