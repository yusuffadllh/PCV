# PCV

Tugas mata kuliah Pengolahan Citra Digital (PCV).

## Isi Repo

- `P1/Intro-1.py` — filter warna gambar & video real-time (webcam)

## Cara Pakai

Install library dulu:

```
pip install opencv-python
```

Jalankan:

```
python P1/Intro-1.py
```

## Yang Dipelajari

- Baca gambar dengan `cv2.imread`
- Cek `dtype` dan `shape` gambar (tinggi, lebar, kanal)
- Manipulasi piksel manual pakai loop `for`
- Filter warna (matiin kanal hijau & biru, sisain merah)
- Akses webcam & filter real-time dengan `cv2.VideoCapture`

