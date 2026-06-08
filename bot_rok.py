import os
import glob
import base64
import json
import subprocess
import time
from config import URL_WEB_APP

# Daftar jalur folder screenshot universal di Android & Huawei
JALUR_SS = [
    '/sdcard/DCIM/Screenshots/*',
    '/sdcard/Pictures/Screenshots/*'
]
file_log = 'terakhir_dikirim.txt'

print('🤖 [START] Bot RoK Auto-Standby Multi-Device Aktif...')
print('💡 Bot otomatis mendeteksi folder SS internal perangkat.')

while True:
    try:
        # Kumpulkan semua file dari berbagai jalur folder
        list_files = []
        for jalur in JALUR_SS:
            list_files.extend(glob.glob(jalur))
            
        if list_files:
            # Cari yang paling baru di antara semua folder
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
