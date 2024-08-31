import math  

# 1. Noktaların Tanımlanması
points = [(1, 2), (4, 6), (5, 8), (3, 4), (7, 1)] 

# 2. Öklid Mesafesi İçin Bir Fonksiyon Yazma
def hesaplaMesafe(nokta1, nokta2):
    x1, y1 = nokta1  
    x2, y2 = nokta2  
    
    # Mesafe formülünü uyguluyoruz
    mesafe = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    return mesafe  

# 3. Mesafelerin Hesaplanması
mesafeler = []  
for i in range(len(points)):  
    for j in range(i + 1, len(points)):  
        mesafe = hesaplaMesafe(points[i], points[j])  
        mesafeler.append(mesafe)  

# 4. Minimum Mesafenin Bulunması
en_kucuk_mesafe = min(mesafeler)  
print('En küçük mesafe:', en_kucuk_mesafe)  