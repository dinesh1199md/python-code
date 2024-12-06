'''to create file with "w" '''
# with open("myfiles","w") as file:
#     conten=file.writelines("helo this is Dinesh Murugesan from salem")

'''to append the already existing file'''
# with open("myfiles","a") as file:
#     conten=file.writelines("Hello this is 2nd time")


'''to read the files'''
with open("myfiles","r") as file:
    # content=file.seek(10) #move the cuesor in 10 byte position 
    content=file.read()
    # print(content)

'''to read the files line by line'''
with open("myfiles","r") as file:
    content=file.read()
    for line in content:
        pass
        # print(line,end="")


'''file operation Exception'''
# try:
#     with open("dineshfile","r") as file:
#         content=file.read()
# except FileNotFoundError:
#     print("File Not found")
# except IOError:
#     print("An I/O error occurred")    
# except Exception as e:
#     print(e)

'''Read csv file'''
import csv
with open(r"C:\Users\dinesh.murugesan02\OneDrive - Infosys Limited\datascience-python\test_csv_file.csv",'r') as csvfile:
    reader=csv.reader(csvfile)
    for row in reader:
        pass
        # print(row)

'''write csv file'''
import csv
with open("write_csv",'w',newline="") as csvfile:
    writter=csv.writer(csvfile) 
    writter.writerow(["col1","col2","col3"])
    writter.writerow(["value","value2","value3"])

'''writting the json file'''
import json
with open("jsonfile",'w') as jsonfile:
    json.dump({"name":"dinesh","place":"salem","age":25},jsonfile)
    #json.dumps({"name":"dinesh","place":"salem","age":25})

with open("jsonfile",'r') as jsonfile:
    data=json.load(jsonfile)
    print(data)




