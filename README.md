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
