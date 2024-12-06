#flat dict
def flat_dic(nd,pat_key='',sep='.'):
    d={}
    for k,v in nd.items():
        new_key= f"{pat_key}{sep}{k}" if pat_key else k
        if isinstance(v,dict):
            d.update(flat_dic(v,new_key,sep))
        else:
            d[new_key]=v
    return d     
nd = {'a': 1, 'b': {'c': 2, 'd': 3}}
print(flat_dic(nd))



d={'a': 1, 'b.c': 2, 'b.d': 3}
for k,v in d.items():
    # print(k)
    if 'c' in k:
        print({k:d[k]})
        
print(sum(d.values()))


#dict values in list
def flat_dic2(nd,pat_key=''):
    d={}
    for k,v in nd.items():
        new_key= f"{pat_key}.{k}" if pat_key else k
        if isinstance(v,dict):
            d.update(flat_dic2(v,new_key))
        elif isinstance(v, list):
            for i,item in enumerate(v):
                d[f"{new_key}.{i}"]=item
        else:
            d[new_key]=v
    return d     
nd = {'a': [1, 2], 'b': {'c': [3, 4]}}

print(flat_dic2(nd))
    

