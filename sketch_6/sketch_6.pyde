class Kolo(): # mieliście skorzystać z mojej klasy, ale ta jest analogiczna, więc uznam
    def __init__(self, wielkosc):
        self.wielkosc = wielkosc
    def sketch(self, x, y):
        self.x = x
        self.y = y
        circle(self.x, self.y,self.wielkosc)

class KoloKolor(Kolo): # nadawajcie adekwatne nazwy, bo a, b, c i 1, 2, 3 na prawdę nie ułatwiają później czytania kodu i połąpania się w nim wam
    def czerwonekolo(self, x, y):
        fill(255,0,0)
        Kolo.sketch(self, x, y)
    def zielonekolo(self, x, y):
        fill(0,255,0)
        Kolo.sketch(self, x, y)
    def niebieskiekolo(self, x ,y):
        fill(0,0,255)
        Kolo.sketch(self, x, y)
    
        
def setup():
    size(500, 500)
    background(0)
    kolo = Kolo(50)
    kolo.sketch(200, 300) 
    kolo = KoloKolor(120)
    kolo.czerwonekolo(300, 200)
    kolo = KoloKolor(40)
    kolo.zielonekolo(50,100)
    kolo = KoloKolor(60)
    kolo.niebieskiekolo(400,370)
    
# 1, 75pkt
