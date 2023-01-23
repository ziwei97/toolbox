import os
import pandas as pd

path = "/Users/ziweishi/Users/ziweishi/Downloads/lowBrightness"

check_list_1 = os.listdir(path)
if ".DS_Store" in check_list_1:
    check_list_1.remove(".DS_Store")

guid=[]
file=[]
type=[]
num = []

for i in check_list_1:
    path_new = os.path.join(path,i)
    # path_latest = os.path.join(path_new,"MSI")
    list_new = os.listdir(path_new)
    if ".DS_Store" in list_new:
        list_new.remove(".DS_Store")
    a=0
    for j in list_new:
        guid.append(i)
        file.append(j)
        type.append((j.split("_"))[0])
        a+=1
        num.append(a)

data = zip(guid,file,type,num)
final = pd.DataFrame(data,columns=["guid","file","type","num"])
final.to_csv("/Users/ziweishi/Documents/list.csv")

# name=[]
# for i in check_list_1:
#     for j in range(20):
#         name.append(i)

#
# final = pd.DataFrame(name,columns=["name"])
# final.to_csv("/Users/ziweishi/Documents/check.csv")

# l = [6,2,3,4,5]
# l1=sorted(l)
# print(l1)