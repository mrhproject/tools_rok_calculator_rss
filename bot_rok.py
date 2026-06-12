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
          [SINKRONISASI AKTIF ENGINE MULTI-ACCOUNT API V58]
===================================================================================
🔑 {Y}ID PERANGKAT ABADI (KTP): {DEVICE_UNIQUE_ID}{N}
===================================================================================
    """
    print(logo)

def verifikasi_user():
    G = "\033[0;32m"
    N = "\033[0m"
    print(f"{G}🔐 [SECURITY] Sistem Verifikasi Akses Mr H Digital{N}")
    print("⏳ Memeriksa status lisensi perangkat ke server Cloud...")
    
    # Menembak aksi verifikasi token murni ke GAS
    try:
        payload = {"user_id": DEVICE_UNIQUE_ID, "action": "verify"}
        headers = {'Content-Type': 'application/json'}
        response = requests.post(URL_WEB_APP, data=json.dumps(payload), headers=headers, timeout=15)
        
        if response.status_code == 200:
            res_json = response.json()
            status_api = res_json.get("status", "unknown")
            
            if status_api == "success":
                print(f"{G}✅ AKSES AKTIF! Selamat bekerja, Bre!{N}\n")
                return True
            elif status_api == "pending":
                print("\n🛑 [TERKUNCI] Token Anda masih berstatus PENDING. Butuh persetujuan Admin.")
                return False
            elif status_api == "registered":
                print("\n🆕 [TERDAFTAR] Perangkat baru otomatis didaftarkan (PENDING). Hubungi Admin.")
                return False
            elif status_api == "expired":
                print("\n🛑 [EXPIRED] Masa aktif Token/Device ID Anda telah habis!")
                return False
        
        # Jika respon tidak standar, gunakan fallback bypass jika token milik boss besar
        if DEVICE_UNIQUE_ID.lower() in ["admin", "pacul_budi"]:
            print(f"{G}✅ BYPASS BOSS BESAR AKTIF! Selamat bekerja, Om Budi!{N}\n")
            return True
            
        print("\n🛑 [GAGAL] Respon validasi dari server Cloud tidak cocok.")
        return False
    except Exception as e:
        if DEVICE_UNIQUE_ID.lower() in ["admin", "pacul_budi"]:
            print(f"{G}⚠️ Server Cloud RTO, Bypass Boss Besar Diaktifkan!{N}\n")
            return True
        print(f"\n❌ Gagal terhubung ke Server Verifikasi: {e}")
        return False

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
    print("🛑 [STOP] Program dihentikan otomatis karena masalah perizinan.")
    sys.exit()

FOLDER_TARGET = cari_folder_ss_otomatis()
file_log = '.terakhir_dikirim.txt'

print('🤖 [START] Bot RoK Auto-Standby AI-Universal Supreme Aktif...')
print(f'🎯 Folder Pantauan: {FOLDER_TARGET}')
print('⏳ Siap siaga! Silakan ambil screenshot tabel SDA di RoK untuk sinkronisasi...\n')

VALID_EXTENSIONS = {'.jpg', '.jpeg', '.png'}

# =========================================================================
# 🔄 MONITORING LOOP RUNTIME (DENGAN SINKRONISASI API PARSING JSON)
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
                    
                    W, H = img.width, img.height
                    
                    # 🎯 FORMULA CROP UNIVERSAL
                    left = int(W * 0.18)
                    top = int(H * 0.05)
                    right = int(W * 0.82)
                    bottom = int(H * 0.92)
                    
                    img_cropped = img.crop((left, top, right, bottom))
                    
                    max_size = 1400
                    if img_cropped.width > max_size:
                        ratio = max_size / float(img_cropped.width)
                        new_height = int(float(img_cropped.height) * float(ratio))
                        img_cropped = img_cropped.resize((max_size, new_height), Image.Resampling.LANCZOS)
                    
                    # 🔥 PROSES PENAJAMAN TEKS TABEL STATISTIK
                    enhancer_kontras = ImageEnhance.Contrast(img_cropped)
                    img_cropped = enhancer_kontras.enhance(1.6)
                    
                    enhancer_tajam = ImageEnhance.Sharpness(img_cropped)
                    img_cropped = enhancer_tajam.enhance(2.5)
                    
                    buffer = BytesIO()
                    img_cropped.save(buffer, format="JPEG", quality=90, optimize=True)
                    nilai_mentah_b64 = buffer.getvalue()
                
                encoded = base64.b64encode(nilai_mentah_b64).decode('utf-8')
                
                payload = {
                    'image': encoded, 
                    'filename': nama_file,
                    'user_id': DEVICE_UNIQUE_ID
                }
                
                print('🚀 Mengirim paket gambar ke Server Cloud API...')
                headers = {'Content-Type': 'application/json'}
                response = requests.post(URL_WEB_APP, data=json.dumps(payload), headers=headers, timeout=30)
                
                if response.status_code == 200:
                    try:
                        res_json = response.json()
                        status_api = res_json.get("status", "unknown")
                        pesan_api = res_json.get("message", "")
                        
                        if status_api == "success":
                            with open(file_log, 'w', encoding='utf-8') as f:
                                f.write(nama_file)
                            
                            data_ext = res_json.get("data_ter_extract", {})
                            print('\n📥 --- 🚀 [SUKSES] DATA MASUK DATABASE CLOUD ---')
                            print(f'💬 Pesan: {pesan_api}')
                            print(f'📍 Koordinat Terdeteksi : {data_ext.get("koordinat", "-")}')
                            print(f'📊 Statistik Extracted  : Makanan={data_ext.get("food","0")}, Kayu={data_ext.get("kayu","0")}, Batu={data_ext.get("stone","0")}, Emas={data_ext.get("emas","0")}')
                            print('-------------------------------------------------')
                            
                            # 🗑️ AUTO-CLEAN GALLERY
                            if os.path.exists(ss_terbaru):
                                os.remove(ss_terbaru)
                                print('🗑️ [AUTO-CLEAN] File fisik dibersihkan dari galeri.')
                                
                        elif status_api == "pending":
                            print('⚠️ [PERINGATAN] Akses Tertunda! Perangkat Anda masih berstatus PENDING di Google Sheet.')
                            print('📢 Silakan hubungi Admin Master untuk diaktifkan aksesnya.')
                            
                        elif status_api == "registered":
                            print('🆕 [PERANGKAT BARU] ID Anda terdaftar otomatis dengan status PENDING.')
                            print('🔒 Mohon hubungi Boss Budi / Admin untuk disetujui.')
                            
                        elif status_api == "expired":
                            print('🛑 [EXPIRED] Lisensi masa aktif token perangkat Anda telah habis!')
                            
                        else:
                            print(f'❓ Respon Server Terbaca: {pesan_api}')
                            
                    except Exception as err_parse:
                        print(f'❌ Gagal melakukan parsing data JSON dari server: {err_parse}')
                        print(response.text)
                else:
                    print(f'❌ Server Mengalami Kendala Respon HTTP: {response.status_code}')
                                        
    except Exception as e:
        print(f'❌ Sistem Mengalami Gangguan: {e}')
        
    time.sleep(5)
