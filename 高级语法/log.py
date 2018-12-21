# 简单的日志输出
import logging

# logging模块提供的日志记录函数所使用的日志器设置的日志级别是WARNING，
# 因此只有WARNING级别的日志记录以及大于它的ERROR和CRITICAL级别的日志记录被输出了，
# 而小于它的DEBUG和INFO级别的日志记录被丢弃了。
LOG_FORMATE = '%(asctime)s----%(levelname)s----%(message)s'
DATE_FORMATE = '%Y/%m/%d %H:%M:%S'
logging.basicConfig(filename='my.log', level=logging.DEBUG, format=LOG_FORMATE, datefmt=DATE_FORMATE)
logging.debug('this is a debug message')
logging.info('this is a info message')
logging.warning('this is a warning message')
logging.error('this is error message')
logging.critical('this is a critical message')


# logging.log(logging.DEBUG, 'this is a debug message')
# logging.log(logging.INFO,'this is a info message')
# logging.log(logging.WARNING,'this is a warning message')
# logging.log(logging.ERROR, 'this is a error message')
# logging.log(logging.CRITICAL, 'this is a critical message')