import pandas as pd
mydataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}
# myvar = pd.DataFrame(mydataset)
# print(myvar)


# import pandas as pd
technologies = {
    'Courses':["Spark","PySpark","Hadoop","Python","pandas"],
    'Fee' :[20000,25000,26000,22000,24000],
    'Duration':['30day','40days','35days','40days','60days'],
    'Discount':[1000,2300,1200,2500,2000]
              }
df = pd.DataFrame(technologies)
# print(df)
'''# Select Single Column by label'''
# print(df.loc[:,"Courses"])
'''# # Select Single Column by Index'''
# print(df.iloc[:,0])

'''# Using Conditions'''
# print(df.loc[df['Fee'] >= 24000])
# print(df.iloc[list(df['Fee'] >= 24000)])
'''
# Select multiple rows by Index'''
# print(df.iloc[[1,2]])

'''re seting the index'''
index_labels=['r1','r2','r3','r4','r5']
df["lb"]=index_labels
df=df.set_index("lb")

'''# Select multiple rows by Index'''
print(df.loc[['r1','r2']])

'''Select Single rows by Index'''
print(df.loc[['r1']])








df22=pd.DataFrame({ 'A':[1,2,3],'B':[4,5,6],})
print(df22)

print(df22)
'''apply'''
# new=df22.apply(lambda x:x.max()-x.min())
# print(new)

'''apply works on a row / column basis of a DataFrame
applymap works element-wise on a DataFrame
map works element-wise on a Series'''

new2=df22.applymap(lambda x: x % 2)
print(new2)

