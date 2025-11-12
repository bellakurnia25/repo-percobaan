class DatabasePohon:
    def __init__(self):
        self.data = []

    # TODO : Kerjakan disini (Fitur 1)
    def tambah_data_pohon (self, pohon):
        self.data.append(pohon)
        print("✅ Data pohon berhasil ditambahkan!")
    
    # TODO : Kerjakan disini (Fitur 2)
    def tampilkan_data_pohon(self):
        if not self.data:
            print("📭 Belum ada data pohon.")
        else:
            print("-"*82)
            print(f"| {'🆔 ID':^3} | {'🌳 Jenis':^14} | {'📍 Lokasi':^15} | {'📅 Tanggal Tanam':^10} | {'⏳ Umur':^13} |")
            print(f"{'-'*82}")
            for pohon in self.data:
                print(pohon.tampilkan())
            print(f"{'-'*82}")
    # TODO : Kerjakan disini (Fitur 4)
    def hapus_data_pohon(self, id_hapus):
        for pohon in self.data:
            if pohon.id == id_hapus:
                self.data.remove(pohon)
                return True
        return False