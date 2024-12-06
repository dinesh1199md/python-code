nested_json = {
    "user": {
        "id": 1,
        "name": "John",
        "address": {
            "city": "New York",
            "zip": "10001"
        },
        "orders": [123, 456]
    }
}


def jsob_flat(j,pat_key=''):
    d={}
    for k,v in j.items():
        n_key= f"{pat_key}.{k}" if pat_key else k
        if isinstance(v,dict):
            d.update(jsob_flat(v,n_key))
        elif isinstance(v,list):
            for i,item in enumerate(v):
                d[f"{n_key}.{i}"]=item
        else:
            d[n_key]=v
    return d
# print(jsob_flat(nested_json))


#filter based on key 
def jsob_filter(j,key):
    d=[]
    if isinstance(j,dict):
        for k,v in j.items():
                if k==key:
                    d.append(v)
                d.extend(jsob_filter(v,key))
    elif isinstance(j,list):
            for item in j:
                d.extend(jsob_filter(item,key))
    return d

print(jsob_filter(nested_json,"orders"))

# out=[]
# for i in ["orders","orders"]:
#     t=jsob_filter(nested_json,i)
#     out.extend(t[0])
# print(set(out))