from pynput import keyboard

def on_press(key):
    try:
        print('Key pressed: {0}',format(key.char))
    except AttributeError:
        print('Special keypressed: {0}'.format(key))

def on_release(key):
    print('Keyreleased: {0}'.format(key))
    if  key == keyboard.Key.esc:
        #Stop the listener
        return False

# Start the listener
with keyboard.Listener(on_pres=on_press, on_releae=on_release) as listener:
    listener.join()