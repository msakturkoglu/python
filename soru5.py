# program: soru5.py
# Bir veya birden fazla girilen komut(ları) işleyerek belirli cihazları aç/kapa yapar.
# Yazar: M. Safa AKTÜRKOĞLU / msakturkoglu@gmail.com / 2020-12-15

# receive-23-1-0\n
# send-181-3-0-1\nreceive-170-3-0\n
# receive-150-0-1\n0-4-5-6-\n
import enum

# komutlarımız için sabit bir enum list oluşturuyoruz. Bu kod içersinde hata yapmamızı engeller ve
# kodun yeniden bakımını (refactoring) kolaylaştırır!
class KomutSeti(enum.Enum):
  SEND = "send"
  RECEIVE = "receive"

  def __str__(self):
    return self.name

# Bu fonksiyon parametre olarak int tipinde bir değer alır ve aldığı göre bir cihaz ismi döndürür. 
# Eğer listenin dışında bir değer girilmiş ise -1 (hata) döndürür.
def CihazStr(i):
  switcher={
    1: 'Televizyon',
    2: 'Çamaşır Makinesi',
    3: 'Buzdolabı',
    4: 'Fırın'
  }
  return switcher.get(i,-1)


def SinyalStr(sinyal):
  if (sinyal >= 0 and sinyal <= 50):
    return "Çok Zayıf"
  elif (sinyal > 50 and sinyal <= 100):
    return "Zayıf"
  elif (sinyal > 100 and sinyal <= 150):
    return "Orta"
  elif (sinyal > 150 and sinyal <= 200):
    return "Güçlü"
  elif (sinyal > 200 and sinyal <= 255):
    return "Çok Güçlü"
  else :
    return -1

def komutIslet(paket):

  paket_arr = paket.split("-")
  
  #Paket sonu karakterini kontrol et
  paketSonu = "\n" in paket_arr[-1]

  komut = paket_arr[0]
  hata = "Hatalı komut: "
  # Gelen paketin komut tipine ve paket sonuna bakıyoruz.
  # Bizim istediğimiz değerler ile uyuşuyorsa paketi ayrıştırmaya başlıyoruz.
  # Eğer komut tipi veya paket sonu bizim komut yapımıza uygun değilse hata mesajı döndürüyoruz!  
  if not (komut == KomutSeti.RECEIVE.value or komut == KomutSeti.SEND.value):
    return hata + "'send' ya da 'receive' içermiyor!"
  elif (paketSonu != True):
    return hata + "paket sonu hatası!"

    #komutun send veya receive olma durumuna göre kaç parametre olması gerektiğini belirliyoruz
    #receive: komutun kendisi + 3 parametre = uzunluk 4
    #send: komutun kendisi + 4 parametre = uzunluk 5
  paketLen = 4 if komut == KomutSeti.RECEIVE.value else 5

  if  (len(paket_arr) != paketLen):
    return "Parametre sayısı hatalı!"
      
  sinyalGucu = int(paket_arr[1])
  sinyal_str = SinyalStr(sinyalGucu)

  if (sinyal_str == -1):
    return "Sinyal değeri aralık dışında!"
    
  cihaz = int(paket_arr[2])
  cihaz_str = CihazStr(cihaz)

  if (cihaz_str == -1):
    return "Tanımsız cihaz!"
    
  durum = int(paket_arr[3].splitlines()[0])
    
  if not (durum == 0 or durum == 1): 
    print("durum:", durum)
    return "Geçersiz cihaz durumu!"

    #eğer komut send komutu ise cevap istenip istenmediği kontrol et
  cevapStr = ''
  if (komut == KomutSeti.SEND.value):
    cevap = int(paket_arr[4].splitlines()[0])
    #eğer cevap 1' e eşit değilse (0 veya farklı bir değer) cevap istenmediğini varsayıyoruz.
    cevapStr = "Cevap: "+ ("1 - İsteniyor\n" if (cevap == 1) else "0 - İstenmiyor\n")

  print("--------------------------------------------------------------------------\n"+
    "Kod Tipi: " + komut + " - " + ("Gelen\n" if (komut == KomutSeti.RECEIVE.value) else "Giden\n") +
    "Sinyal Gucu: " + str(sinyalGucu) + " - " + sinyal_str + "\n"+
    "Cihaz: "+ str(cihaz) + " - " + cihaz_str +"\n"+
    "Durumu: "+ str(durum) + " - " + ("On\n" if (durum == 1) else "Off\n") +
    cevapStr +
    "--------------------------------------------------------------------------\n"
  )
  return True

#Kullanıcıdan komut girmesini istiyoruz:  
_input = input("Komut giriniz:")   

#Girilen string içerisindeki \n ifadelerini satırsonu (newline) karakterine çeviriyoruz ve birden fazla komut olabileceği için komutları bir diziye dönüştürüyoruz
komutListesi = _input.replace("\\n","\n").splitlines(True)

count = 1
#Dizideki komutları işletiyoruz
for komut in komutListesi:
  print("Komut "+str(count)+"/" + str(len(komutListesi))+":")
  res = komutIslet(komut)
  if (res != True):
    print(res)
  count += 1