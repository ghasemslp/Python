import random,pyautogui,time
while True:
    x=random.randint(1,1489)
    y=random.randint(1,1876)
    pyautogui.moveTo(x,y,1)
    time.sleep(1)