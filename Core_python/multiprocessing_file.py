"""Mutliprocessing"""
from multiprocessing import Process,Pool
from functools import partial

class mprocessing:
    def task1(self,list_data,alapha_data):
        partial_task=partial(self.task2,alapha_data=alapha_data)
        with Pool(5) as pool:
            pool.map(partial_task,list_data)
     
    def task2(self,list_data,alapha_data):
        print(list_data,alapha_data)


def main():
    l1=list(range(5))
    a1="abcde"
    a2="fghij"
    mp=mprocessing()
    p1=Process(target=mp.task1,args=(l1,a1))
    p2=Process(target=mp.task1,args=(l1,a2))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    
if __name__ == "__main__":
    main()


