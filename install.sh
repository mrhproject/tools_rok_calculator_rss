#!/bin/bash

G="\033[0;32m"
N="\033[0m"

echo -e "${G}=== INSTALASI OTOMATIS TOOLS ROK CALCULATOR RSS ===${N}"

# 1. Update system & install package bawaan
pkg update && pkg upgrade -y
pkg install python git termux-api -y

# 2. Setup Storage (Pastikan klik "Izinkan" di HP kamu)
termux-setup-storage

# Upgrade pip & install library yang dibutuhkan
pip install --upgrade pip
pip install requests

# 3. Pindah ke direktori HOME untuk proses pembersihan folder lama
cd ~

# Hapus folder lama jika ada di HOME (Proses update/fresh install)
# KOREKSI: Ini aman dilakukan karena script saat ini dipanggil dari luar folder targets
if [ -d "tools_rok_calculator_rss" ] && [ "$PWD" != "$HOME/tools_rok_calculator_rss" ]; then
    rm -rf ~/tools_rok_calculator_rss
fi

# Jika foldernya belum ada di HOME (karena dihapus tadi), kita clone ulang ke posisi yang benar
if [ ! -d "tools_rok_calculator_rss" ]; then
    git clone https://github.com/mrhproject/tools_rok_calculator_rss.git
fi

# 4. Suntik otomatis alias mrh_update_stock ke .bashrc
echo -e "${G}=== MENGINSTAL ALIAS SAKTI 'mrh_update_stock' ===${N}"
if [ ! -f ~/.bashrc ]; then
    touch ~/.bashrc
fi

if ! grep -q "alias mrh_update_stock" ~/.bashrc; then
    echo "alias mrh_update_stock='cd ~/tools_rok_calculator_rss && python bot_rok.py'" >> ~/.bashrc
    echo -e "${G}Alias 'mrh_update_stock' berhasil ditambahkan!${N}"
else
    echo -e "${G}Alias sudah ada, lanjut...${N}"
fi

# Refresh konfigurasi terminal agar langsung aktif seketika
source ~/.bashrc

echo -e "${G}===========================================${N}"
echo -e "${G}INSTALASI SELESAI, BRE! GAS RUNNING...${N}"
echo -e "${G}===========================================${N}"

# 5. Pindah ke folder dan langsung jalankan bot
cd ~/tools_rok_calculator_rss && python bot_rok.py
