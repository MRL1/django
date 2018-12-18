# 时间的常用模块
# calendar——日历
import calendar
import time
import datetime
cal = calendar.calendar(2018)
print(cal)

cal1 = calendar.calendar(2018,l=0,c=5)
print(cal1)

# 判断某一年是否是闰年
print(calendar.isleap(2019))

# 获取指定年份之间的闰年个数
print(calendar.leapdays(1995, 2018))

# 获取某个月的日历字符串
m = calendar.month(2017,8)
print(m)

# time模块
# 得到时间戳
t = time.time()
print(t)

# 得到当前的时间结构
lt = time.localtime()
print(lt)

# 返回元祖的正常字符串化的时间结构
tt = time.asctime(lt)
print(tt)

# 获取字符串化的当前时间
print(time.ctime())
print(type(time.ctime()))

# 使用时间元祖获取对应的时间戳
llt = time.localtime()
ttt = time.mktime(llt)
print(ttt)

# sleep:使程序进入睡眠，N秒后继续
def sleep():
    for i in range(1,10):
        print(i)
        time.sleep(1)
#sleep()

# 将时间元祖转化为自定义的字符串格式 2018年12月18日  11:43
lt2 = time.localtime()
ft = time.strftime('%Y{0}%m{1}%d{2} %H:%M').format('年', '月','日')
print(ft)




# datatime模块
print(datetime.date(2018,12,18))

print(datetime.datetime)
print(datetime.datetime.now())
print(datetime.datetime.today())