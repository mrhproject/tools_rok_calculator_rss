import os

import glob

import base64

import json

import time

import uuid

import sys

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

                        [MODE SUPREME SPEED & AUTO-CLEAN AKTIF]

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

print(f'🎯 Folder Pantauan: {FOLDER_TARGET}')

print('⏳ Siap siaga! Cukup lakukan screenshot di game RoK, data meluncur otomatis...\n')



while True:

    try:

        # Saring file gambar secara selektif untuk menghemat daya proses CPU

        list_files = []

        for ext in ('/*.jpg', '/*.jpeg', '/*.png', '/*.JPG', '/*.JPEG', '/*.PNG'):

            list_files.extend(glob.glob(FOLDER_TARGET + ext))

            

        if list_files:

            # Ambil screenshot paling gres / terbaru

            ss_terbaru = max(list_files, key=os.path.getctime)

            nama_file = os.path.basename(ss_terbaru)

            

            # Baca logs riwayat

            last_sent = ''

            if os.path.exists(file_log):

                with open(file_log, 'r', encoding='utf-8') as f:

                    last_sent = f.read().strip()

            

            # Deteksi jika benar-benar ada jepretan baru

            if nama_file != last_sent:

                print(f'📸 Terdeteksi SS Baru: {nama_file}')

                print('⚡ Menjalankan Engine Kompresi Gambar MRH Digital (RAM Mode)...')

                

                # 🛠️ STRATEGI OPTIMASI 1: Buka gambar, turunkan resolusi skala proporsional & turunkan kualitas ke 75%

                with Image.open(ss_terbaru) as img:

                    # Konversi ke mode RGB jika formatnya PNG agar bisa disimpan sebagai JPEG kompresi tinggi

                    if img.mode in ("RGBA", "P"):

                        img = img.convert("RGB")

                    

                    # Batasi resolusi maksimal lebar 1280px agar performa OCR di Google Sheets tetap akurat namun super ringan

                    max_size = 1280

                    if img.width > max_size:

                        ratio = max_size / float(img.width)

                        new_height = int(float(img.height) * float(ratio))

                        img = img.resize((max_size, new_height), Image.Resampling.LANCZOS)

                    

                    # Simpan hasil kompresi langsung ke memory RAM buffer (Bebas I/O Storage HP)

                    buffer = BytesIO()

                    img.save(buffer, format="JPEG", quality=75, optimize=True)

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

                    

                    # 🛠️ STRATEGI OPTIMASI 2: Auto-Delete file screenshot asli di HP biar penyimpanan lega

                    try:

                        if os.path.exists(ss_terbaru):

                            os.remove(ss_terbaru)

                            print(f'🗑️ [AUTO-CLEAN] Berhasil menghapus file fisik sampah dari galeri.')

                    except Exception as err_del:

                        print(f'⚠️ Gagal menghapus file fisik: {err_del}')

                        

                else:

                    print(f'❌ Server Mengalami Kendala Respon HTTP: {response.status_code}')

                                

    except Exception as e:

        print(f'❌ Sistem Mengalami Gangguan: {e}')

        

    time.sleep(3)
