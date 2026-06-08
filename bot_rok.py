import os
import glob
import base64
import json
import subprocess
import time
from config import URL_WEB_APP

def tampilkan_logo():
    G = "\033[0;32m"  # Warna Hijau Cerah
    N = "\033[0m"     # Warna Normal Kembali
    
    logo = f"""
{G}███╗   ███╗██████╗     ██╗  ██╗    ██████╗ ██╗ ██████╗ ██╗████████╗ █████╗ ██╗     
████╗ ████║██╔══██╗    ██║  ██║    ██╔══██╗██║██╔════╝ ██║╚══██╔══╝██╔══██╗██║     
██╔████╔██║██████╔╝    ███████║    ██║  ██║██║██║  ███╗██║   ██║   ███████║██║     
██║╚██╔╝██║██╔══██╗    ██╔══██║    ██║  ██║██║██║   ██║██║   ██║   ██╔══██║██║     
██║ ╚═╝ ██║██║  ██║    ██║  ██║    ██████╔╝██║╚██████╔╝██║   ██║   ██║  ██║███████╗
╚═╝     ╚═╝╚═╝  ╚═╝    ╚═╝  ╚═╝    ╚═════╝ ╚═╝ ╚═════╝ ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝
                                    
                              ✨ ᴹʳ 𝐇 𝐃𝐢𝐠𝐢𝐭𝐚 l ࿐ ✨
                       🤖 AI-Universal Auto-RSS Standby 🤖
==================================================================================={N}
    """
    print(logo)

def verifikasi_user():
    """ Fungsi untuk memvalidasi token akses user ke Google Apps Script Cloud """
    G = "\033[0;32m"  # Hijau
    R = "\033[0;31m"  # Merah
    N = "\033[0m"     # Reset
    
    print(f"{G}🔐 [SECURITY] Sistem Verifikasi Akses Mr H Digital{N}")
    token_input = input("Masukkan Kunci Akses / Token Anda: ").strip()
    
    if not token_input:
        print(f"{R}❌ Token tidak boleh kosong!{N}")
        return False
        
    print("⏳ Memeriksa hak akses ke server Cloud...")
    
    try:
        # Membuat payload verifikasi temporer
        payload_verify = json.dumps({'action': 'verify', 'token': token_input})
        with open('verify_temp.json', 'w', encoding='utf-8') as f:
            f.write(payload_verify)
            
        # Tembak langsung ke Web App GAS kamu
        cmd = ['curl', '-s', '-X', 'POST', '-H', 'Content-Type: application/json', '-d', '@verify_temp.json', URL_WEB_APP]
        response = subprocess.check_output(cmd).decode('utf-8').strip()
        
        # Hapus file sampah verifikasi
        if os.path.exists('verify_temp.json'):
            os.remove('verify_temp.json')
            
        # Cek respon dari Web App kamu
        if "VALID" in response:
            print(f"{G}✅ AKSES DIIZINKAN! Selamat bekerja, Bre!{N}\n")
            return True
        else:
            print(f"{R}❌ AKSES DITOLAK! Token salah atau sudah kedaluwarsa.{N}")
            print(f"{R}   Silakan hubungi Mr H Digital untuk mendapatkan akses.{N}")
            return False
            
    except Exception as e:
        print(f"{R}❌ Gagal terhubung ke server verifikasi: {e}{N}")
        if os.path.exists('verify_temp.json'):
            os.remove('verify_temp.json')
        return False

def cari_folder_ss_otomatis():
    """ Fungsi AI pintar untuk melacak letak folder screenshot di setiap OS Android/Huawei """
    posisi_pencarian = ['/sdcard/DCIM/', '/sdcard/Pictures/', '/sdcard/MyFiles/', '/sdcard/']
    nama_target = ['Screenshots', 'Screenshot', 'TangkapanLayar']
    
    for posisi in posisi_pencarian:
        if os.path.exists(posisi):
            for target in nama_target:
                jalur_cek = os.path.join(posisi, target)
                # Jika folder ditemukan dan valid, langsung kunci jalurnya
                if os.path.exists(jalur_cek) and os.path.isdir(jalur_cek):
                    return jalur_cek + '/*'
                    
    # Opsi cadangan standar jika tidak terdeteksi sama sekali
    return '/sdcard/DCIM/Screenshots/*'

# --- EKSEKUSI UTAMA SAAT BOT PERTAMA NYALA ---
tampilkan_logo()

# Jalankan proteksi verifikasi cloud terlebih dahulu
if not verifikasi_user():
    print("\n🛑 [STOP] Program dihentikan otomatis.")
    exit()

FOLDER_SCREENSHOT = cari_folder_ss_otomatis()
file_log = 'terakhir_dikirim.txt'

print('🤖 [START] Bot RoK Auto-Standby AI-Universal Aktif...')
print(f'🎯 Folder Terdeteksi: {FOLDER_SCREENSHOT.replace("/*", "")}')
print('⏳ Siap siaga! Silakan lakukan screenshot hasil panen di dalam game RoK...\n')

while True:
    try:
        # Kumpulkan semua file dan pastikan membuang sub-folder (seperti folder /Games)
        list_files = [f for f in glob.glob(FOLDER_SCREENSHOT) if os.path.isfile(f)]
            
        if list_files:
            ss_terbaru = max(list_files, key=os.path.getctime)
            nama_file = os.path.basename(ss_terbaru)
            
            last_sent = open(file_log, 'r').read().strip() if os.path.exists(file_log) else ''
            
            if nama_file != last_sent:
                print(f'📸 Menemukan SS Baru: {nama_file}')
                
                with open(ss_terbaru, 'rb') as img:
                    encoded = base64.b64encode(img.read()).decode('utf-8')
                
                payload = json.dumps({'image': encoded, 'filename': nama_file})
                
                with open('payload_temp.json', 'w', encoding='utf-8') as f:
                    f.write(payload)
                
                print('🚀 Mengirim otomatis ke Cloud...')
                
                cmd = ['curl', '-s', '-X', 'POST', '-H', 'Content-Type: application/json', '-d', '@payload_temp.json', URL_WEB_APP]
                subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                
                with open(file_log, 'w') as f:
                    f.write(nama_file)
                
                if os.path.exists('payload_temp.json'):
                    os.remove('payload_temp.json')
                
                print('✅ Sukses Terkirim')
                
    except Exception as e:
        print(f'❌ Eror: {e}')
        
    time.sleep(3)
