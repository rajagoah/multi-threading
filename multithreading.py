import threading

def calc(num1,num2):
    return num1*num2

def calc_2(num1,num2):
    return num1-num2

if __name__=="__main__":
    t1 = threading.Thread(target=calc, args=(3,2))
    t2 = threading.Thread(target=calc, args=(1, 2))

    t1.start()
    print("t1 started")
    t2.start()
    print("t2 started")
    x = t1.join()
    y = t2.join()
    print(x,y)
    print('success')