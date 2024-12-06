import pandas as pd

mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3,7,2],
  'City':["salem","chennai","bamgalore"]
}
myvar = pd.DataFrame(mydataset)
# print(myvar)
'''#to print specific colunm'''
# print(myvar[["cars","City"]]) 
'''#fillter colunm based on condtion''' 
# print(myvar[myvar["passings"]>3]) 

'''#missing value'''
# print(myvar.fillna(myvar.mean(),inplace=True))
# print(myvar)

'''group by'''
# groupby=myvar.groupby("City")['passings'].mean()
# print(groupby)

'''Creat CSV'''
myvar.to_csv("test_csv_file.csv")
'''read CSV'''
df=pd.read_csv(r"C:\Users\dinesh.murugesan02\OneDrive - Infosys Limited\datascience-python\test_csv_file.csv")
# print(df.head()) #head show first few rows

'''merge 2 df'''
df1=pd.DataFrame({"ID":[1,2,3],"name":["dinesh","ganesh","don"]})
df2=pd.DataFrame({"ID":[1,2,4],"name":["dinesh","ganesh", "don"]})

# mergedf=pd.merge(df1, df2,on="ID").reset_index(drop=True)
# print(mergedf)

# print(df1)

'''sort df '''
# sorted_df=df1.sort_values(by="ID",ascending=False)
# print(sorted_df)

'''redet index'''
# RESETINDEX_df=df1[df1["ID"]>2].reset_index(drop=True)
# print(RESETINDEX_df)

'''APPLY'''
df2["ID"]=df2["ID"].apply(lambda X:X+5)
print(df2["ID"])