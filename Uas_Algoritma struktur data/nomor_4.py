class Buah:
    def __init__(self, nama="", warna="", rasa=""):
        self.nama = nama
        self.warna = warna
        self.rasa = rasa

    def setNama(self, nama):
        self.nama = nama

    def setWarna(self, warna):
        self.warna = warna

    def setRasa(self, rasa):
        self.rasa = rasa

    def tampilkanInfo(self):
        print(f"Nama: {self.nama}")
        print(f"Warna: {self.warna}")
        print(f"Rasa: {self.rasa}")

if __name__ == "__main__":
    buah1 = Buah()
    buah1.setNama("Apel")
    buah1.setWarna("Merah")
    buah1.setRasa("Manis")
    buah1.tampilkanInfo()

    print("\n")

    buah2 = Buah("Mangga", "Kuning", "Asam")
    buah2.tampilkanInfo()
