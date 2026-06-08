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
    """ Fungsi Validasi Token Akses - Kebal Terhadap Eror Redirect 405 Google """
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
        payload_verify = json.dumps({'action': 'verify', 'token': token_input})
        with open('verify_temp.json', 'w', encoding='utf-8') as f:
            f.write(payload_verify)
            
        # 🔥 SAKTI UTAMA: Ditambah '--post302' agar curl patuh mengubah metode ke GET saat diredirect oleh Google!
        cmd = ['curl', '-s', '-L', '--post302', '-H', 'Content-Type: application/json', '-d', '@verify_temp.json', URL_WEB_APP]
        raw_response = subprocess.check_output(cmd).decode('utf-8')
        
        response = raw_response.strip().upper()
        
        if os.path.exists('verify_temp.json'):
            os.remove('verify_temp.json')
            
        if "VALID" in response:
            print(f"{G}✅ AKSES DIIZINKAN! Selamat bekerja, Bre!{N}\n")
            return True
        elif "EXPIRED" in response:
            print(f"{R}❌ PAKET HABIS! Masa aktif token Anda telah kedaluwarsa.{N}")
            return False
        else:
            print(f"{R}❌ AKSES DITOLAK! Token salah atau tidak terdaftar.{N}")
            return False
            
    except Exception as e:
        print(f"{R}❌ Gagal terhubung ke server verifikasi: {e}{N}")
        if os.path.exists('verify_temp.json'):
            os.remove('verify_temp.json')
        return False

def cari_folder_ss_otomatis():
    posisi_pencarian = ['/sdcard/DCIM/', '/sdcard/Pictures/', '/sdcard/MyFiles/', '/sdcard/']
    nama_target = ['Screenshots', 'Screenshot', 'TangkapanLayar']
    for posisi in posisi_pencarian:
        if os.path.exists(posisi):
            for target in nama_target:
                jalur_cek = os.path.join(posisi, target)
                if os.path.exists(jalur_cek) and os.path.isdir(jalur_cek):
                    return jalur_cek + '/*'
    return '/sdcard/DCIM/Screenshots/*'

# --- EKSEKUSI UTAMA SAAT BOT PERTAMA NYALA ---
tampilkan_logo()

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
                
                # 🔥 SAKTI JUGA: Pasang '--post302' di pengiriman gambar agar kiriman OCR aman terkendali
                cmd = ['curl', '-s', '-L', '--post302', '-H', 'Content-Type: application/json', '-d', '@payload_temp.json', URL_WEB_APP]
                subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                
                with open(file_log, 'w') as f:
                    f.write(nama_file)
                if os.path.exists('payload_temp.json'):
                    os.remove('payload_temp.json')
                print('✅ Sukses Terkirim')
    except Exception as e:
        print(f'❌ Eror: {e}')
    time.sleep(3)
