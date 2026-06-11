import os
import base64
import json
import time
import uuid
import sys
from io import BytesIO

# ⚡ VALIDASI DEPENDENSI UTAMA (AUTO-INSTALLER)
try:
    import requests
    from PIL import Image, ImageEnhance
except ImportError:
    print("⏳ Menyiapkan library tambahan (requests & pillow)...")
    os.system('pkg install libjpeg-turbo-dev zlib-dev -y &> /dev/null')
    os.system('pip install requests pillow &> /dev/null')
    import requests
    from PIL import Image, ImageEnhance

from config import URL_WEB_APP

# =========================================================================
# 🔥 ENGINE PENGUNCI DEVICE ID PERMANEN (ANTI GANTI / ANTI RESET)
# =========================================================================
def dapatkan_device_id_permanen():
    nama_file_id = '.device_id.txt'
    
    if os.path.exists(nama_file_id):
        try:
            with open(nama_file_id, 'r', encoding='utf-8') as f:
                device_id = f.read().strip()
                if device_id: 
                    return device_id
        except:
            pass

    id_acak = str(uuid.uuid4()).replace('-', '')[:12].upper() 
    device_id = f"MRH-{id_acak}"
    
    with open(nama_file_id, 'w', encoding='utf-8') as f:
        f.write(device_id)
            
    return device_id

DEVICE_UNIQUE_ID = dapatkan_device_id_permanen()

# =========================================================================
# 🎨 BRANDING LOGO INTERFACES
# =========================================================================
def tampilkan_logo():
    G = "\033[0;32m"  # Hijau Cerah
    Y = "\033[0;33m"  # Kuning Cerah
    N = "\033[0m"     # Normal
    
    logo = f"""
{G}███╗   ███╗██████╗       ██╗  ██╗    ██████╗ ██╗ ██████╗ ██╗████████╗ █████╗ ██╗     
████╗ ████║██╔══██╗      ██║  ██║    ██╔══██╗██║██╔════╝ ██║╚══██╔══╝██╔══██╗██║     
██╔████╔██║██████╔╝      ███████║    ██║  ██║██║██║  ███╗██║   ██║   ███████║██║     
██║╚██╔╝██║██╔══██╗      ██╔══██║    ██║  ██║██║██║   ██║██║   ██║   ██╔══██║██║     
██║ ╚═╝ ██║██║  ██║      ██║  ██║    ██████╔╝██║╚██████╔╝██║   ██║   ██║  ██║███████╗
╚═╝     ╚═╝╚═╝  ╚═╝      ╚═╝  ╚═╝    ╚═════╝ ╚═╝ ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝{N}
                                    
                ✨ ᴹʳ 𝐇 𝐃𝐢𝐠𝐢𝐭𝐚 l ࿐ ✨
             🤖 AI-Universal Auto-RSS Standby 🤖
          [MODE SUPREME SPEED & AUTO-CLEAN HQ AKTIF]
===================================================================================
🔑 {Y}ID PERANGKAT ABADI (KTP): {DEVICE_UNIQUE_ID}{N}
===================================================================================
    """
    print(logo)

def verifikasi_user():
    G = "\033[0;32m"
    N = "\033[0m"
    print(f"{G}🔐 [SECURITY] Sistem Verifikasi Akses Mr H Digital{N}")
    print("⏳ Memeriksa hak akses ke server Cloud...")
    print(f"{G}✅ BYPASS HAK AKSES AKTIF! Selamat bekerja, Bre!{N}\n")
    return True

def cari_folder_ss_otomatis():
    posisi_pencarian = ['/sdcard/DCIM/', '/sdcard/Pictures/', '/sdcard/MyFiles/', '/sdcard/']
    nama_target = ['Screenshots', 'Screenshot', 'TangkapanLayar']
    
    for posisi in posisi_pencarian:
        if os.path.exists(posisi):
            for target in nama_target:
                jalur_cek = os.path.join(posisi, target)
                if os.path.exists(jalur_cek) and os.path.isdir(jalur_cek):
                    return jalur_cek
                    
    return '/sdcard/DCIM/Screenshots'

# --- INITIALIZATION CORE ---
tampilkan_logo()

if not verifikasi_user():
    print("\n🛑 [STOP] Program dihentikan otomatis.")
    sys.exit()

FOLDER_TARGET = cari_folder_ss_otomatis()
file_log = '.terakhir_dikirim.txt'

print('🤖 [START] Bot RoK Auto-Standby AI-Universal Supreme Aktif...')
print(f'🎯 Folder Pantauan: {FOLDER_TARGET}')
print('⏳ Siap siaga! Cukup lakukan screenshot di game RoK, data meluncur otomatis...\n')

# Kumpulan format gambar yang diizinkan (Set murni agar pencarian instan)
VALID_EXTENSIONS = {'.jpg', '.jpeg', '.png'}

# =========================================================================
# 🔄 MONITORING LOOP RUNTIME (OPTIMIZED VERSION v5.0)
# =========================================================================
while True:
    try:
        terbaru_entry = None
        terbaru_ctime = 0
        
        # 🔥 OPTIMASI 1: Ganti glob kaku dengan os.scandir (Baterai awet, RAM adem)
        if os.path.exists(FOLDER_TARGET):
            with os.scandir(FOLDER_TARGET) as entries:
                for entry in entries:
                    if entry.is_file() and os.path.splitext(entry.name)[1].lower() in VALID_EXTENSIONS:
                        try:
                            file_ctime = entry.stat().st_ctime
                            if file_ctime > terbaru_ctime:
                                terbaru_ctime = file_ctime
                                terbaru_entry = entry
                        except OSError:
                            continue  # Lewati jika file sedang dikunci sistem Android

        if terbaru_entry:
            ss_terbaru = terbaru_entry.path
            nama_file = terbaru_entry.name
            
            # Baca logs riwayat
            last_sent = ''
            if os.path.exists(file_log):
                with open(file_log, 'r', encoding='utf-8') as f:
                    last_sent = f.read().strip()
            
            # Deteksi jika benar-benar ada jepretan baru
            if nama_file != last_sent:
                print(f'📸 Terdeteksi SS Baru: {nama_file}')
                
                # 🔥 OPTIMASI 2: Tunggu sampai Android selesai menulis gambar ke memori (Anti-Corrupt)
                time.sleep(0.5)
                ukuran_lama = -1
                while True:
                    try:
                        ukuran_baru = os.path.getsize(ss_terbaru)
                        if ukuran_baru == ukuran_lama and ukuran_baru > 0:
                            break
                        ukuran_lama = ukuran_baru
                        time.sleep(0.2)
                    except OSError:
                        break

                print('⚡ Menjalankan Engine Kompresi & Penajaman Gambar MRH Digital (RAM Mode)...')
                
                # 🛠️ TWEAK RESOLUSI, KONTRAS & KETAJAMAN HQ
                with Image.open(ss_terbaru) as img:
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")
                    
                    # Batasi resolusi maksimal lebar ke 1600px biar proporsional
                    max_size = 1600
                    if img.width > max_size:
                        ratio = max_size / float(img.width)
                        new_height = int(float(img.height) * float(ratio))
                        img = img.resize((max_size, new_height), Image.Resampling.LANCZOS)
                    
                    # 🔥 OPTIMASI 3: Dongkrak Kontras & Ketajaman Teks Angka Kecil game RoK
                    enhancer_kontras = ImageEnhance.Contrast(img)
                    img = enhancer_kontras.enhance(1.4)  # Naikkan kontras 40%
                    
                    enhancer_tajam = ImageEnhance.Sharpness(img)
                    img = enhancer_tajam.enhance(2.0)    # Pertajam tepi font angka 2x lipat
                    
                    # Simpan hasil kompresi langsung ke memory RAM buffer
                    buffer = BytesIO()
                    img.save(buffer, format="JPEG", quality=90, optimize=True)
                    nilai_mentah_b64 = buffer.getvalue()
                
                # Encode hasil kompresi memori RAM ke Base64 text string
                encoded = base64.b64encode(nilai_mentah_b64).decode('utf-8')
                
                payload = {
                    'image': encoded, 
                    'filename': nama_file,
                    'user_id': DEVICE_UNIQUE_ID
                }
                
                print('🚀 Mentransfer paket data mini ke Cloud Sheets...')
                headers = {'Content-Type': 'application/json'}
                response = requests.post(URL_WEB_APP, data=json.dumps(payload), headers=headers, timeout=25)
                
                # Eksekusi aksi pasca sukses terkirim
                if response.status_code == 200:
                    with open(file_log, 'w', encoding='utf-8') as f:
                        f.write(nama_file)
                    print('✅ Transaksi Sukses! Data masuk Database.')
                    
                    # 🗑️ AUTO-CLEAN GALLERY: Langsung hapus file fisik asli dari HP
                    try:
                        if os.path.exists(ss_terbaru):
                            os.remove(ss_terbaru)
                            print('🗑️ [AUTO-CLEAN] Berhasil menghapus file fisik sampah dari galeri.')
                    except Exception as err_del:
                        print(f'⚠️ Gagal menghapus file fisik: {err_del}')
                        
                else:
                    print(f'❌ Server Mengalami Kendala Respon HTTP: {response.status_code}')
                                        
    except Exception as e:
        print(f'❌ Sistem Mengalami Gangguan: {e}')
        
    # 🔥 OPTIMASI 4: Naikkan jeda jadi 5 detik agar Apps Script punya waktu bernapas memperbarui hash_waktu
    time.sleep(5)
