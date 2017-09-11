# -*- coding: utf-8 -*-


from datetime import datetime, timedelta, timezone

# 获取当前datetime
now = datetime.now()
print(now)
print(type(now))

# 指定时间创建datetime
dt = datetime(2017, 9, 11, 15, 40)
print(dt)

# datetime转换为timestamp
print(dt.timestamp())

# 把timestamp转换为datetime:
t = dt.timestamp()
print(datetime.fromtimestamp(t))
print(datetime.utcfromtimestamp(t))

# 从str读取datetime
cday = datetime.strptime('2017-09-11 17:20:30', '%Y-%m-%d %H:%M:%S')
print(cday)

# 把datetime格式化输出:
print('strftime:', cday.strftime('%a, %b %d %H:%M'))

# 对日期进行加减:
print('current datetime =', cday)
print('current + 10 hours =', cday + timedelta(hours=10))
print('current - 1 day =', cday - timedelta(days=1))
print('current + 2.5 days =', cday + timedelta(days=2, hours=12))

# 把时间从UTC+0时区转换为UTC+8:
utc_dt = datetime.utcnow().replace(tzinfo=timezone.utc)
utc8_dt = utc_dt.astimezone(timezone(timedelta(hours=8)))
print('UTC+0:00 now =', utc_dt)
print('UTC+8:00 now =', utc8_dt)