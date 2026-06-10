#!/bin/bash

# Warna teks untuk estetika Termux
G="\033[0;32m" # Hijau
Y="\033[0;33m" # Kuning
R="\033[0;31m" # Merah
N="\033[0m"    # Normal

clear
echo -e "${G}=======================================================${N}"
echo -e "${G}   ██╗███╗   ███╗██████╗ ██╗  ██╗    ██████╗ ██╗ ██████╗${N}"
echo -e "${G}   ██║████╗ ████║██╔══██╗██║  ██║    ██╔══██╗██║██╔════╝${N}"
echo -e "${G}   ██║██╔████╔██║██████╔╝███████║    ██║  ██║██║██║  ███╗${N}"
echo -e "${G}   ██║██║╚██╔╝██║██╔══██╗██╔══██║    ██║  ██║██║██║   ██║${N}"
echo -e "${G}   ██║██║ ╚═╝ ██║██║  ██║██║  ██║    ██████╔╝██║╚██████╔╝${N}"
echo -e "${G}=======================================================${N}"
echo -e "${G}      AUTO-INSTALLER BOT SUPREME v56 BY MRH DIGITAL    ${N}"
echo -e "${G}=======================================================${N}"
echo ""

# 1. Update system & install package bawaan + Dependensi Kompresi Gambar
echo -e "${G}[1/5] Memperbarui sistem Termux & menginstal core packages...${N}"
pkg update && pkg upgrade -y

# Kunci penting: libjpeg-turbo dan zlib wajib ada di Termux untuk proses Pillow (Kompresi Gambar)
pkg install python git termux-api libjpeg-turbo zlib -y

# 2. Setup Storage (Meminta izin akses folder Galeri HP)
echo -e "${G}[2/5] Mengonfigurasi perizinan memori internal HP...${N}"
echo -e "${Y}⚠️  MOHON KLIK 'IZINKAN / ALLOW' PADA POP-UP DI HP KAMU SEBENTAR LAGI!${N}"
sleep 2
termux-setup-storage

# Upgrade pip ke versi paling gres
echo -e "${G}[3/5] Menginstal library Python tingkat lanjut (RAM Mode)...${N}"
pip install --upgrade pip

# Install requests untuk koneksi server dan Pillow untuk engine kompresi gambar
pip install requests pillow

# 3. Pindah ke direktori HOME untuk proses pembersihan folder lama
cd ~

# Hapus folder lama jika ada di HOME (Proses update / fresh install)
if [ -d "tools_rok_calculator_rss" ] && [ "$PWD" != "$HOME/tools_rok_calculator_rss" ]; then
    echo -e "${Y}🧹 Menghapus folder tools versi lama...${N}"
    rm -rf ~/tools_rok_calculator_rss
fi

# Clone repository fresh dari Github MRH Project
echo -e "${G}[4/5] Mengunduh script bot dari server GitHub...${N}"
git clone https://github.com/mrhproject/tools_rok_calculator_rss.git

# 4. Suntik otomatis alias mrh_update_stock ke .bashrc
echo -e "${G}[5/5] Memasang sistem pintasan alias 'mrh_update_stock'...${N}"
if [ ! -f ~/.bashrc ]; then
    touch ~/.bashrc
fi

# Bersihkan alias lama jika ada untuk menghindari duplikasi kode di .bashrc
sed -i '/alias mrh_update_stock/d' ~/.bashrc

# Masukkan perintah alias baru
echo "alias mrh_update_stock='cd ~/tools_rok_calculator_rss && python bot_rok.py'" >> ~/.bashrc
echo -e "${G}✅ Alias 'mrh_update_stock' berhasil dipasang ke sistem!${N}"

# Amankan konfigurasi
source ~/.bashrc &> /dev/null

echo ""
echo -e "${G}=======================================================${N}"
echo -e "${G} 🎉 PROSES INSTALASI SELESAI, BRE! GAS RUNNING...${N}"
echo -e "${G}=======================================================${N}"
echo -e "${Y}💡 TIPS PINTASAN:${N}"
echo -e "Mulai sekarang, untuk menyalakan bot cukup buka Termux dan ketik: ${G}mrh_update_stock${N}"
echo -e "${G}=======================================================${N}"
echo "🚀 Membuka folder dan menjalankan bot pertama kali..."
echo ""
sleep 2

# 5. Pindah ke folder dan langsung jalankan bot
cd ~/tools_rok_calculator_rss && python bot_rok.py
