
import time
from multiprocessing import Process
# from multiprocessing.shared_memory import SharedMemory

shasqvalues=[]
def square_list(l):
     time.sleep(12)
     global sqvalues
     for i in l:
          print("square : ",i*i)
          sqvalues.append(i*i)
          '''with in thee function list can be stored'''
     print("Result with in the process :",sqvalues)     

def cube_list(l):
     time.sleep(12)
     for i in l:
        print("cube : ",i*i*i)
    #  return [i*i*i for i in l]

        
if __name__== "__main__":
    
    '''with thread call'''
    l=[2,3,8,9] 
    t=time.time()
    t1=Process(target=square_list,args=(l,))
    # t2=multiprocessing.Process(target=cube_list,args=(l,))
    t1.start()
    # t2.start()
    t1.join()
    # t2.join()
    print("work done : ",time.time()-t)
    '''this list will be empty, because each process have different memory addres space(virtual memory).
    the program variable will not be shares between two process. 
    we need to use IPC "INTERPROCESS COMMUNICATION" techque to share the data between two process
    possible instead it is printed with in the each function'''
#     print(sqvalues)
    print("Done")
     