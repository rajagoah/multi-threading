import threading
from time import time
import logging

def calc(num1,num2):
    return num1*num2

def calc_2(num1,num2):
    return num1-num2

if __name__=="__main__":
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    ts = time()
    logger.info(" The session is starting %s:", ts)
    t1 = threading.Thread(target=calc, args=(3,2))
    t2 = threading.Thread(target=calc, args=(1, 2))

    t1.start()
    print("t1 started")
    t2.start()
    print("t2 started")
    x = t1.join()
    y = t2.join()
    print(x,y)

    logger.info(" The session has ended %s:", time()-ts)