import datetime
import time

time = time.time()
print(f"Seconds since January 1, 1970: {time} or {time:.2e} in scientific notation")

date = datetime.datetime.now()
year = date.strftime("%Y")
month = date.strftime("%B")
day = date.strftime("%d")
print(f"{month} {day} {year}")
