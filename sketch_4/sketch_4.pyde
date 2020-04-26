import random 
add_library('pdf') 

def setup():
    global img,img1
    size(400,400) 
    img = loadImage("zdjecie.png") 
    img1 = loadImage("wasy.png")
    beginRecord(PDF, "outzdjecie.pdf") 
    
    print(random.random()) 
    fill(20,255,200) 


def draw():
    global img,img1
    image(img, 0,0, height, width)
    image(img1,130,180,height/3,width/3)
      #1 wyświetlamy wczytany obraz we wskazanych wpółrzędnych (czyli w rogu 0,0) skalując do wymiaru wysokości i szerokości naszego okna
    #shape(img, 0,0, height/2, width/2) #2 wyświetlamy wczytany kształt we wskazanych współrzędnych  skalując do wysokości i szerokości pliku
    endRecord() #1 kończymy zapisywanie do pliku PDF, by nie zapisać tylu obrazów na sobie co odpalonych klatek. Można zapis zrobić dopiero po wykonaniu kilku operacji draw, np. jeżeli chcielibyśmy narsować jakiś obraz kilkukrotnie w paru miejscach przesuwając go co klatkę
    #exit() #2 plik zapisze się dopiero przy jego zamknięciu będącym jednocześnie zamknięciem zapisywania


def mousePressed():
    exit()
