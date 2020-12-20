# program: arama.py
# Üç basamaklı rakamları birbirinden farklı kaç tane sayı olduğunu bularak ekrana yazdırır.
# Yazar: M. Safa AKTÜRKOĞLU / msakturkoglu@gmail.com / 2020-12-15

def say():
  sayac = 0

  for i in range(1, 9):
    for j in range(0, 9):
      for k in (0,9):
        if ( i != j and i != k and j != k ):
          sayac += 1
          print(i,j,k)

  print("Sayac: ", sayac)


say()