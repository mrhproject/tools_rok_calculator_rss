Markdown
# 🤖 Tools RoK Calculator RSS (Auto-Standby)

Automated screenshot uploader for Rise of Kingdoms resource calculation. Script ini berfungsi untuk memantau folder screenshot perangkat secara real-time dan otomatis mengirimkan gambar terbaru ke cloud database (Google Apps Script Web App) tanpa perlu keluar dari game.

---

## ⚡ Fitur Utama
* **Multi-Device Support:** Otomatis mendeteksi folder screenshot bawaan sistem Android (Samsung, Oppo, Vivo, dll) maupun Huawei/HarmonyOS (MatePad/Pictures).
* **Auto-Standby Loop:** Berjalan senyap di latar belakang setiap 3 detik mencari data screenshot baru.
* **Anti-Duplikasi:** Sistem log internal mendeteksi nama file agar gambar yang sama tidak terkirim dua kali.
* **Lightweight:** Sangat ringan dijalankan di Termux dan hemat konsumsi RAM perangkat.

---

## 🚀 Cara Instalasi Otomatis (Termux)

Buka aplikasi **Termux** di HP atau Tablet kamu, lalu cukup *copy-paste* satu baris perintah sakti di bawah ini dan tekan **Enter**:

```bash
pkg install git -y && git clone [https://github.com/mrhproject/tools_rok_calculator_rss.git](https://github.com/mrhproject/tools_rok_calculator_rss.git) && cd tools_rok_calculator_rss && chmod +x install.sh && ./install.sh
⚠️ PENTING SAAT INSTALASI:
Saat proses berjalan, Termux akan memunculkan pop-up izin memori: "Termux requests storage access". Pastikan kamu klik ALLOW / IZINKAN agar bot bisa membaca folder screenshot.

🕹️ Cara Menjalankan Bot di Kemudian Hari
Jika instalasi sudah selesai dan kamu ingin menyalakan kembali bot ini di lain waktu, cukup buka Termux dan ketik perintah ringkas ini:

Bash
cd tools_rok_calculator_rss && python bot_rok.py
🔄 Cara Mengambil Pembaruan Script (Update)
Jika ada pembaruan fitur dari pemilik repository, kamu tinggal ketik perintah ini di dalam folder untuk melakukan sinkronisasi otomatis:

Bash
git pull
🛡️ Konfigurasi Tambahan (Biar Bot Gak Mati di Background)
Agar sistem operasi perangkat tidak membunuh proses Termux saat kamu sedang asyik bermain game, lakukan langkah taktis ini:

Tarik bar notifikasi perangkat ke bawah pada bagian Termux, lalu klik Acquire Wakelock (Mengunci performa CPU).

Masuk ke Pengaturan Perangkat > Aplikasi > Peluncuran Aplikasi (App Launch) > Cari Termux > Ubah ke Kelola Manual (Manage Manually) > Aktifkan opsi Berjalan di Latar Belakang (Run in Background).

Developed by MrH Project 🚀🔥


---

### 💾 Cara Eksekusi Terakhir di GitHub Browser:
1. Buka repository: `[https://github.com/mrhproject/tools_rok_calculator_rss](https://github.com/mrhproject/tools_rok_calculator_rss)`.
2. Klik file **`README.md`**.
3. Klik **ikon pensil** di kanan atas untuk mengedit.
4. Hapus total semua tulisan lama yang ada di sana.
5. *Paste* kode penuh di atas ke dalam kotak, lalu klik tombol hijau **`Commit changes...`** di pojok kanan atas.

Sekarang lapak repository asisten pertanian RoK kamu sudah resmi beres, tampan, rapi, dan siap
