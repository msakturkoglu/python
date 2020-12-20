# program: email.py
# Verilen bir emnail adresinin geçerli olup olmadığını kontrol eder
# Yazar: M. Safa AKTÜRKOĞLU / msakturkoglu@gmail.com / 2020-12-15

def kontrol(str):
  count = 0
  for ch in str:
    if ch == '@':
      count = count + 1
 
  if count == 1:
    return True
  else:
    return False
 
#mail adresini al 
mail=input('Mail : ')

#doğruluğunu kontrol et ve sonucu ekrana bas
if (kontrol(mail)==True):
      print('Mail adresi doğrulandı.')
else:
      print('Lütfen geçerli bir mail adresi giriniz!')

