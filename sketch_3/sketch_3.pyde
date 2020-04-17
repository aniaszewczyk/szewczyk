def setup():
    size(400, 400)
    textSize(70) 

def draw():
    background(70,130,180)
    noFill()
    strokeWeight(3)
    stroke(85,107,47)
    bezier(60,120,50,400,400,0,400,400)
    bezier(50,110,40,390,390,0,400,400)
    
    fill(0)
    text("A.", width/2-50, height/2) 
    text(" S", width/2, height/2)
    
   
    
    
    if (mouseX > 150 and mouseX < 220 and mouseY > 150 and mouseY < 200):
        fill(75,0,130)
        text("A.", width/2-50, height/2)
        
def keyPressed():
  if(key=='s'):
      fill(75,0,130)
      text(" S", width/2, height/2)
  
  if (key == CODED):
    if (keyCode == RIGHT and mouseX > 150 and mouseX < 220 and mouseY > 150 and mouseY < 200):
        fill(0)
        text("A.", width/2-50, height/2)
        fill(75,0,130)
        text(" S", width/2, height/2)
        
    if (keyCode == LEFT):
        fill(75,0,130)
        text("A.", width/2-50, height/2)
        
        
