from datetime import datetime
import time

now=datetime.now()
start_time=datetime(now.year,now.month,now.day,now.hour,now.minute,now.second)
print(start_time)

end_time=datetime(2024,6,24)
print((end_time-now).days) #days 날짜만 출력
print(end_time-now) #날짜, 시간 출력
