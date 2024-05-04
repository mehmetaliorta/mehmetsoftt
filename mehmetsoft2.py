print("hoş geldin")
while True:
    print("giriş için g")
    print("kayıt için k")
    print("çıkış için ç")

    secim=input("ne yapmak istersiniz")

    if secim == "k":
        ki=input("isim gir")
        kş=input("şifre gir")
        if len(kş)>= 8:
            print("kayıt başarılı")

        else:
            print("şifre en az `8` karakter olmalı>!")

    if  secim == "g":
        gi=input("ism gir ")
        gş=input ("şifre gir")
        if ki == gi and kş == gş:
            print("giriş başarılı")

            s=input("ne yapmak istersiniz oyun `o` için hesap makinası için `h` ye bas")
            if s == "o":
                while True:
                    print("kelimeler = elma ,armut, çilek , kiraz , portakal")
                    import random
                    kelimeler = ["elma","armut","çilek","kiraz","portakal"]
                    secilenkelime = random.choice(kelimeler)
                    while True:
                        tahminhakkı = 5
                        t=input("tahmin gir yada baştan başla :")
                        if t == "b":
                            break
                        if secilenkelime == t :
                            print("tahmin doru",secilenkelime)
                            break
                        else:
                            print("yanlış tahmin tekrar dene")
                    
                    
            if s == "h":
                while True:
                    print("+")
                    print("-")
                    print("*")
                    print("/")
                    print("g")
                    secim2=input("ne yapmak istersiniz :")
                    if secim2 == "g":
                        print("çıkış yapılıyor")
                        break
                    sayı1=int(input("sayı gir :"))
                    sayı2=int(input("sayı gir :"))
                    if secim2 == "+":
                        print(sayı1+sayı2)
                        continue
                    if secim2 == "-":
                        print(sayı1-sayı2)
                        continue
                    if secim2 == "*":
                        print(sayı1*sayı2)
                        continue
                    if secim2 == "/":
                        print(sayı1/sayı2)
                        continue
                
                    
        else:
            input("yanlış şıfre veya kullanıcı adı tekrar dene")

    if secim == "ç":
        break
    
    
        
