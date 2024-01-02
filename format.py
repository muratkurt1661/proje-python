#coding:utf-8
import os

txt="""
**************************************************************************************
1-)windows10 x86 kurulumu yapar
2-)Windows10 x64 kurulumu yapar
3-)Windows7 kurulumu yapar (x86 & x64)

NOT:Bu program canlı windows sisteminin üzerine kurulum yapmaz.Lütfen önce disk yöne-
ticisine girip windows u kuracağınız bir bölüm oluşturunuz.Ardından kurulum bittikten 
sonra dilerseniz eski windowsunuzun kurulu olduğu bölümü silebilirsiniz.Windows  .iso 
dosyanızı sanal sürücü olarak bağladıktan sonra veyahutta windows kurulum disketinizi 
bilgisayara taktıktan sonra windows kurulum işlemine başlayabilirsiniz.Kolay Gelsin.

Lütfen yapmak istediğiniz komutu seçiniz:

**************************************************************************************


"""

metin=input(txt)

HDD_SSD=input("kurulum  yapacağınız diskin birim etiketini giriniz:")
USB_CD=input("bootable diskinizin birim etiketini giriniz:")

def bootsettings():
    print(os.system("bcdboot {}:\windows".format(HDD_SSD)))


def win7():
    kodlar="""
    dism /get-wiminfo /wimfile:{}:\sources\install.wim
    """.format(USB_CD)

    print(os.system(kodlar))

    index=input("index no giriniz:")

    kodlar2="""
    dism /Apply-Image /ImageFile:{}:\sources\install.wim /index:{} /ApplyDir:{}:\ 
    """.format(USB_CD,index,HDD_SSD)
    print(os.system("format {}:/q".format(HDD_SSD)))
    print(os.system(kodlar2))

    bootsettings()

def win10x86():
    kodlar="""
    DISM /get-wiminfo /wimfile:{}:/x86/sources/install.esd
    """.format(USB_CD)

    print(os.system(kodlar))

    index=input("index no giriniz:")
    installdir=str("x86")
    kodlar2="""
    dism /apply-image /imagefile:{}:\{}\sources\install.esd /index:{} /applydir:{}:\ 
    """.format(USB_CD,installdir,index,HDD_SSD)
    print(os.system("format {}:/q".format(HDD_SSD)))
    print(os.system(kodlar2))
    bootsettings()

def win10x64():
    kodlar="""
    DISM /get-wiminfo /wimfile:{}:/x64/sources/install.esd
    """.format(USB_CD)

    print(os.system(kodlar))

    index=input("index no giriniz:")
    installdir=str("x64")
    kodlar2="""
    DISM /Apply-Image /Imagefile:{}:\{}\sources\install.esd /index:{} /applydir:{}:\ 
    """.format(USB_CD,installdir,index,HDD_SSD)
    print(os.system("format {}:/q".format(HDD_SSD)))
    print(os.system(kodlar2))
    bootsettings()


#############################################################################################################################################
    
if metin=="1":
    win10x86()

elif metin=="2":
    win10x64()

elif metin=="3":
    win7()
else:
    print("yanlış tuşlama yaptınız")


