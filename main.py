# Fibonacci dizisini hesaplayan ve sonucu belirli bir sınıra kadar sayı
#  içeren bir liste olarak döndüren bir döngü nasıl oluşturulur?

sinir = int(input("Sınır Sayısını Giriniz : "))
fibo_listesi = [0,1]

for i in range(1,sinir):
    yeni_sayi = fibo_listesi[-1]+fibo_listesi[-2]
    if yeni_sayi > sinir:
        break
    fibo_listesi.append(yeni_sayi)

print(fibo_listesi)
