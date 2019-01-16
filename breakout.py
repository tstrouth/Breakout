#Author: Tyler Strouth & Kaitlin Sine
#Purpose: to create the game Breakout in Python
import rectangles, time
import tkinter as tk
#constants
WINDOW_HEIGHT = 500
WINDOW_WIDTH  = 400
ORDER_OF_MAG  = 10
X_WIDTH       = 20
QUARTER       = 4
START_BLOCK_Y = 20
FRAMES_PER_SECOND = 1/60

# pre: needs a valid tkinter canvas
#post: goes through a nested for loop and creates blocks at the top of the
#      screen then appends the blocks to a list
def draw_blocks(canvas):
        block_list = []
        for i in range(0, WINDOW_WIDTH,
                       WINDOW_WIDTH // ORDER_OF_MAG * 2):
            for j in range(START_BLOCK_Y, WINDOW_HEIGHT // QUARTER, WINDOW_HEIGHT):
                if (0 <= i <= WINDOW_WIDTH) and (0 <= j <=
                                                 WINDOW_HEIGHT //
                                                 ORDER_OF_MAG):
                    blocks = rectangles.blocks(canvas)
                    blocks.x_coor_1 = i
                    blocks.x_coor_2 = i + X_WIDTH
                    blocks.y_coor_1 = j
                    blocks.y_coor_2 = j + ORDER_OF_MAG 
                    blocks.color    = "red"
                blocks.draw_blocks()
                block_list.append(blocks)

        return block_list

#initiates tkinter window
window = tk.Tk()
#creates the canvas
canvas = tk.Canvas(window, width = WINDOW_WIDTH,
                   height = WINDOW_HEIGHT)
canvas.pack()
#draws the objects
#with specific conditions
block_list = draw_blocks(canvas)

paddle = rectangles.paddle(canvas)
paddle.x_coor_1 = 210
paddle.x_coor_2 = 290
paddle.y_coor_1 = 420
paddle.y_coor_2 = 440
paddle.velocity = 20
paddle.color    = "green"
paddle.draw_paddle()

box = rectangles.box(canvas)
box.x_coor_1   = 240
box.y_coor_1   = 270
box.y_velocity = 4
box.x_velocity = 4
box.diameter   = 10
box.color      = "magenta"

box.draw_box()
 
window.bind("<KeyPress>", paddle.move_paddle)
game_play = True

#starts the animation loop
"""
while we play the game it determines which bricks are soft "blue"
vs which are strong "red" once these are determined if
strong is hit they become soft and if soft is hit they are
removed from the block list and then we re-iterate through
the block list and re-draw the blocks
"""
while game_play:
    canvas.delete(tk.ALL)
    paddle.draw_paddle()
    box.move_box()
    box.draw_box()
    i = 0
    if box.check_collision(paddle.x_coor_1, paddle.x_coor_2, paddle.y_coor_1,
                           paddle.y_coor_2) == True:
        box.y_velocity *= -1
    while i < len(block_list):
        block_list[i].draw_blocks()
        if (box.check_collision(block_list[i].x_coor_1, block_list[i].x_coor_2,
                               block_list[i].y_coor_1, block_list[i].y_coor_2)
            == True):
                
                box.y_velocity *= -1
            
                if block_list[i].color == "blue":
                        block_list.pop(i)
                elif block_list[i].color == "red":
                        block_list[i].color = "blue"
        #print('i', i, 'length', len(block_list))
        i += 1
    if len(block_list) == 0:
        congrats = canvas.create_text(WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2,
                                      text ="congratulations")
        game_play = False
    canvas.update()
    time.sleep(FRAMES_PER_SECOND)

window.mainloop()


