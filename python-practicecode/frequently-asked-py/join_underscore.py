
def convert_to_str(l):
    # st=''
    # for i in l:
    #     st=st+ str(i)+"_"
    # return st
    return "_".join(str(num) for num in l)



l=[1,2,3,4,5,6,7]
print(convert_to_str(l))