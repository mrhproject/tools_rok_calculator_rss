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
{G}███╗   ███╗██████╗       ██╗  ██╗     ██████╗ ██╗ ██████╗ ██╗████████╗ █████╗ ██╗     
████╗ ████║██╔══██╗      ██║  ██║     ██╔══██╗██║██╔════╝ ██║╚══██╔══╝██╔══██╗██║     
██╔████╔██║██████╔╝      ███████║     ██║  ██║██║██║  ███╗██║   ██║   ███████║██║     
██║╚██╔╝██║██╔══██╗      ██╔══██║     ██║  ██║██║██║   ██║██║   ██║   ██╔══██║██║     
██║ ╚═╝ ██║██║  ██║      ██║  ██║     ██████╔╝██║╚██████╔╝██║   ██║   ██║  ██║███████╗
╚═╝     ╚═╝╚═╝  ╚═╝      ╚═╝  ╚═╝     ╚═════╝ ╚═╝ ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝{N}
                                    
                 ✨ ᴹʳ 𝐇 𝐃𝐢𝐠𝐢𝐭𝐚 l ࿐ ✨
              🤖 AI-Universal Auto-RSS Standby 🤖
          [MODE SANDBOX UJI COBA CROP ADAPTIF AKTIF]
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
print('⏳ Siap siaga! Silakan ambil screenshot tabel SDA di RoK untuk menguji hasil crop...\n')

VALID_EXTENSIONS = {'.jpg', '.jpeg', '.png'}

# =========================================================================
# 🔄 MONITORING LOOP RUNTIME (UJI COBA CROP ADAPTIF TAB & HP)
# =========================================================================
while True:
    try:
        terbaru_entry = None
        terbaru_ctime = 0
        
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
                            continue

        if terbaru_entry:
            ss_terbaru = terbaru_entry.path
            nama_file = terbaru_entry.name
            
            last_sent = ''
            if os.path.exists(file_log):
                with open(file_log, 'r', encoding='utf-8') as f:
                    last_sent = f.read().strip()
            
            if nama_file != last_sent:
                print(f'📸 Terdeteksi SS Baru: {nama_file}')
                
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

                print('⚡ Menjalankan Engine Crop Adaptif & Penajaman Tabel SDA (RAM Mode)...')
                
                with Image.open(ss_terbaru) as img:
                    if img.mode in ("RGBA", "P"):
                        img = img.convert("RGB")
                    
                    # Mendapatkan resolusi asli HP / Tab yang digunakan secara dinamis
                    W, H = img.width, img.height
                    
                    # 🎯 FORMULA CROP UNIVERSAL: Mengunci area tengah agak ke kanan tempat tabel statistik berada.
                    # Formula ini dirancang agar aman baik di layar lebar HP memanjang maupun rasio kotak Tablet/Tab.
                    left = int(W * 0.18)
                    top = int(H * 0.05)
                    right = int(W * 0.82)
                    bottom = int(H * 0.92)
                    
                    img_cropped = img.crop((left, top, right, bottom))
                    
                    # Perbesar resolusi hasil potongan agar font angka gajah stabil saat dibaca server
                    max_size = 1400
                    if img_cropped.width > max_size:
                        ratio = max_size / float(img_cropped.width)
                        new_height = int(float(img_cropped.height) * float(ratio))
                        img_cropped = img_cropped.resize((max_size, new_height), Image.Resampling.LANCZOS)
                    
                    # 🔥 PROSES PENAJAMAN TEKS TABEL STATISTIK
                    # Naikkan kontras 60% agar warna font angka putih terisolasi tajam dari background biru
                    enhancer_kontras = ImageEnhance.Contrast(img_cropped)
                    img_cropped = enhancer_kontras.enhance(1.6)
                    
                    # Pertajam tepi font angka game 2.5x lipat
                    enhancer_tajam = ImageEnhance.Sharpness(img_cropped)
                    img_cropped = enhancer_tajam.enhance(2.5)
                    
                    # Simpan hasil olahan langsung ke RAM Buffer
                    buffer = BytesIO()
                    img_cropped.save(buffer, format="JPEG", quality=90, optimize=True)
                    nilai_mentah_b64 = buffer.getvalue()
                
                encoded = base64.b64encode(nilai_mentah_b64).decode('utf-8')
                
                payload = {
                    'image': encoded, 
                    'filename': nama_file,
                    'user_id': DEVICE_UNIQUE_ID
                }
                
                print('🚀 Mengirim paket uji coba gambar ke GAS Sandbox...')
                headers = {'Content-Type': 'application/json'}
                response = requests.post(URL_WEB_APP, data=json.dumps(payload), headers=headers, timeout=25)
                
                if response.status_code == 200:
                    with open(file_log, 'w', encoding='utf-8') as f:
                        f.write(nama_file)
                    
                    print('📥 --- RESPON HASIL SCAN SERAVAH DARI CLOUD ---')
                    try:
                        res_json = response.json()
                        print(res_json.get("teks_hasil_ocr_mentah", "Teks kosong!"))
                    except:
                        print(response.text)
                    print('-----------------------------------------------')
                    
                    # 🗑️ AUTO-CLEAN GALLERY
                    try:
                        if os.path.exists(ss_terbaru):
                            os.remove(ss_terbaru)
                            print('🗑️ [AUTO-CLEAN] File fisik dibersihkan dari galeri.')
                    except Exception as err_del:
                        print(f'⚠️ Gagal menghapus file fisik: {err_del}')
                        
                else:
                    print(f'❌ Server Mengalami Kendala Respon HTTP: {response.status_code}')
                                        
    except Exception as e:
        print(f'❌ Sistem Mengalami Gangguan: {e}')
        
    time.sleep(5)
