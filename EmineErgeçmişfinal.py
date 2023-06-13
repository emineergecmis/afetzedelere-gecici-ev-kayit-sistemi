print("HOŞGELDİNİZ...Yaşanan afetin yaralarını hep birlikte saracağız.")

#admine ait bilgiler
class admin:
    def __init__(self,ad,soyad,yas,tc,tel):
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
        self.tc=tc
        self.tel=tel
    def bilgilerigoster(self):
        print('----------yönetici bilgileri----------')
        print('Ad:{} , Soyad:{} , Yaş:{} , TC:{} , Tel:{}'.format(admn.ad,admn.soyad,admn.yas,admn.tc,admn.tel))
admn=admin(ad='Emine',soyad='Ergeçmiş',yas=0,tc=123456789,tel=5551234567)
admn.bilgilerigoster()
"""
(sisteme üye olmadan bu sistemi kullanamazsınız!!)
"""
demet=('1-sisteme üye ol','2-sisteme giriş yap','3-şifremi unuttum','4-sisteme geçiş','q-çıkış yap')
for i in demet:
    print(i)
    
    uyebilgileri={}   
    def uyeol():
        tc=input("11 haneli TC kimlik numaranızı tuşlayın: ")
        adsd=input('adınızı ve soyadınızı girin:')
        kaolustur=input('kullanıcı adı oluşturun:')
        sifre=input("şifrenizi oluşturun:")
        dy=int(input('doğum yılınızı giriniz:'))
        yas=2023-dy
        c=input('cinsiyetinizi giriniz:')
        telno=int(input('Telefon numaranızı başında 0 olmadan giriniz:'))
        uyebilgileri[kaolustur] =[tc,adsd,sifre,yas,c,telno]
        print(uyebilgileri[kaolustur])
        
    def sistemegiris():
         hasder=input("Afetten etkilenen binanızın hasar tespit sonucuna göre hasar derecesini giriniz. ")
         list=["1=acil yıktırılacak bina","2=yıkık","3=ağır hasarlı","4=orta hasarlı","5=az hasarlı","6=hasarsız"]
         print(list)

         kay=int(input("(1-12 ay arası tercih yapabilirsiniz)yaklaşık olarak kaç ay konaklayacağınızı giriniz:"))
         if(kay<13 and kay>0):
                 print(f'sisteme {kay} ay kadar konaklama yapacağınız bilgisi kaydedilmiştir')
         else:
                 print("hatalı tuşlama yapılmıştır.")
         iş=input("Daha önceden çalıştığınız bir işiniz var mıydı EVET ise 'e' , HAYIR İSE 'h' girin")
         if(iş.lower()=='e'):
              input("önceden çalıştığınız işi giriniz:")
         else:
              input("çalışabileceğiniz iş pozisyonlarını giriniz:")
               
              
                
while True:
    ss = input("Yapmak istediğiniz işlemin numarasını veya harfini girin:")
    if ss == 'q':
        print('...çıkılıyor...')
        break
    elif ss == '1':
        print("Sisteme üye ol seçeneğini seçtiniz")
        uyeol()
        
        durum = input("Bilgileri onaylıyorsanız evet, onaylamıyorsanız hayır girin.")
        if durum.lower() == "evet":
            extrkisi = input("Oluşturacağınız kayda eklemek istediğiniz başka biri var mı? Evet ise 'e', hayır ise 'h' girin:")
            if (extrkisi.lower() == 'e'):
                print("Eklemek istediğiniz kişinin bilgilerini giriniz")
                uyeol()
            else:
                sistemegiris()
        else:
            sistemegiris()
              

    elif(ss=='2'):
        print("sisteme giriş yap seçeneğini seçtiniz kullanıcı adınızı ve parolanızı girin")
        kaolustur=input("kullanıcı adı: ")
        sifre=input("şifre: ")
        if kaolustur in uyebilgileri and uyebilgileri[kaolustur][2] == sifre:
            print("bilgiler doğru")
            print("giriş yaptınız..")
        else:
            break
        
    elif(ss=='3'):
         while True:
             print('şifremi unuttum seçeneğini seçtiniz.')
             ys=input('oluşturmak istediğiniz yeni şifrenizi giriniz:')
             ts=input('Lütfen oluşturduğunuz yeni şifrenizi tekrar giriniz:')
             if not ys:
                   print("parola oluşturmadan işleme devam edemezsiniz!")
             elif len(ys)>12 or len(ys)<5:
                   print("parola 12 karakterden uzun 5 karakterden kısa olmamalı") #döngüye sok tekrar şifre girsin
             elif(ys==ts):
                   print('yeni şifreniz oluşturuldu.')
                    
             else:
                 print('şifreler birbiriyle uyuşmamaktadır')
             break
   
    elif(ss=='4'):
        sistemegiris()
                    
        deviş = input("Hala devam edebileceğiniz/etmekte olduğunuz bir işiniz var mı? EVET ise 'e', HAYIR İSE 'h' girin: ")

        if deviş.lower() == 'e':
          input("İşi giriniz:")
          asücret = 8500
          maas = int(input("Aldığınız maaşı TL bazında giriniz:"))
    
          def maastankesinti(maas,yuzde=15):
            odenecektutar = maas * yuzde / 100
            kalan = maas - odenecektutar
            maas -= odenecektutar
            return maas, odenecektutar, kalan
    
          if maas>asücret:
            maas, odenecektutar, kalan = maastankesinti(maas)
            print("maaşınızın %15'lik kısmı yani {} TL her ay ev sahibine ödenir ve maaşınızdan kalan para {} TL'dir.".format(odenecektutar, kalan))
          else:
           print("Herhangi bir ücret ödenmez.")
        else:
          print("En kısa sürede çalışabileceğiniz bir iş bulmalısınız.")     

        şehirt=input("şehir tecihiniz var mıdır EVET ise 'e' , HAYIR İSE 'h' girin=")
        sehirlist=[]
        i=0
        while(i<3):
          sehir=input("şehir giriniz:")
          sehirlist.append(sehir)
          i+=1
        
        if(şehirt.lower()=='e'):
          print("seçtiğiniz şehirlerin listesi {}".format(sehirlist))
        else:
          print("size uygun kriterlerde bir şehir rastgele seçilecektir")

    else:
        print('....YANLIŞ GİRİŞ....')
        print("Aşağıdaki seçeneklerden birini giriniz:",demet)
