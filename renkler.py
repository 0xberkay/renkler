

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
    

tum_renkler=("\033[0msifirla","\033[37mbeyaz","\033[31mkirmizi","\u001b[38;5;208mturuncu","\033[32myesil","\033[33msari","\033[34mlacivert","\033[35mpembe","\u001b[38;5;165mmor","\u001b[38;5;32mmavi","\033[90msiyah","\u001b[38;5;228maciksari","\u001b[38;5;246mgri","\u001b[38;5;95mkahverengi","\033[96mpmavi","\033[91mpkirmizi","\033[92mpyesil","\033[93mpsari\033[0m","\033[40masiyah","\033[41makirmizi","\033[42mayesil","\033[43masari","\033[44malacivert","\033[45mamor","\033[46mamavi","\033[47mabeyaz","\033[101mapkirmizi","\033[102mapyesil","\033[103mapsari","\033[104maplacivert","\033[105mapmor","\033[106mapmavi","\033[107mapbeyaz","\033[0;49mapsifirla","\033[1mkalin","\033[4maltcizgi\033[0m","\033[5mparlak")



def rastgeleRenkler(*rastgele):
    
    import random
    rastgeleliste = list(rastgele)
    rastgeleRenk = random.choice(rastgeleliste)
    return rastgeleRenk


