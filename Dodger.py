# Imports go at the top
from microbit import *
import random
player_x = 2
player_y = 4
brick_x = random.randint(0,4)
brick_y = 0
lives = 3
score = 0


# Code in a 'while True:' loop repeats forever
while lives > 0:
    # player logic
    if button_a.is_pressed(): player_x -= 1
    if button_b.is_pressed(): player_x += 1
    if player_x > 4: player_x = 4
    if player_x < 0: player_x = 0
        
    # brick logic
    brick_y += 1
    if brick_y > 4: 
        brick_x = random.randint(0,4)
        brick_y = 0
        score += 1
    display.set_pixel(player_x,player_y,9)
    display.set_pixel(brick_x,brick_y,9)
    if brick_y > 0: display.set_pixel(brick_x,brick_y-1,5)
    if brick_y > 1: display.set_pixel(brick_x,brick_y-2,2)


    # check hit
    if brick_x == player_x and brick_y == player_y:
        for i in range(5):
            display.set_pixel(brick_x,brick_y,6)
            sleep(100)
            display.clear()
            sleep(100)
        lives -= 1
        brick_x = random.randint(0,4)
        brick_y = 0
        
    sleep(200)
    display.clear()

display.scroll('SCORE:'+ str(score))
display.scroll('SCORE:'+ str(score))
    