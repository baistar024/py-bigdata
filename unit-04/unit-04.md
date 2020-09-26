## 日期和时间类型

### datetime模块
    datetime 模块提供用于处理日期和时间的类。在支持日期时间数学运算的同时，实现的关注点更着重于如何能够更有效地解析其属性用于格式化输出和数据操作。
    日期和时间对象可以根据它们是否包含时区信息而分为“感知型”和“简单型”两类。
#### 确定一个对象是感知型还是简单型
    date 类型的对象都是简单型的。 
       
    time 或 datetime 类型的对象可以是感知型或者简单型。    
    一个 datetime 对象 d 在以下条件同时成立时将是感知型的：    
    d.tzinfo 不为 None    
    d.tzinfo.utcoffset(d) 不返回 None    
    在其他情况下，d 将是简单型的。
    
    一个 time 对象 t 在以下条件同时成立时将是感知型的：    
    t.tzinfo 不为 None    
    t.tzinfo.utcoffset(None) 不返回 None。    
    在其他情况下，t 将是简单型的。    
    感知型和简单型之间的区别不适用于 timedelta 对象。
    
####　datetime常量
    datetime.MINYEAR和datetime.MAXYEAR

#### datetime有效类
    class datetime.date
    一个理想化的简单型日期，它假设当今的公历在过去和未来永远有效。 
    属性: year, month, day。
    
    class datetime.time
    一个独立于任何特定日期的理想化时间，它假设每一天都恰好等于 24*60*60 秒。 （这里没有“闰秒”的概念。） 
    包含属性: hour, minute, second, microsecond 和 tzinfo。
    
    class datetime.datetime
    日期和时间的结合。
    属性：year, month, day, hour, minute, second, microsecond, and tzinfo.
    
    class datetime.timedelta
    表示两个 date 对象或者 time 对象,或者 datetime 对象之间的时间间隔，精确到微秒。
    
    class datetime.tzinfo
    一个描述时区信息对象的抽象基类。
    用来给 datetime 和 time 类提供自定义的时间调整概念（例如处理时区和/或夏令时）。
    
    class datetime.timezone
    一个实现了 tzinfo 抽象基类的子类，用于表示相对于 世界标准时间（UTC）的偏移量。
    
    子类关系
    object
    timedelta
    tzinfo
        timezone
    time
    date
        datetime

### date对象
    date 对象代表一个理想化历法中的日期（年、月和日），即当今的格列高利历向前后两个方向无限延伸
    1，date对象创建
        方法一：date = datetime.date(y,m,d)
        方法二: date = datetime.today()
        方法三: date = datetime.fromtimestamp(timestamp)
        方法四: date = datetime.fromisoformat("date-string)
        方法五: date = dateteim.fromordinal(ordinal)
    2.date对象的属性
    date.min == date(MINYEAR, 1, 1)
    date.max == date(MAXYEAR, 12, 31)
    date.resolution两个日期对象的最小间隔
    date.year
    date.month
    date.day
    3. 支持的运算
    date2 = date1 + timedelta
    date2 = date1 = timedelta
    timedelta = date1- date2 
    date1 < date2    date1在前成立 
    4.date实例方法
    date.replace(year= , nonth = , day = )    更新日期
    date.timetuple()    返回时：分：秒: 秒
    date.toordinal()    返回日期的预期格列高利历序号，其中公元 1 年 1 月 1 日的序号为 1
    date.weekday()      返回一个整数代表星期几，星期一为0，星期天为6。
    date.isoweekday()   返回一个整数代表星期几，星期一为1，星期天为7。
    date.isoclendar()   返回一个三元元组，(ISO year, ISO week number, ISO weekday) 。
    date.isoformat      返回一个以 ISO 8601 格式 YYYY-MM-DD 来表示日期的字符串:
    date.__str__()      对于日期对象d, str(d)
    date.ctime()  == time.ctime(time.mktime(d.timetuple))   返回一个表示日期的字符串:
    date.strftime(format)   返回一个由显式格式字符串所指明的代表日期的字符串。
    date.__format__(format) 与 date.strftime() 相同

##　time对象
    一个 time 对象代表某日的（本地）时间，它独立于任何特定日期，并可通过 tzinfo 对象来调整。
    1. time对象的定义
    datetime.time(h= , m= ,micros = , tz=none, *, fold=0) 所有参数是可选
    date.time.fromisoformat(time-string) "HH:MM:SS.ffffff"
    
    2. 类属性
    time.min 最早的时间， time(0,0,0,0)
    time.max 最晚的时间， time(23,59,59, 999999)
    time.resolution 时间精度 timedelta(microsencond = 1)
    3. 实例属性
    time.hour
    time.minute
    time.second
    time.microsencond
    time.tzinfo
    time.fold
    4.实例方法
    time.replace(h, m, s, ms, tz, fold)
    返回一个具有同样属性值的 time，除非通过任何关键字参数指定了某些属性值。 
    请注意可以通过指定 tzinfo=None 从一个感知型 time 创建一个简单型 time，而不必转换时间数据。
    
    time.isoformat(timespec = 'auto')
    返回表示为下列 ISO 8601 格式之一的时间字符串：
    
    time.__str__() == str(time)
    对于时间对象 t, str(t) 等价于 t.isoformat()
    
    time.strftime(format)
    返回一个由显式格式字符串所指明的代表时间的字符串。
    
    time.__format__(format)
    与 time.strftime() 相同。 此方法使得为 time 对象指定以 格式化字符串字面值 
    表示的格式化字符串以及使用 str.format() 进行格式化成为可能。 
    要获取格式指令的完整列表，请参阅 strftime() 和 strptime() 的行为。
    
    time.utcoffset()
    如果 tzinfo 为 None，则返回 None，否则返回 self.tzinfo.utcoffset(None)，
    并且在后者不返回 None 或一个幅度小于一天的 a timedelta 对象时将引发异常。
    
    time.dst
    time.tzname()
    如果 tzinfo 为 None，则返回 None，否则返回 self.tzinfo.tzname(None)，
    如果后者不返回 None 或者一个字符串对象则将引发异常。
    
## datetim对象
    datetime 对象是包含来自 date 对象和 time 对象的所有信息的单一对象。
    1. 创建datetime对象
        方法一：date.datetime(y,m,d,h,m,s,ms,tz, fold)
        方法二：datetime.today()    返回表示当前地方时的 datetime 对象，其中 tzinfo 为 None。 
        方法三: datetime.now()     返回表示当前地方时的 date 和 time 对象。
        方法四: datetime.utcnow()  返回表示当前 UTC 时间的 date 和 time，其中 tzinfo 为 None。
        方法五： datetime.formtimestamp(timestamp, tz)    
        方法六: datetime.utcfromtimestamp(timestamp)
        方法七: datetime.fromordinal(ordinal)
        方法八: datetime.combine(date, time, tz)
        方法十: datetime.fromisoformat(date-string)
        方法十一： datetime.fromisocalendar(y,w,d)
        方法十二: datetime.strptime(date-string, format)
    2. 类属性
    datetime.min
    datetime.max
    datetime.resolution
    datetime.year
    datetime.month
    datetime.day
    datetime.hour
    datetime.minute
    datetime.second
    datetime.microsencond
    datetime.tzinfo
    datetime.fold
    3. 支持运算
        dt2 = dt1 + td
        dt2 = dt1 - td
        td = dt2 - dt1
        dt1 < dt2
    4. 实例方法
        datetime.date()  ==>date  
        datetime.time()  ==>time
        datetime.timetz()  ==>time
        datetime.replace(y,m,d,h,m,s,ms,tz,fold)
        datetime.astimezone(tz=None)
        datetime.utcoffset()
        datetime.dst()
        dateeimt.tzname()
        datetime.timetuple()
        datetime.utctimetuple()
        datetime.toordinal()
        datetime.timestamp()
        datetime.weekday()
        datetime.isoformat()
        datetime.__str__()
        datetime.ctime()
        datetime.strftime()
        datetime.__format__()
        
        
        
        
    
    