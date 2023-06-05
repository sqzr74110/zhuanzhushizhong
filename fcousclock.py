import time

def focus_timer(duration):
    start_time = time.time()
    end_time = start_time + duration
    while time.time() < end_time:
        time_left = end_time - time.time()
        mins, secs = divmod(time_left, 60)
        timer = '{:02d}:{:02d}'.format(int(mins), int(secs))
        print(timer, end="\r")
        time.sleep(1)
    print('时间到！')

focus_timer(25*60) # 25分钟
