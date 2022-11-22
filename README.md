# TUGAS BESAR ALGEO 2
Face Recognition using Eigenface with PCA Algorithm.

> Kelompok (KomukEigen) :
  - Irsyad Nurwidianto Basuki (13521072)
  - Muhammad Zaydan Athallah (13521104)

## Table of Contents
* [General Information](#general-information)
* [Technology Used](#technologies-used)
* [Features](#features)
* [Setup](#setup)
* [Acknowledgements](#acknowledgements)

## General Information
> Program ini dapat mencocokkan gambar wajah seseorang dengan gambar wajah lain (Face Recognition atau Pengenalan Wajah). Face Recognition dalam program ini dibuat dengan menggunakan library OpenCV untuk memproses gambar menjadi matriks. Matriks tersebut akan diproses sedemikian rupa dan nantinya akan dibandingkan dengan matriks gambar lain dengan metode eigenfaces. Program akan menghasilkan hasil gambar termirip dari gambar uji yang diberikan pengguna.

> Garis besar algoritma yang digunakan adalah dengan mereduksi dimensi serta penggunaan konsep aljabar linier untuk mengenali wajah. Dimulai dengan pemrosesan dataset yang besar lalu diolah dengan penggunaan matriks kovarian dan dekomposisi QR untuk mendapatkan nilai eigen & vektor eigen. Selanjutnya adalah pemrosesan eigenfaces yang telah dihasilkan serta mendapatkan weight dari tiap eigenfaces. Untuk face recognition dapat dilakukan dengan perhitungan jarak euclidean.

> Catatan : Program ini tidak akurat 100% sehingga sering kali terjadi ketidakcocokan antara gambar yang diuji dengan hasil gambar termirip.


## Technology Used
Bahasa yang digunakan :
- Python (100%)

Libray yang digunakan : 
- OpenCV
- Numpy
- Os
- Pathlib
- Tkinter
- PIL


## Features
1. Import dataset di GUI
2. Import test image di GUI
3. Output gambar termirip


## Setup
Berikut adalah langkah - langkah penggunaan program :
1. Jalankan gui.py pada terminal (yang terdapat Python3)
2. Tekan tombol "Choose File" dibawah tulisan "INSERT YOUR DATASET" untuk menentukan folder dataset
3. Tekan tombol "Chose File" dibawah tulisan "INSERT YOUR IMAGE" untuk menentukan gambar mana yang ingin diuji
4. Pastikan gambar di "TEST IMAGE" sesuai dengan gambar yang dipilih untuk diuji
5. Tekan tombol "START" untuk memulai pemrosesan gambar
6. Harap menunggu untuk pemrosesan gambar
7. Program akan menghasilkan gambar hasil kecocokan dan durasi pemrosesan gambar.

Note : untuk pengguna macOS diharap untuk mengganti "\\" dengan "/" yang ada pada gui.py


## Acknowledgements
- Terima kasih kepada Tuhan Yang Maha Esa
- Terima kasih kepada para dosen pengampu : Bapak Dr. Judhi S. Santoso, Bapak Dr. Rinaldi Munir, Bapak Dr. Rila Mandala
- Terima kasih kepada Tim Asisten Kuliah IF2123
- Terima kasih kepada teman - teman yang telah membantu
