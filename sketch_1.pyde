def setup():
    size(400, 400)
    point(1,1)
    rectMode(RADIUS)
    
def draw():
    print(height, width, mouseX, mouseY, mousePressed)
    
    if mousePressed:
        rect(height/4,width/4,height/4,width/4)   
    else:
        line(width, height, mouseX, mouseY)
