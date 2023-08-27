# 문자를 날짜로
from datetime import datetime
print(datetime.strptime('05:34','%H:%M')) # 1900-01-01 05:34:00

# 날짜끼리의 차 구하기
import datetime
day1 = datetime.datetime(2016,1,1)
day2 = datetime.datetime(2016,2,1)
print(day2-day1)        # 31 days, 0:00:00
print((day2-day1).days) # 31