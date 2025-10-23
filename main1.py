class Texnika:
    def __init__(self,nomi, narxi, brendi):
        self.nomi = nomi
        self.narxi = narxi
        self.brendi = brendi


    def info(self):
        print(f' Nomi: {self.nomi} Narxi: {self.narxi} Brendi: {self.brendi}')
        
        
    def narx_oshdi(self, foiz):
        raqam = int(self.narxi)
        yangi_narx = raqam + (raqam * foiz/100)
        self.narxi = f'{int(yangi_narx)}$'
        print(f'{self.nomi} narxi {foiz}% ga oshdi! yangi narx: {self.narxi}')


class Telefon(Texnika):
    def __init__(self, nomi, narxi, brendi, kameralar_soni):
        super().__init__(nomi, narxi, brendi)
        self.kameralar_soni = kameralar_soni
        
        
    def zvonok(self):
        print(f'{self.nomi} telefon qildi ')


    def fotoolish(self):
        print(f'{self.nomi} rasimga oldi unda kameralar soni: {self.kameralar_soni}')
        
        
class Noutbook(Texnika):
    def __init__(self, nomi, narxi, brendi, batareya_soati):
        super().__init__(nomi, narxi, brendi)
        self.batareya_soati = batareya_soati
        
        
    def yangilash(self):
        print(f'{self.nomi} tizimiga yangilanish kiritilmoqda')
        
        
    def ish_boshladi(self):
        print(f'{self.nomi} ishga tushdi endi u taxminan ishlash vaqti {self.batareya_soati}')

        
        
tel1 = Telefon('Iphone', 400, 'Apple', 3)
nout = Noutbook('Asus', 600, 'asus', 5)


tel1.info()
tel1.fotoolish()
tel1.zvonok()
tel1.narx_oshdi(50)

print()

nout.info()
nout.ish_boshladi()
nout.yangilash()
nout.narx_oshdi(10)