import random 
add_library('pdf') 

def setup():
    global img,img1
    size(400,400) # to nie są proporcje zdjęcia dokumentowego
    img = loadImage("zdjecie.png") 
    img1 = loadImage("wasy.png")
    beginRecord(PDF, "outzdjecie.pdf") 
    
    print(random.random()) 
    fill(20,255,200) 


def draw():
    global img,img1
    image(img, 0,0, height, width)
    image(img1,130,180,height/3,width/3) # miał być wybór elementu
    
    endRecord() 


def mousePressed():
    exit()
    
# 1,5p
