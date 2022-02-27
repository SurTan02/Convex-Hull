import numpy as np

def angle(p1,p2,p3):
    '''
        Fungsi untuk mencari sudut yang p213
    '''
    p1 = np.array(p1)
    p2 = np.array(p2)
    p3 = np.array(p3)

    p12 = p1 - p2
    p13 = p1 - p3

    cosine_angle = np.dot(p12, p13) / (np.linalg.norm(p12) * np.linalg.norm(p13))
    angle = np.arccos(cosine_angle)
    return angle

def distpoint(p1,p2):
    '''
        Fungsi untuk mencari jarak antara 2 titik
    '''
    x = p2[0] - p1[0]
    y = p2[1] - p1[1]    
    return (x*x + y*y)**0.5 

def dist(p1,p2,p3):
    '''
        Fungsi untuk mencari jarak suatu titik (p3) terhadap 
        garis yang dibentuk oleh titik p1 dan p2
    '''
    a = p2[0] - p1[0]           #x2 - x1
    b = p1[1] - p3[1]           #y1 - y3
    c = p1[0] - p3[0]           #x1 - x3
    d = p2[1] - p1[1]           #y2 - y1
    return abs(a*b - c*d) / distpoint(p1,p2) 

def determinan(p1, p2, p3):
    '''
        Fungsi untuk penentuan determinan. Digunakan untuk mengecek
        posisi titik p3 terhadap garis yang dibentuk titik p1 dan p2.
    '''
    return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])

# 
def quickhull(arr):
    '''
        Fungsi utama untuk mencari convex hull.
    '''
    hull = []
    
    # Mencari titik dengan absis minimum dan maksimum. 
    sort=sorted(arr,key=lambda x:x[0])
    p1=sort[0]
    p2=sort[-1]

    # Memanggil fungsi quickhullPartition
    # Dipanggil dua kali untuk mencari solusi dibawah dan diatas garis.
    hull += quickhullPartition(arr, p1, p2)
    hull += quickhullPartition(arr, p2, p1)
    
    return hull

def quickhullPartition(arr, p1, p2):
    '''
        Implementasi Algoritma Divide and Conquer 
        untuk menghasilkan convex hull
    '''

    # Divide, dengan hanya mengambil titik di sebelah kiri garis
    # Jika absis p2 > p1, maka bagian sebelah kiri == bagian atas garis
    # Jika absis p1 > p2, maka bagian sebelah kiri == bagian bawah garis
    # Titik di sebelah kanan tidak diproses karena tidak mungkin membentuk convex hull
    El_point = []
    for point in arr:
        if (determinan(p1, p2, point) >0):
            El_point.append(point)
    # Points = [point for point in arr if determinan(p1, p2, point) >0]

    # Mencari titik terjauh terhadap garis yang dibentuk p1 dan p2
    pmax = None
    maxDist = 0
    maxAngle = 0
    for point in El_point:
        tempDist = dist(p1, p2,point)
        if  tempDist >= maxDist:
            maxDist = tempDist
            pmax = point
        elif tempDist == maxDist:
            tempAngle = angle(p1,p2,point)
            if (tempAngle > maxAngle):
                maxAngle = tempAngle
                pmax = point 

    if pmax == None:
        return [p2]
    hull = []
    
    # Bagian Conquer, Rekursi 
    # Dipanggil dua kali untuk mencari solusi di sebelah kiri p1-pmax dan
    # di sebelah kiri pmax-p2 
    hull += quickhullPartition(El_point, p1, pmax)
    hull += quickhullPartition(El_point, pmax, p2)
    return hull