def mean_tuple(num):
    result=[ sum(x)/len(x) for x in zip(num)]
    return result

print(mean_tuple([1,2,3,4]))
# print(mean_tuple()) 

tup=(1,2,3,4)
a=tuple()
# print(tup,a)


class NameClass:
    def __init__(self) -> None:
        # self.name=n
        pass
    def display(self):
        print(f'print statement')

obj1=NameClass()
obj1.display()