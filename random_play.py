import pyautogui
import random
import time
from PIL import ImageGrab
from PIL import Image
import numpy as np
import pytesseract
import cv2
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def select_gba():
    pyautogui.moveTo(1130, 220, 0.2)
    pyautogui.click()
    time.sleep(0.2)
    
def press_key(key):
    time.sleep(0.1)
    pyautogui.keyDown(key)
    pyautogui.keyUp(key)
    
def select_unit():
    press_key('a')
    press_key('z')

def move_unit(left=0,right=0,up=0,down=0, random_move=False, max_manhattan=5):
    if random_move==True:
        finding_move = True
        while finding_move:
            left = random.randint(0,max_manhattan+1)
            right = random.randint(0,max_manhattan+1)
            up = random.randint(0,max_manhattan+1)
            down = random.randint(0,max_manhattan+1)
            if abs(left-right) + abs(up-down) <= max_manhattan:
                finding_move = False
    #optimize the movement process so excess moves aren't performed
    if left>right:
        for i in range(0, left-right):
            press_key('j')
    elif right>left:
        for i in range(0, right-left):
            press_key('l')
    if up>down:
        for i in range(0, up-down):
            press_key('i')
    elif down>up:
        for i in range(0, down-up):
            press_key('k')

    press_key("z")
    time.sleep(0.7)

#assume unit has moved
def wait():
    press_key('i')
    press_key('z')
    
def set_quickplay():
    press_key('k')
    press_key('z')
    press_key('k')
    press_key('k')
    press_key('k')
    press_key('z')
    time.sleep(1.5)
    press_key('l')
    press_key('l')
    press_key('k')
    press_key('l')
    press_key('k')
    press_key('l')
    press_key('l')
    press_key('x')
    press_key('i')
    
def quick_reset():
    press_key('f1')
    
def start_fe8():
    time.sleep(2)
    press_key('z')
    time.sleep(8)
    press_key('z')
    time.sleep(1)
    press_key('z')
    time.sleep(1)
    press_key('k')
    press_key('z')
    press_key('z')
    press_key('j')
    press_key('z')
    time.sleep(4)
    press_key('v')
    time.sleep(3)
    press_key('v')
    time.sleep(2.5)
    press_key('v')
    press_key('v')
    time.sleep(4)
    press_key('v')
    time.sleep(1)
    press_key('v')
    time.sleep(1)
    press_key('v')
    time.sleep(3)
    press_key('v')

def reset_to_title():
    press_key('f1')

def trigger_wait():
    press_key('z')
    press_key('z')
    
def cancel():
    press_key('x')

def subscreen(x0,y0,x1,y1, screen):
    sub_img = []
    for i in range(y0,y1,1):
        row=[]
        for j in range(x0,x1,1):
            row.append(screen[i][j])
        sub_img.append(np.array(row))
    sub_img = np.array(sub_img)
    return sub_img

def wait_in_menu():
    screen = np.array(ImageGrab.grab(bbox = (885,84,1364,403)))
        
    length_5_left = subscreen(35,195,78,222, screen)
    length_4_left = subscreen(35,163,78,190, screen)
    length_3_left = subscreen(35,131,78,158, screen)
    length_2_left = subscreen(35,99,78,126, screen)

    length_5_right = subscreen(371,195,414,222, screen)
    length_4_right = subscreen(371,163,414,190, screen)
    length_3_right = subscreen(371,131,414,158, screen)
    length_2_right = subscreen(371,99,414,126, screen)
        
    left_5_text = pytesseract.image_to_string(length_5_left)
    left_4_text = pytesseract.image_to_string(length_4_left)
    left_3_text = pytesseract.image_to_string(length_3_left)
    left_2_text = pytesseract.image_to_string(length_2_left)
        
    right_5_text = pytesseract.image_to_string(length_5_right)
    right_4_text = pytesseract.image_to_string(length_4_right)
    right_3_text = pytesseract.image_to_string(length_3_right)
    right_2_text = pytesseract.image_to_string(length_2_right)
    
    #context: hips is what pytesseract reads the "Wait" option as
    
    if((left_5_text == "hips") or (left_4_text == "hips")
       or (left_3_text == "hips") or (left_2_text == "hips")
       or (right_5_text == "hips") or (right_4_text == "hips")
       or (right_3_text == "hips") or (right_2_text == "hips")):
        return True
    else:
        return False

def generics_are_dead():
    screen = np.array(ImageGrab.grab(bbox = (885,84,1364,403)))
    dialogue = subscreen(29,63,306,94, screen)
    seth_quote = pytesseract.image_to_string(dialogue)
    
    #context: "All that's left is their leader..."
    #is what pytesseract reads in the dialogue box
    #that triggers once only the boss is left alive
    
    if(seth_quote == "All that’s left is their leader..."):
        return True
    else:
        return False

def generic_dialogue_on_screen():
    screen = np.array(ImageGrab.grab(bbox = (885,84,1364,403)))
    
    quote_1 = subscreen(29,67,382,98, screen)
    quote_2 = subscreen(29,67,280,94, screen)
    
    quote_a = pytesseract.image_to_string(quote_1)
    quote_b = pytesseract.image_to_string(quote_2)
    
    #context: "What was that'? Do you think you can" and "Vou will be the first to diet"
    #are what pytesseract reads in the dialogue boxes that trigger
    #once the boss is the only one alive and it's his turn
    #and once he enters combat, respectively
    
    if((quote_a == "What was that’? Do you think you can")
       or (quote_b == "Vou will be the first to diet")):
        return True
    else:
        return False

def game_is_lost():
    screen = np.array(ImageGrab.grab(bbox = (885,84,1364,403)))
    dialogue = subscreen(205,63,378,98, screen)
    death_quote = pytesseract.image_to_string(dialogue)
    
    #context: "Brother... Im sorry," is what pytesseract reads in
    #the dialogue box that triggers once the main character dies
    
    #warning: Seth's death quote wasn't considered as a game over
    #condition because in the Normal Mode Prologue, he's invincible

    if(death_quote == "Brother... Im sorry,"):
        return True
    else:
        return False

def game_is_won():
    screen = np.array(ImageGrab.grab(bbox = (885,84,1364,403)))
    dialogue = subscreen(77,67,200,94, screen)
    death_quote = pytesseract.image_to_string(dialogue)
       
    #context: "What? How?" is what pytesseract reads in the dialogue
    #box that triggers once the boss dies
       
    if(death_quote == "What? How?"):
        return True
    else:
        return False

def is_player_phase():
    screen = np.array(ImageGrab.grab(bbox = (885,84,1364,403)))
    top_name = subscreen(111,21,162,44, screen)
    bottom_name = subscreen(111,245,162,268, screen)
    
    top_eirika = pytesseract.image_to_string(top_name)
    bottom_eirika = pytesseract.image_to_string(bottom_name)

    if((top_eirika == 'Eirika') or (bottom_eirika == 'Eirika')):
        return True
    else:
        return False

select_gba()
reset_to_title()
start_fe8()
time.sleep(2)
set_quickplay()
game_lost = False
game_won = False
turn = 0
while((game_lost != True) and (game_won != True)):
    #cursor always start at main character
    turn = turn+1
    print("Turno ", turn)
    press_key('z')
    move_unit(random_move=True)
    while(wait_in_menu() == False):
        cancel()
        press_key('z')
        move_unit(random_move=True)
    wait()
    
    select_unit()
    move_unit(random_move=True, max_manhattan=8)
    while(wait_in_menu() == False):
        cancel()
        press_key('z')
        move_unit(random_move=True, max_manhattan=8)
    wait()
    
    #enemy phase
    waiting = True
    while(waiting == True):
        time.sleep(5)
        if(is_player_phase() == True):
            print("Done waiting")
            waiting = False
        else:
            if((generics_are_dead() == True) or (generic_dialogue_on_screen() == True)):
                press_key('v')
            elif(game_is_won() == True):
                print("Game won!")
                game_won = True
                waiting = False
            elif(game_is_lost() == True):
                print("Game over")
                game_lost = True
                waiting = False
                
#reset_to_title()