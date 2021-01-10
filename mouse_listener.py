from pynput import mouse

def on_click(x,y, button, pressed):
    print('Button: %s, position:(%s, %s), Pressed : %s'%(button, x, y, pressed))
def on_move(x,y):
    print('위치 : x:%s, y:%s' %(x,y))

with mouse.Listener(on_move=on_move, on_click=on_click)as listener:
    listener.join()
    