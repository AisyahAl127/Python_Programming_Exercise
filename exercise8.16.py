#1
import exercise87
album1 = exercise87.album ('Tulus', 'Manusia')
album2 = exercise87.album ('Sheila on 7', 'Kisah Klasik Untuk Masa Depan')
album3 = exercise87.album ('Noah', 'Second Chance', jumlah=12)
print (album1)
print (album2)
print (album3)

#2
from exercise87 import album
album1 = album ('Tulus', 'Manusia')
album2 = album ('Sheila on 7', 'Kisah Klasik Untuk Masa Depan')
album3 = album ('Noah', 'Second Chance', jumlah=12)
print(album1)
print(album2)
print(album3)

#3
from exercise87 import album as al
album1 = al ('Tulus', 'Manusia')
album2 = al ('Sheila on 7', 'Kisah Klasik Untuk Masa Depan')
album3 = al ('Noah', 'Second Chance', jumlah=12)
print(album1)
print(album2)
print(album3\n)

#4
import exercise87 as ex
album1 = ex.album ('Tulus', 'Manusia')
album2 = ex.album ('Sheila on 7', 'Kisah Klasik Untuk Masa Depan')
album3 = ex.album ('Noah', 'Second Chance', jumlah=12)
print(album1)
print(album2)
print(album3\n)

#5
from exercise87 import *