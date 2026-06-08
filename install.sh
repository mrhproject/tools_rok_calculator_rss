#!/bin/bash
G="\033[0;32m"
N="\033[0m"
echo -e "${G}=== INSTALASI OTOMATIS TOOLS ROK CALCULATOR RSS ===${N}"
pkg update && pkg upgrade -y
pkg install python git termux-api -y
termux-setup-storage
pip install --upgrade pip
pip install requests
echo -e "${G}===========================================${N}"
echo -e "${G}INSTALASI SELESAI, BRE! GAS RUNNING...${N}"
echo -e "${G}===========================================${N}"
python bot_rok.py
