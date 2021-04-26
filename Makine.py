# Bu basit bir hesap makinesi programıdır.
# Daha fazla referans için dm belirtebilirsiniz

import time
import colorama
from colorama import Fore, Back, Style
colorama.init()

def toplama():
  print(Fore.GREEN)
  print("Toplama sonucu: ", sayi1+sayi2)
  time.sleep(2.0)

def carpma():
  print(Fore.GREEN)
  print("Çarpmanın sonucu: ", sayi1 * sayi2)
  time.sleep(2.0)

def cikarma():
  print(Fore.GREEN)
  print("Çıkarmanın sonucu: ", sayi1-sayi2)
  time.sleep(2.0)

def bolme():
  print(Fore.GREEN)
  print("Bölmenin sonucu: ", sayi1/sayi2)

print(Fore.WHITE)
print("Sisteme giriş yapılıyor..")
time.sleep(4.0)
print("Sisteme giriş yapıldı.")
while True:
  print(Fore.WHITE)
  print("Lütfen işlem seçiniz.")
  print(Fore.CYAN+"[1] Toplama \n[2] Çarpma \n[3] Çıkarma \n[4] Bölme \n[5] Çıkış")
  print(Fore.WHITE)
  secim = input("--:")
  if int(secim)>0 and int(secim)<6:
    if secim == "1":
      print(Fore.LIGHTRED_EX)
      sayi1 = int(input("İlk sayıyı giriniz: "))
      sayi2 = int(input("İkinci sayıyı giriniz: "))
      toplama()
    elif secim == "2":
      print(Fore.LIGHTRED_EX)
      sayi1 = int(input("İlk sayıyı giriniz: "))
      sayi2 = int(input("İkinci sayıyı giriniz: "))
      carpma()

    elif secim == "3":
      print(Fore.LIGHTRED_EX)
      sayi1 = int(input("Büyük sayıyı giriniz: "))
      sayi2 = int(input("Küçük sayıyı giriniz: "))
      cikarma()
    elif secim == "4":
      print(Fore.LIGHTRED_EX)
      sayi1 = int(input("Büyük sayıyı giriniz: "))
      sayi2 = int(input("Küçük sayıyı giriniz: "))
      bolme()
    elif secim=="5":
      print(Back.WHITE+Fore.BLACK+"Çıkış yapılıyor..")
      time.sleep(2.0)
      break

  else:
    print(Back.RED)
    print("Lütfen eşleşen sayıları seçin!")
    print(Back.RESET)
