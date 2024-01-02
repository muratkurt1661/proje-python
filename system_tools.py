import os


    

metin=""" 
**********************************************************
*                      HOŞGELDİNİZ                       *
*                   ig=muratkurtt1661                    *                  
*                                                        *
* 1-)Bilgisayarı kapatır                                 *
* 2-)Bilgisayarı yeniden başlatır                        *
* 3-)sistemi programları ve driverları toptan günceller  *
* 4-)şifreyi değiştirir yada kaldırır                    *
* 5-)Ekranı kilitler                                     *
* 6-)Gelişmiş başlangıç ayarını açar                     *
* 7-)Windows10 & Office programı crackler                *
* 8-)Windows kurulumu yapar                              *
* işlem yapmak istediğiniz numarayı giriniz.             *
* Programı sonlandırmak için q ya basınız:              *                                         
*                                                        *
********************************************************** 
"""
message=input(metin)

def kapat():
    os.system("shutdown -s -t 15 ")

def restart():

    os.system("shutdown -r -t 15")

def upgrade():
    os.system("winget upgrade --all")

def password():
    
    kullanıcı=input("kullanıcı adı giriniz:")
    
    os.system("net user {} *".format(kullanıcı))

def __advanced_options__():

    os.system("shutdown /r /o /f /t 15")
    
def kilitle():
    os.system("Rundll32.exe user32.dll,LockWorkStation")

def _crack():
    os.system("kms.bat")
    

def winsetup():
    import format
    
    

###########################################################################################################



if message=="1":
    
    kapat()
    print("Bilgisayar 15 saniye içinde kapanacak:")
    
    a=input(" kapanmasını istemiyorsanız a ya basınız:")
    if a=="a":
         os.system("shutdown -a")
    else:
         print("bekleyiniz...")
        

elif message=="2":
    print("Bilgisayar 15 saniye içinde yeniden başlatılıyor :")
    restart()
    a=input(" yeniden başlamasını istemiyorsanız a ya basınız:")
    if a=="a":
        os.system("shutdown -a")
    else:
        print("bekleyiniz...")
        
elif message=="3":
    p=input("güncellemeyi başlatmak için p tuşuna basınız:")

    if p=="p":
        upgrade()
    else:
        print("yanlış tuşa bastınız")
        
elif message=="4":
    os.system("net user")
    print("şifre oluştururken girilien girdiler güvenlik amacıyla ekranda gözükmez:)")
    password()
        

elif message=="5":
    kilitle()
        
        
elif message=="6":
    print("15 saniye bekleyiniz...")
    __advanced_options__()
    a=input("iptal etmek için a ya basınız:")
        
    if a=="a":
        os.system("shutdown -a")
        
elif message=="7":
    
    print("bundan sonraki ekran ne yazıkki ingilizce efendim.")
    _crack()


elif message=="8":
    winsetup()
        
elif metin=="q":
    system_tools=exit()
        