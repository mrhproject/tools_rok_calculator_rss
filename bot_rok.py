import os
import base64
import json
import time
import uuid
import sys
import gc  # ⚡ Engine pembersih RAM otomatis
from io import BytesIO

# ⚡ VALIDASI DEPENDENSI UTAMA
try:
    import requests
    from PIL import Image
except ImportError:
    print("⏳ Menyiapkan library tambahan (requests & pillow)...")
    os.system('pkg install libjpeg-turbo-dev zlib-dev -y &> /dev/null')
    os.system('pip install requests pillow &> /dev/null')
    import requests
    from PIL import Image

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
                if device_id: return device_id
        except:
            pass

    id_acak = str(uuid.uuid4()).replace('-', '')[:12].upper() 
    device_id = f"MRH-{id_acak}"
    with open(nama_file_id, 'w', encoding='utf-8') as f:
        f.write(device_id)
    return device_id

DEVICE_UNIQUE_ID = dapatkan_device_id_permanen()
# =========================================================================

def tampilkan_logo():
    G = "\033[0;32m"  # Hijau Cerah
    Y = "\033[0;33m"  # Kuning Cerah
    N = "\033[0m"     # Normal
    
    logo = f"""
{G}███╗   ███╗██████╗     ██╗  ██╗    ██████╗ ██╗ ██████╗ ██╗████████╗ █████╗ ██╗     
████╗ ████║██╔══██╗    ██║  ██║    ██╔══██╗██║██╔════╝ ██║╚══██╔══╝██╔══██╗██║     
██╔████╔██║██████╔╝    ███████║    ██║  ██║██║██║  ███╗██║   ██║   ███████║██║     
██║╚██╔╝██║██╔══██╗    ██╔══██║    ██║  ██║██║██║   ██║██║   ██║   ██╔══██║██║     
██║ ╚═╝ ██║██║  ██║    ██║  ██║    ██████╔╝██║╚██████╔╝██║   ██║   ██║  ██║███████╗
╚═╝     ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝    ╚═════╝ ╚═╝ ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝{N}
                                    
                              ✨ ᴹʳ 𝐇 𝐃𝐢𝐠𝐢𝐭𝐚 l ࿐ ✨
                           🤖 AI-Universal Auto-RSS Standby 🤖
                    [MODE: BYPASS STORAGE + AUTO-FILTER LANDSCAPE]
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

# --- INITIALIZATION ---
tampilkan_logo()

if not verifikasi_user():
    print("\n🛑 [STOP] Program dihentikan otomatis.")
    sys.exit()

FOLDER_TARGET = cari_folder_ss_otomatis()
file_log = '.terakhir_dikirim.txt'

print('🤖 [START] Bot RoK Auto-Standby AI-Universal Supreme Aktif...')
print(f'🎯 Folder Pantauan Utama: {FOLDER_TARGET}')
print('⏳ Siap siaga! Cukup lakukan screenshot di game RoK, data meluncur otomatis...\n')

while True:
    try:
        list_files = []
        # 🚀 BYPASS SCOPED STORAGE: Ambil data real-time pake command 'ls' Linux
        folder_alt = FOLDER_TARGET.replace("DCIM", "Pictures") if "DCIM" in FOLDER_TARGET else FOLDER_TARGET.replace("Pictures", "DCIM")
        
        for folder in [FOLDER_TARGET, folder_alt]:
            if os.path.exists(folder):
                cmd = f"ls -1 {folder} 2>/dev/null"
                with os.popen(cmd) as stream:
                    files = stream.read().splitlines()
                for f in files:
                    if f.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                        list_files.append(os.path.join(folder, f))
            
        if list_files:
            ss_terbaru = max(list_files, key=os.path.getmtime)
            nama_file = os.path.basename(ss_terbaru)
            
            # Saringan 1: Validasi file size sampah (minimal 20 KB)
            if os.path.exists(ss_terbaru) and os.path.getsize(ss_terbaru) < 20480:
                try:
                    os.remove(ss_terbaru)
                    continue
                except:
                    pass

            last_sent = ''
            if os.path.exists(file_log):
                with open(file_log, 'r', encoding='utf-8') as f:
                    last_sent = f.read().strip()
            
            if nama_file != last_sent:
                print(f'📸 Terdeteksi SS Baru: {nama_file}')
                
                # Saringan 2: Pastikan file selesai ditulis penuh ke storage oleh HP (Anti-0KB)
                ukuran_lama = -1
                percobaan = 0
                while percobaan < 5:
                    try:
                        ukuran_baru = os.path.getsize(ss_terbaru)
                        if ukuran_baru > 0 and ukuran_baru == ukuran_lama: break
                        ukuran_lama = ukuran_baru
                    except: pass
                    time.sleep(0.5)
                    percobaan += 1
                
                print('⚡ Menjalankan Engine Kompresi Gambar MRH Digital (RAM Mode)...')
                
                # Buka gambar untuk divalidasi posisinya
                is_valid_landscape = True
                with Image.open(ss_terbaru) as img:
                    # 🚨 Saringan 3: FILTER LANDSCAPE ONLY (Tembok Pengaman Chat WA / Foto Portrait)
                    if img.height > img.width:
                        print(f"⚠️ [ABORT] {nama_file} terdeteksi Gambar Portrait (Bukan Game RoK). Langsung Skip & Sapu!")
                        is_valid_landscape = False
                    else:
                        # Jika lolos sensor landscape, lakukan proses kompresi RAM
                        if img.mode in ("RGBA", "P"):
                            img = img.convert("RGB")
                        
                        max_size = 1280
                        if img.width > max_size:
                            ratio = max_size / float(img.width)
                            new_height = int(float(img.height) * float(ratio))
                            img = img.resize((max_size, new_height), Image.Resampling.LANCZOS)
                        
                        buffer = BytesIO()
                        img.save(buffer, format="JPEG", quality=75, optimize=True)
                        nilai_mentah_b64 = buffer.getvalue()

                # Eksekusi aksi jika file terbukti gambar Portrait (Sampah)
                if not is_valid_landscape:
                    try:
                        with open(file_log, 'w', encoding='utf-8') as f: f.write(nama_file)
                        if os.path.exists(ss_terbaru): os.remove(ss_terbaru)
                    except: pass
                    continue # Langsung lompat nyari screenshot game yang asli

                encoded = base64.b64encode(nilai_mentah_b64).decode('utf-8')
                payload = {'image': encoded, 'filename': nama_file, 'user_id': DEVICE_UNIQUE_ID}
                
                print('🚀 Mentransfer paket data mini ke Cloud Server...')
                headers = {'Content-Type': 'application/json'}
                
                # RE-TRY MECHANISM: Mengatasi sinyal naik-turun di lapangan (3x Coba)
                sukses_kirim = False
                for i in range(3):
                    try:
                        response = requests.post(URL_WEB_APP, data=json.dumps(payload), headers=headers, timeout=25)
                        if response.status_code == 200:
                            sukses_kirim = True
                            break
                    except:
                        print(f'⚠️ Kendala Jaringan (Percobaan {i+1}/3): Tunda 2 detik...')
                        time.sleep(2)
                
                if sukses_kirim:
                    with open(file_log, 'w', encoding='utf-8') as f:
                        f.write(nama_file)
                    print('✅ Transaksi Sukses! Data masuk Database.')
                    
                    try:
                        if os.path.exists(ss_terbaru):
                            os.remove(ss_terbaru)
                            print(f'🗑️ [AUTO-CLEAN] Berhasil menghapus file fisik sampah dari galeri.')
                    except Exception as err_del:
                        print(f'⚠️ Gagal menghapus file fisik: {err_del}')
                else:
                    print(f'❌ Server Gagal Merespon setelah 3 kali percobaan.')
                    
                # Bebaskan RAM
                del nilai_mentah_b64, encoded, payload
                gc.collect()
                                
    except Exception as e:
        print(f'❌ Sistem Mengalami Gangguan: {e}')
        if "cannot identify image file" in str(e) and 'ss_terbaru' in locals():
            try:
                with open(file_log, 'w', encoding='utf-8') as f: f.write(nama_file)
                if os.path.exists(ss_terbaru): os.remove(ss_terbaru)
                print("🚨 [BYPASS] Berkas rusak disapu dari antrean!")
            except: pass
        
    time.sleep(3)
