#!/bin/bash
# Hapus folder lama agar instalasi selalu fresh
rm -rf ~/tools_rok_calculator_rss

G="\033[0;32m"
N="\033[0m"

echo -e "${G}=== INSTALASI OTOMATIS TOOLS ROK CALCULATOR RSS ===${N}"

# 1. Update system & install package
pkg update && pkg upgrade -y
pkg install python git termux-api -y
termux-setup-storage
pip install --upgrade pip
pip install requests

# 2. Suntik otomatis alias mrh_update_stock ke .bashrc
echo -e "${G}=== MENGINSTAL ALIAS SAKTI 'mrh_update_stock' ===${N}"
if ! grep -q "alias mrh_update_stock" ~/.bashrc; then
    echo "alias mrh_update_stock='cd ~/tools_rok_calculator_rss && python bot_rok.py'" >> ~/.bashrc
    echo -e "${G}Alias 'mrh_update_stock' berhasil ditambahkan!${N}"
else
    echo -e "${G}Alias sudah ada, lanjut...${N}"
fi

# Refresh konfigurasi terminal
if [ -f ~/.bashrc ]; then
    source ~/.bashrc
fi

echo -e "${G}===========================================${N}"
echo -e "${G}INSTALASI SELESAI, BRE! GAS RUNNING...${N}"
echo -e "${G}===========================================${N}"

# 3. Pindah ke folder sebelum menjalankan bot
cd ~/tools_rok_calculator_rss && python bot_rok.py
