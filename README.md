# Convex Hull 

Tugas Kecil 2 IF2211 Strategi Algoritma Semester II Tahun 2021/2022

Implementasi Convex Hull untuk Visualisasi Tes _Linear Separability_ Dataset dengan Algoritma _Divide and Conquer_ 

## Table of Contents
* [General Information](#general-information)
* [Requirement and Installation](#requirement-and-installation)
* [How to Run](#how-to-run)
* [Author](#author)

## General Information
Sebuah pustaka sederhana untuk menghasilkan _convex hull_ dari kumpulan data 2 dimensi dengan menggunakan strategi _divide and conquer_. Contoh penggunaan dari pustaka ini dapat dilihat pada file main.py di folder ```src```

## Requirement and Installation

  - Download dan Install <a href="http://www.python.org/downloads/">Python 3</a>
  - Tambahkan Python dan pip ke PATH environment variable. Berikut adalah _guide_ yang dapat diikuti:
    - https://www.geeksforgeeks.org/pythonpath-environment-variable-in-python/
    - https://stackoverflow.com/questions/23708898/pip-is-not-recognized-as-an-internal-or-external-command
  - Clone repository ini 
  - Install modul yang dibutuhkan dengan mengetikkan command ini pada root folder repository
    ```
    pip install -r requirements.txt
    ```
## How to Run
Ketikkan perintah ini pada root directory repository ini
```
python src/main.py
```
Program akan memiliki tampilan sebagai berikut

```
Daftar Dataset
1. Dataset iris
2. Dataset wine
3. Dataset breast cancer
Pilih Dataset yang ingin digunakan : _
```
Ketikkan angka sesuai dengan dataset yang ingin digunakan, misalkan 1 untuk menggunakan dataset iris
```
Daftar atribut:
1 sepal length (cm)
2 sepal width (cm)
3 petal length (cm)
4 petal width (cm)
atribut-x yang ingin digunakan : _
```
Ketikkan pilihan untuk atribut pada sumbu x, misalkan 1 untuk sepal length (cm
```
Daftar atribut:
1 sepal length (cm)
2 sepal width (cm)
3 petal length (cm)
4 petal width (cm)
atribut-x yang ingin digunakan : 1
atribut-y yang ingin digunakan : _
```
Ketikkan pilihan untuk atribut pada sumbu y, pastikan pilihan berbeda dengan atribut x

Program akan menampilkan graph yang menunjukkan poligon yang dibentuk dari _convex hull_
![output](![image](https://user-images.githubusercontent.com/73408389/155894330-953522a1-078a-4770-b105-df8ad4f34925.png)

## Author
<a href="http://github.com/SurTan02">Suryanto (13520059)</a> 
