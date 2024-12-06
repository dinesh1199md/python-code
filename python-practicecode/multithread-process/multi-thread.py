
import time 
import threading
sq_result=[]
def square_list(l):
     time.sleep(5)
     for i in l:
          print("square : ",i*i)
          sq_result.append(i*i)
    #  return [i*i for i in l]
def cube_list(l):
     time.sleep(5)
     for i in l:
        print("cube : ",i*i*i)
    #  return [i*i*i for i in l]

        
if __name__== "__main__":
    '''normal call'''
    # l=[2,3,8,9]
    # t=time.time()
    # square_list(l)
    # cube_list(l)
    # print("work done : ",time.time()-t)
    '''with thread call'''
    l=[2,3,8,9] 
    t=time.time()
    t1=threading.Thread(target=square_list,args=(l,))
    t2=threading.Thread(target=cube_list,args=(l,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print("work done : ",time.time()-t)
    print('square result',sq_result)
     