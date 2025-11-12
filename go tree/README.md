# Go-Tree-by-AP-12
# 🌳 Go Tree – Aplikasi CLI Pemantauan Bibit Pohon

**Go Tree** adalah aplikasi Command Line Interface (CLI) yang dirancang untuk membantu pencatatan, pemantauan, dan analisis pertumbuhan bibit pohon berdasarkan data penanaman dan kondisi lingkungan. Aplikasi ini mendukung pelestarian lingkungan dengan mencatat setiap pohon yang ditanam, menghitung umurnya, serta monitoring dengan memberikan saran pemeliharaan berdasarkan musim dan kondisi pohon.

---

## 📦 Fitur Utama

Fitur & Deskripsi 
| 🌱 Tambah Data Pohon | Menambahkan data bibit pohon yang ditanam (jenis, lokasi, tanggal tanam). ID pohon dibuat otomatis. |
| 📊 Tampilkan Data Pohon | Menampilkan seluruh data pohon dalam bentuk tabel, termasuk umur pohon yang dihitung otomatis. |
| ⏳ Submenu Umur & Tanggal | - Hitung umur pohon berdasarkan tanggal referensi | - Tentukan tanggal saat pohon mencapai umur tertentu |
| 🧠 Analisis Pemeliharaan | Memberikan saran pemeliharaan berdasarkan umur pohon dan musim saat ini (hujan/kemarau). |
| 📝 Input Kondisi & Kunjungan | Menambahkan data kunjungan pohon (tanggal dan kondisi: subur/kering/layu). |
| 📋 Tabel Kondisi Pohon | Menampilkan tabel kondisi terakhir setiap pohon beserta pesan analisis. |
| 🗑️ Hapus Data Pohon | Menghapus data pohon berdasarkan ID setelah ditampilkan ulang. |
| 🚪 Keluar | Menutup aplikasi dengan pesan ramah. |

---

## 🧾 Data yang Dicatat

- 🆔 ID Pohon (otomatis)
- 🌳 Jenis Pohon
- 📍 Lokasi Penanaman
- 📅 Tanggal Tanam (validasi: tidak boleh melebihi tanggal hari ini)
- ⏳ Umur Pohon (dihitung otomatis)
- 🖥️ Kondisi Terakhir (subur/kering/layu)
- 📅 Tanggal Kunjungan Terakhir
- 💬 Pesan Analisis Kondisi

---

## 🗓️ Logika Musim & Pemeliharaan

- **Musim Hujan**: Oktober – April  
- **Musim Kemarau**: Mei – September  
- **Pohon Muda**: < 180 hari  
- **Pohon Tua**: ≥ 180 hari  

| Musim | Umur | Saran Pemeliharaan |
|-------|------|---------------------|
| Hujan | Muda | Pastikan drainase baik agar akar tidak membusuk |
| Hujan | Tua  | Periksa batang dan cabang dari kerusakan akibat angin |
| Kemarau | Muda | Siram rutin pagi dan sore, hindari kekeringan |
| Kemarau | Tua  | Pangkas cabang kering, periksa daun secara berkala |

---

## 🛠️ Cara Menjalankan

1. Pastikan Python 3.x sudah terinstal
2. Clone repository:
   ```bash
   git clone https://github.com/Charice2407/Go-Tree-by-AP-12.git
   cd go-tree
3. python main.py

## 🗃️ Struktur Folder

go-tree/
├── main.py               # CLI utama
├── pohon.py              # Kelas Pohon dan logika analisis
├── database.py           # Manajemen data pohon
├── utils.py              # Validasi tanggal
├── README.md             # Dokumentasi proyek

## 👥 Kontributor

**Ketua Kelompok & Pengembang Utama
- Glenn Robean Runtunuwu (H071251020)

**Anggota & Pengembang Fitur
- Kurnia Natalia Bela (H071251040) 
- Patricius Reinhard Danduru (H071251074)
- Moh Varel Julianto EP (H071251048)     
- Chereen Bunga Catalina Ramba (H071251072)
- Andi Jusuf Permana Putra Djoeddawi (H071251078)
- Muhammad Ihsan Althaf Eddy (H071251066)

## 📚 Lisensi
Proyek ini dibuat untuk keperluan MID Project dari praktikum mata kuliah Algoritma dan Pemrograman 2025 dan bersifat open-source untuk edukasi dan pelestarian lingkungan.

