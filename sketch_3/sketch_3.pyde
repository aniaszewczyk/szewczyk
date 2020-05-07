def setup():
    size(400, 400)
    textSize(70)
    global zaznaczenie
    zaznaczenie = (75,0,130) # ku czytelności i by nie musieć pamiętać co to za cyferki były, dodatkowo przy chęci zmianykoloru wystarczy zmienić tylko w tym miejscu, a nie szukać gdzie było wpisywane
    # rzeczy, które wywołują się raz na starcie lepiej dać w setup
    noFill()
    strokeWeight(3)
    stroke(85,107,47)
    background(70,130,180)
    bezier(60,120,50,400,400,0,400,400)
    bezier(50,110,40,390,390,0,400,400)

def draw():        
    if keyPressed:
        if(key=='s'):
            fill(*zaznaczenie)
            text(" S", width/2, height/2)
            fill(0)
            text("A.", width/2-50, height/2)
        
        if (key == CODED):
            if (keyCode == RIGHT and mouseX > 150 and mouseX < 220 and mouseY > 150 and mouseY < 200):
                fill(0)
                text("A.", width/2-50, height/2)
                fill(*zaznaczenie)
                text(" S", width/2, height/2)
                
            if (keyCode == LEFT):
                fill(*zaznaczenie)
                text("A.", width/2-50, height/2)
                fill(0)
                text(" S", width/2, height/2)
    elif (mouseX > 150 and mouseX < 220 and mouseY > 150 and mouseY < 200):
        fill(*zaznaczenie)
        text("A.", width/2-50, height/2)
        fill(0)
        text(" S", width/2, height/2)
    else:
        fill(0)
        text("A.", width/2-50, height/2) 
        text(" S", width/2, height/2)
        
# poprawiłam, przeanalizuj
# w tym momencie same strzałki też działają, ale nie będę bardziej mieszać ;)
# 1,5pkt
