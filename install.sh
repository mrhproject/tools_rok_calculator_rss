#!/data/data/com.termux/files/usr/bin/bash

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
echo -e "${G}       AUTO-INSTALLER BOT SUPREME v58 BY MRH DIGITAL    ${N}"
echo -e "${G}         [EDISI STABIL OPTIMASI DEPENDENSI PILLOW]       ${N}"
echo -e "${G}=======================================================${N}"
echo ""

# Ambil jalur folder aktif saat ini agar eksekusi script aman
JALUR_SEKARANG=$(pwd)

# 1. SETUP STORAGE DI PALING ATAS (ANTI GEMBOK/ANTI GANTUNG)
echo -e "${G}[1/4] Mengonfigurasi perizinan memori internal HP...${N}"
echo -e "${Y}⚠️  MOHON KLIK 'IZINKAN / ALLOW' PADA POP-UP DI HP KAMU SEBENTAR LAGI!${N}"
termux-setup-storage
sleep 3

# Trik menyegarkan jalur filesystem Android agar langsung sinkron
am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard &> /dev/null

# 2. UPDATE SYSTEM & DEPENDENSI INTI (DENGAN FIX COMPILER PILLOW)
echo -e "${G}[2/4] Memperbarui sistem Termux & menginstal core packages...${N}"
apt update && apt full-upgrade -y

# Tambahan libjpeg-turbo-dev & zlib-dev wajib agar Pillow tidak error saat di-compile di Android baru
pkg install python git termux-api libjpeg-turbo libjpeg-turbo-dev zlib zlib-dev binutils -y

# Upgrade pip ke versi paling stabil
pip install --upgrade pip

# Pasang requests dan pillow dengan opsi pembersihan cache agar fresh
echo -e "${G}⏳ Memasang pustaka Python (Requests & Pillow RAM Mode)...${N}"
pip install requests
pip install pillow --no-cache-dir

# 3. REGISTER PERINTAH SAKTI GLOBAL
echo -e "${G}[3/4] Memasangkan sistem eksekusi global 'mrh_update_stock'...${N}"

if [ -f ~/.bashrc ]; then
    sed -i '/alias mrh_update_stock/d' ~/.bashrc
fi

if [ -f "$PREFIX/bin/mrh_update_stock" ]; then
    rm -f $PREFIX/bin/mrh_update_stock
fi

# Buat file perintah langsung ke direktori binary utama Termux ($PREFIX/bin) menggunakan jalur dinamis
echo '#!/data/data/com.termux/files/usr/bin/bash' > $PREFIX/bin/mrh_update_stock
echo "cd $JALUR_SEKARANG && python bot_rok.py" >> $PREFIX/bin/mrh_update_stock

# Berikan izin eksekusi penuh ke sistem Termux
chmod +x $PREFIX/bin/mrh_update_stock

echo ""
echo -e "${G}=======================================================${N}"
echo -e "${G} 🎉 PROSES INSTALASI SELESAI SAKTI TANPA DRAMA, BRE!${N}"
echo -e "${G}=======================================================${N}"
echo -e "${Y}💡 TIPS PINTASAN GLOBAL:${N}"
echo -e "Sekarang, dari folder mana saja, cukup ketik: ${G}mrh_update_stock${N}"
echo -e "${G}=======================================================${N}"
echo "🚀 Langsung menyalakan mesin bot pertama kali..."
echo ""
sleep 1.5

# 4. EKSEKUSI BOT SEGAR INSTAN
cd $JALUR_SEKARANG && python bot_rok.py
