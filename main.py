import math

# Noktaları içeren liste
points = [(x1, y1), (x2, y2), (x3, y3), ...]  # Noktalarınızı burada tanımlayın

# Öklid mesafesi hesaplama fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point2[0] - point1[0])**2 + (point2[1] - point1[1])**2)

# Mesafeleri saklayacak liste
distances = []

# Her nokta çifti arasındaki mesafeyi hesapla
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        dist = euclideanDistance(points[i], points[j])
        distances.append(dist)

# Minimum mesafeyi bul ve yazdır
min_distance = min(distances)
print("Minimum mesafe:", min_distance)
