# program: arama.py
# Girilen bir string ifadede aranan bir ifade bulunduğunda bir  ̈onceki ve bir sonraki karakteri ekrana getirir.
# Yazar: M. Safa AKTÜRKOĞLU / msakturkoglu@gmail.com / 2020-12-15


def ara(str, aranan):
  if len(aranan) > len(str):
    return "Aranan değer çok uzun!"
  #eğer girilen metin ile aranan değer aynı ise girilen metni döndür!
  elif str == aranan:
    return str
  
  sonuc = str.find(aranan)
  if (sonuc == -1):
    return "Aranan ifade string içerisinde bulunamadı!"
  karakter1 = str[sonuc -1]
  karakter2 = str[sonuc+len(aranan)]

  return karakter1 + aranan + karakter2
    
    


metin = input("Metin giriniz:")
aranan = input("Aranan:")
print(ara(metin, aranan))