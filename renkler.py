#Berkay kucuk
#berkaykucuk.com.tr
#github.com/bksec

#####################################
###############RENKLER###############
#####################################

sifirla  = '\033[0m'
beyaz = '\033[37m'
kirmizi= '\033[31m'
turuncu = '\u001b[38;5;208m'
yesil= '\033[32m'
sari= '\033[33m'
lacivert= '\033[34m'
pembe= '\033[35m'
mor = '\u001b[38;5;165m'
mavi= '\u001b[38;5;32m'
siyah = '\033[90m'
kahverengi = '\u001b[38;5;95m'
aciksari = '\u001b[38;5;228m'
gri = '\u001b[38;5;246m'
turkuaz = '\u001b[38;5;45m'
pmavi = '\033[96m'#p --> parlak
pkirmizi= '\033[91m'
pyesil = '\033[92m'
psari = '\033[93m'
asiyah= '\033[40m'#a --> arkaplan
akirmizi= '\033[41m'
ayesil= '\033[42m'
asari= '\033[43m'
alacivert= '\033[44m'
amor= '\033[45m'
amavi= '\033[46m'
abeyaz= '\033[47m'
apsiyah= '\033[100m'#a --> arkaplan-parlak
apkirmizi= '\033[101m'
apyesil= '\033[102m'
apsari= '\033[103m'
aplacivert= '\033[104m'
apmor= '\033[105m'
apmavi= '\033[106m'
apbeyaz= '\033[107m'
apsifirla= '\033[0;49m'
#yazi sekilleri
kalin = '\033[1m'
altcizgi = '\033[4m'
parlak = '\033[5m'
    

tum_renkler=("sifirla","beyaz","kirmizi","turuncu","yesil","sari","lacivert","pembe","mor","mavi","siyah","aciksari","gri","kahverengi","pmavi","pkirmizi","pyesil","psari","asiyah","akirmizi","ayesil","asari","alacivert","amor","amavi","abeyaz","apkirmizi","apyesil","apsari","aplacivert","apmor","apmavi","apbeyaz","apsifirla","kalin","altcizgi","parlak")



def rastgeleRenkler(*rastgele):
    
    import random
    rastgeleliste = list(rastgele)
    rastgeleRenk = random.choice(rastgeleliste)
    return rastgeleRenk


