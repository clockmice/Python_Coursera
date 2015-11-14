# template for "Stopwatch: The Game"

# define global variables
import simplegui
time = 0
x = 0
y = 0
dsec = None

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    global dsec
    dsec = t % 10
    min = (t / 10) / 60
    sec = (t / 10) % 60
    return "%d:%.2d.%d" % (min, sec, dsec)

    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_handler():
    timer.start()

def stop_handler():
    global x, y
    if timer.is_running():
        timer.stop()
        y += 1
        if dsec == 0:
            x += 1

def reset_handler():
    global time, x, y
    timer.stop()
    time = 0
    x = 0
    y = 0

# define event handler for timer with 0.1 sec interval
def timer_handler():
    global time
    time += 1

# define draw handler
def draw(canvas):
    global time, x, y
    text = format(time)
    counter = str(x) + "/" + str(y)
    canvas.draw_text(text, (50,110), 40, "white")
    canvas.draw_text(counter, (150,20), 20, "white")
    
    
# create frame
frame = simplegui.create_frame("Stopwatch: The Game", 200, 200)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw)
start_button = frame.add_button("Start", start_handler)
stop_button = frame.add_button("Stop", stop_handler)
reset_button = frame.add_button("Reset", reset_handler)

# start frame
frame.start()

# Please remember to review the grading rubric

