import time
from plyer import notification
if __name__=="__main__":
    while True:
        notification.notify(
            title = "Please drink water Prashish",
            message = "Boy you gotta stay hydrated",  
            timeout = 10
            )
        time.sleep(1800) 
