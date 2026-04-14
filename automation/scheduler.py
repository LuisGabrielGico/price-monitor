import schedule
import time
from main import run

schedule.every(10).seconds.do(run)

print("Automation system initiated...")

try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("System intentionally shut down.")