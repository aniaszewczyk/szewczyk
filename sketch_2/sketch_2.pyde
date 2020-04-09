def setup():
    size(360,360)
    global a, b, c, d # jeżeli są w tej funkcji - mamy pewność, że zainicjalizują się przy tworzeniu okna
    a = 180
    b = 0
    c = 1
    d = -1
    
def draw():
    background(0)
    global a, b, c, d
    
    ellipse(a,b,50,50)
    a = a - c
    b = b + d
    
    if (a > width):
        fill(255,0,0)
        a = width
        c = -c
    if (b > height):
        fill(0,255,0)
        b = height
        d = -d
    if (a < 0):
        fill(0,0,255)
        a = 0
        c = -c
    if (b < 0):
        fill(100)
        b = 0
        d = -d
        #oryginalnie napisane
    
    if mousePressed:
        exit()
# zmiana koloru miała być z wykorzystaniem kolekcji, bo mieliście je powtórzyć
# 1,5p
