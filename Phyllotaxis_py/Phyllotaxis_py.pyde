n = 0
c = 12

def setup():
    size(720, 720)
    colorMode(HSB)
    background(0,0,0)
    
    
def draw():
    global n
    angle = n * 137.5
    radius = c * sqrt(n)
    x = radius * cos(degrees(angle)) + width/2
    y = radius * sin(degrees(angle)) + height/2
    fill((angle-radius) % 256 , 255, 255)
    noStroke()
    ellipse(x, y, 8, 8)
    n +=1
    
    
