class Kwadrat(): # klasy zwyczajowo zapisujemy wielką literą
    def __init__(self, x, y, w):
        self.x = x
        self.y = y
        self.w = w
        self.up = 0
        self.down = 0
        self.left = 0
        self.right = 0
        
    def na_ekranie(self):
        fill(0)
        rect(self.x, self.y, self.w, self.w)
        
    def porusza_sie(self):
        self.x = self.x + (self.right - self.left)
        self.y = self.y + (self.down - self.up)
        
def setup():
    size(400,400)
    global k1, k2
    k1 = Kwadrat(150,150, 50)
    k2 = Kwadrat(200,200, 50)
    
def draw():
    background(255)
    k1.na_ekranie()
    k2.na_ekranie()
    k1.porusza_sie()
    
# żeby oba albo więcej kwadrató się poruszało, zrobiłąbym wartości kierunkowe atrybutamiklasy zamist instancji
# jeżeli ten ruch ma się różnić, to dodałabym jakieś wartości typu prędkość, czy aktywacja już w metodach, czy atrybutach poszczególnych figur
def keyPressed():
    if keyCode == UP:
        k1.up = 1
    if keyCode == DOWN:
        k1.down = 1
    if keyCode == LEFT:
        k1.left = 1
    if keyCode == RIGHT:
        k1.right = 1
        
def keyReleased():
    if keyCode == UP:
        k1.up = 0
    if keyCode == DOWN:
        k1.down = 0
    if keyCode == LEFT:
        k1.left = 0
    if keyCode == RIGHT:
        k1.right = 0
        
# 2pkt
