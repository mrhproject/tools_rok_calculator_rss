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
echo -e "${G}       AUTO-INSTALLER BOT SUPREME v56 BY MRH DIGITAL    ${N}"
echo -e "${G}=======================================================${N}"
echo ""

# 1. SETUP STORAGE DI PALING ATAS (ANTI GEMBOK/ANTI GANTUNG)
echo -e "${G}[1/5] Mengonfigurasi perizinan memori internal HP...${N}"
echo -e "${Y}⚠️  MOHON KLIK 'IZINKAN / ALLOW' PADA POP-UP DI HP KAMU SEBENTAR LAGI!${N}"
termux-setup-storage
sleep 3

# Trik menyegarkan jalur filesystem Android agar langsung sinkron
am broadcast -a android.intent.action.MEDIA_MOUNTED -d file:///sdcard &> /dev/null

# 2. PINDAH KE HOME & MANDATORI SAPU BERSIH FOLDER LAMA
cd $HOME
echo -e "${G}[2/5] Membersihkan sisa-sisa instalasi folder lama...${N}"
# Paksa hapus total tanpa syarat gantung agar git clone 100% anti-gagal
if [ -d "tools_rok_calculator_rss" ]; then
    echo -e "${Y}🧹 Menghapus folder tools versi lama secara permanen...${N}"
    rm -rf tools_rok_calculator_rss
fi

# 3. UPDATE SYSTEM & DEPENDENSI INTI
echo -e "${G}[3/5] Memperbarui sistem Termux & menginstal core packages...${N}"
apt update && apt full-upgrade -y
pkg install python git termux-api libjpeg-turbo zlib -y

# Upgrade pip dan pasang library Pillow RAM Mode + Requests
pip install --upgrade pip
pip install requests pillow

# 4. CLONE REPOSITORY FRESH DARI GITHUB
echo -e "${G}[4/5] Mengunduh script bot murni dari server GitHub...${N}"
git clone https://github.com/mrhproject/tools_rok_calculator_rss.git

# 5. REGISTER PERINTAH SAKTI GLOBAL (BISA DIPANGGIL DARI MANA SAJA LAH!)
echo -e "${G}[5/5] Memasang sistem eksekusi global 'mrh_update_stock'...${N}"

# Bersihkan sisa-sisa gantung alias lama di .bashrc agar tidak menumpuk sampah kode
if [ -f ~/.bashrc ]; then
    sed -i '/alias mrh_update_stock/d' ~/.bashrc
fi

# Hapus shortcut bin lama jika terdeteksi
if [ -f "$PREFIX/bin/mrh_update_stock" ]; then
    rm -f $PREFIX/bin/mrh_update_stock
fi

# Buat file perintah langsung ke direktori binary utama Termux ($PREFIX/bin)
echo '#!/data/data/com.termux/files/usr/bin/bash' > $PREFIX/bin/mrh_update_stock
echo 'cd $HOME/tools_rok_calculator_rss && python bot_rok.py' >> $PREFIX/bin/mrh_update_stock

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

# Eksekusi langsung perintah global yang baru kita buat
mrh_update_stock
