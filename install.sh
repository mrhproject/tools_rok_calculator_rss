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
echo -e "${G}        AUTO-INSTALLER BOT SUPREME v58.1 BY MRH DIGITAL   ${N}"
echo -e "${G}           [FIXED REPOSITORY & PILLOW COMPILER]          ${N}"
echo -e "${G}=======================================================${N}"
echo ""

# =========================================================================
# 🚨 GERBANG UTAMA: KONFIGURASI URL WEB APP USER BARU
# =========================================================================
echo -e "${Y}[?] Tempel/Paste URL Google Web App Anda di bawah ini:${N}"
read -r INPUT_URL

# Validasi tipis agar user tidak mengosongkan URL
if [ -z "$INPUT_URL" ]; then
    echo -e "${R}❌ URL tidak boleh kosong, Bre! Silakan jalankan ulang script.${N}"
    exit 1
fi

# Otomatis membuat atau menimpa file config.py sesuai input user baru
cat <<EOF > config.py
URL_WEB_APP = '$INPUT_URL'
EOF
echo -e "${G}✅ File config.py berhasil dikonfigurasi secara otomatis!${N}"
echo ""

# Ambil jalur folder aktif saat ini agar eksekusi script aman
JALUR_SEKARANG=$(pwd)

# 1. SETUP STORAGE DI PALING ATAS
echo -e "${G}[1/4] Mengonfigurasi perizinan memori internal HP...${N}"
echo -e "${Y}⚠️  MOHON KLIK 'IZINKAN / ALLOW' PADA POP-UP DI HP KAMU SEBENTAR LAGI!${N}"
termux-setup-storage
sleep 3

# Trik menyegarkan jalur filesystem Android agar langsung sinkron
am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard &> /dev/null

# 2. SEGARKAN REPOSITORY & UPDATE INTEL
echo -e "${G}[2/4] Memperbarui sistem Termux & menginstal core packages...${N}"
apt update -y
pkg update -y

# FIX NAME: Menggunakan paket library yang valid di Termux environment tanpa dev-postfix
echo -e "${G}⏳ Memasang Python, Git, dan library pendukung gambar...${N}"
pkg install python git termux-api libjpeg-turbo zlib binutils ndk-sysroot clang make -y

# Pastikan environment Python & Pip benar-benar terpasang sebelum upgrade
if ! command -v python &> /dev/null; then
    echo -e "${R}❌ Python gagal terpasang otomatis. Mencoba metode alternatif...${N}"
    apt install python -y
fi

# Upgrade pip ke versi paling stabil
python -m pip install --upgrade pip

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

# Buat file perintah langsung ke direktori binary utama Termux ($PREFIX/bin)
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
echo "🚀 Langsung menyalakan mesin bot..."
echo ""
sleep 1.5

# 4. EKSEKUSI BOT SEGAR INSTAN
cd $JALUR_SEKARANG && python bot_rok.py
