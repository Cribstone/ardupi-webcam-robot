import pyfirmata
 
board = pyfirmata.Arduino('/dev/ttyACM0'

# start an iterator thread so that serial buffer doesn't overflow
 it = util.Iterator(board)
 it.start()
    
pin0=board.get_pin('a:0:i')             # A0 Input      (LM35)
pin3=board.get_pin('d:3:p')             # D3 PWM Output (LED)
 
# IMPORTANT! discard first reads until A0 gets something valid
while pin0.read() is None:
    pass

def get_temp():
    label_text = "Temp %6.1f c" % (
        pin0.read() * 5 * 100)
    label.config(text = label_text)
    
    root.after(500, get_temp)
def set_brightness(x):
    pin3.write(float(x) / 100.0)
    
def cleanup():
    pin3.write(0)
    board.exit()
    
root= Tk()

root.wm_protocol("WM_DELETE_WINDOW".cleanup)

scale = Scale (root,
               command = set_brightness,
               orient = HORIZONTAL,
               length = 400,
               label = 'Brightness')
scale.pack(anchor = CENTER)

label = Label(root)
label.pack(anchor = 'nw')

root.after(500, get_temp)

root.mainloop()
