
import pandas as pd
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, 6],
    'C': [7, 8, 9]
})

'''getting all columns'''
# print(df.columns.tolist())

'''getting single column by index'''
# print(df.columns[1])

'''rename columns'''
df.rename(columns={'A':"first_column",'B':"SECOND_column"},inplace=True)
# print(df.columns.tolist())
# print(df)

new_column_names = ['New_A', 'New_B', 'New_C']
df.columns=new_column_names
# print(df)


# ------------------------------------------------------------
# Method2
data = {
    'Column1': [1, 2, 3],
    'Column2': [4, 5, 6],
    'Column3': [7, 8, 9]
}

df2=pd.DataFrame(data,columns=["New1","New2","New3"])
# print(df2)
print("-------Info------------")
print(df.info())
print("-------describe------------")
print(df.describe())