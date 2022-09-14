import logging
import functools,time
from os.path import expanduser,join

def log(fun):
    functools.wraps(fun)
    def wrapper(*args,**kwargs):
        logger=logging.getLogger("execution_time_log")
        if not logger.hasHandlers():
            logger.setLevel(logging.INFO)
            filehandler=logging.FileHandler(join(expanduser("~"),"execution_time.log"))
            formatter=logging.Formatter('%(asctime)s - %(function_name)s - %(exec_time)f')
            filehandler.setFormatter(formatter)
            logger.addHandler(filehandler)
        start_time=time.time()
        called_return=fun(*args,**kwargs)
        end_time=time.time()
        logger.info(None,extra={'exec_time':end_time-start_time,'function_name':fun.__name__})
        return called_return
    return wrapper


# Examples

@log
def test1():
    time.sleep(10)

@log
def test2():
    time.sleep(20)
@log
def test3():
    time.sleep(15)


test1()
test2()
test3()
