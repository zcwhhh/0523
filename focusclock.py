import time

def countdown(timer):
    while timer:
        mins, secs = divmod(timer, 60)
        timeformat = '{:02d}:{:02d}'。format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        timer -= 1

    print('Time is up!')

def focus_timer(focus_time, break_time):
    while True:
        print("Focus for {} minutes"。format(focus_time))
        countdown(focus_time * 60)

        print("Take a break for {} minutes"。format(break_time))
        countdown(break_time * 60)

if __name__ == '__main__':
    focus_time = 25
    break_time = 5
    focus_timer(focus_time, break_time)
