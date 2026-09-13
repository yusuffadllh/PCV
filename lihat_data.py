# %%
# FILE KHUSUS TAMPILAN: lihat data mentah di Variables panel
# jalankan sel ini dulu, lalu klik variabel di panel Variables

import cv2

IMG_PATH = r"e:\Project\PCV\P1\WhatsApp Image 2026-09-08 at 7.49.33 AM.jpeg"
img = cv2.imread(IMG_PATH)

# %%
# potongan kecil biar gampang dibaca mentahnya di Variables
potongan = img[:8, :8]          # 8x8 piksel pojok kiri atas (3 kanal)
potongan_b = img[:8, :8, 0]     # cuma kanal biru
potongan_g = img[:8, :8, 1]     # cuma kanal hijau
potongan_r = img[:8, :8, 2]     # cuma kanal merah

# info dasar sesuai contoh dosen
imgtype = img.dtype
(h, w, c) = img.shape

# statistik dasar
stat = {
    "shape": img.shape,
    "dtype": str(img.dtype),
    "min": int(img.min()),
    "max": int(img.max()),
    "mean": round(float(img.mean()), 2),
}
stat
