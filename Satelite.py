import pgzrun
from random import randint
from time import time


WIDTH = 800
HEIGHT = 600

lines = []
satellites = []
next_satellite = 0

start_time = 0
total_time = 0
end_time = 0

number_of_satellites = 8
def create_satellites():
    global start_time 
    for i in range(0,number_of_satellites):
    satellite = Actor("satelite")
    satellite.pos = randint(40,WIDTH-40), randint(40,HEIGHT-40)
    satellites.append(satellite)

def draw():
    global total_time
    screen.blit("Space",(0,0))
    number = 1 
    for satellite in satellites:
        screen.draw.text(str(number), (satellite.pos[0]), satellite.pos[1]+20)
        satellite.draw()
        number = number + 1 
    for line in lines:
        screen.draw.line(line[0], line[1], (12,32,31))
    if next_satellite < number_of_satellites :
        total_time = time() - start_time
        screen.draw.text(str(round(total_time,1)), (10,10), fontsize=40)
    else:
         screen.draw.text(str(round(total_time,1)), (10,10), fontsize=40)
         