import os
import glob
import base64
import json
import subprocess
import time
from config import URL_WEB_APP

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

# Eksekusi pencarian otomatis saat bot pertama kali dijalankan
FOLDER_SCREENSHOT = cari_folder_ss_otomatis()
file_log = 'terakhir_dikirim.txt'

print('🤖 [START] Bot RoK Auto-Standby AI-Universal Aktif...')
print(f'🎯 Folder Terdeteksi: {FOLDER_SCREENSHOT.replace("/*", "")}')

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
