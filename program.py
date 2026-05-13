import pyautogui as tp
import keyboard as kb
import time


def muovi(tasto, x, y):
    if kb.is_pressed(tasto):
        tp.moveTo(x, y)


def muovi_per(tasto, x, y):
    if kb.is_pressed(tasto):
        tp.moveRel(x,y)


def muovi_per_comb(t1, t2, x, y):
    if kb.is_pressed(t1) and kb.is_pressed(t2):
        tp.moveRel(x, y)


sinistro_premuto = False
def tasto_sinistro(t1, t2):
    global sinistro_premuto

    if kb.is_pressed(t1) and kb.is_pressed(t2) and not sinistro_premuto:
        tp.mouseDown(button='left')
        sinistro_premuto = True

    elif kb.is_pressed(t1) and kb.is_pressed(t2) and sinistro_premuto:
        tp.mouseUp(button='left')
        sinistro_premuto = False


destro_premuto = False
def tasto_destro(t1, t2):
    global destro_premuto

    if kb.is_pressed(t1) and kb.is_pressed(t2) and not destro_premuto:
        tp.mouseDown(button='right')
        destro_premuto = True

    elif kb.is_pressed(t1) and kb.is_pressed(t2) and destro_premuto:
        tp.mouseUp(button='right')
        destro_premuto = False


def scroll(t1, t2, x):
    if kb.is_pressed(t1) and kb.is_pressed(t2):
        tp.scroll(x)
    


while (True):                         #wait until
    if kb.is_pressed("a") and kb.is_pressed("m") and kb.is_pressed("k"):
        break

while (True):
    
        scroll("alt", "up", x=100)
        scroll("space", "up", x=500)
        scroll("alt", "down", x=-100) 
        scroll("space", "down", x=-500) 
        muovi_per("up", x=0, y=-20)
        muovi_per("down", x=0, y=20)
        muovi_per("right", x=20, y=0)
        muovi_per("left", x=-20, y=0)
        muovi_per_comb("up", "shift", x=0, y=-300)
        muovi_per_comb("down", "shift", x=0, y=300)
        muovi_per_comb("right", "shift", x=300, y=0)
        muovi_per_comb("left", "shift", x=-300, y=0)
        tasto_sinistro("ctrl", "enter")
        tasto_destro("shift", "enter")        


        if kb.is_pressed("s") and kb.is_pressed("m") and kb.is_pressed("k"):
            break



