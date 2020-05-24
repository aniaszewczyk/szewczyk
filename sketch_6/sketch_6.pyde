class Kolo():
    def __init__(self, wielkosc):
        self.wielkosc = wielkosc
    def sketch(self, x, y):
        self.x = x
        self.y = y
        circle(self.x, self.y,self.wielkosc)

class Kolo2(Kolo):
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
    kolo = Kolo2(120)
    kolo.czerwonekolo(300, 200)
    kolo = Kolo2(40)
    kolo.zielonekolo(50,100)
    kolo = Kolo2(60)
    kolo.niebieskiekolo(400,370)
