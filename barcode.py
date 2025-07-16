import qrcode
import os

# Link Google Drive
link_gdrive = "https://drive.google.com/drive/u/2/folders/1oyvx00DqyAyGX_gt3W8buLEptcnuLDsC"

# Nama file
filename = "TF IDF.png"

# Path folder tujuan (ganti dengan folder yang kamu inginkan)
folder_tujuan = "D:\Codex.Project\Project SKRIPSI\C2\Barcode"

# Gabungkan path folder + nama file
full_path = os.path.join(folder_tujuan, filename)

# Buat QR code dan simpan
qr = qrcode.make(link_gdrive)
qr.save(full_path)

print(f"QR code berhasil disimpan di: {full_path}")