# program: url.py
# Verilen bir url adresinin geçerli olup olmadığını kontrol eder
# Yazar: M. Safa AKTÜRKOĞLU / msakturkoglu@gmail.com / 2020-12-15


def url_dogrula(url):
      #girilen adresin uzunluğunu al
      uzunluk = len(url)

      sonek_arr = ["com", "net", "org"] #buraya istenildiği kadar adres soneki eklenebilir
      bSonek = False
      
      #girilen adresin ilk 3 karakterini al
      onek = url[0] + url[1] + url[2]

      #girilen adresin son 3 karakterini al
      sonek = url[uzunluk - 3] + url[uzunluk-2] + url[uzunluk-1]

      #on ek ve son ekteki noktaları al
      ilkNokta = url[3]
      sonNokta = url[uzunluk - 4]

      for s in sonek_arr:
        if (sonek == s):
          bSonek = True

      if (onek == "www" and bSonek and ilkNokta == "." and sonNokta == "."):
        return True
      else:
        return False
        
#url adresini al 
url=input('Url :')

#doğruluğunu kontrol et ve sonucu ekrana bas
if (url_dogrula(url)==True):
  print('Url adresi doğrulandı.')
else:
  print('Lütfen geçerli bir url adresi giriniz!')