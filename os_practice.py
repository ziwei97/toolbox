import os
import pathlib
import pandas as pd
import shutil

request = pd.read_excel("/Users/ziweishi/Desktop/Book5.xlsx",sheet_name="Sheet1")
request_list = request["ImgCollGUID"].to_list()

# path= "/Users/ziweishi/Documents/msi/BTS_data_2022-11-01/"
path= "/Users/ziweishi/Downloads/phase_1_msi"
path1 = "/Users/ziweishi/Documents/Phase_1_MSI"
# os.mkdir(path1)
list = os.listdir(path)
if ".DS_Store" in list:
    list.remove(".DS_Store")

for i in list:
    guid_path = os.path.join(path,i)
    new_path1 = os.path.join(path1,i)
    # os.makedirs(new_path1)
    file_list = os.listdir(guid_path)
    if ".DS_Store" in file_list:
        file_list.remove(".DS_Store")
    list_sort = sorted(file_list)
    msi = list_sort[1:2]
    msi_path = os.path.join(new_path1, "pseudo")
    os.makedirs(msi_path)
    for j in msi:
        old_path = os.path.join(guid_path,j)
        new_path=os.path.join(msi_path,j)
        shutil.move(old_path,new_path)



# df = pd.DataFrame(list,columns=["guid"])
# df.to_excel("/Users/ziweishi/Desktop/Book6.xlsx")
#
#
# os.mkdir('/Users/ziweishi/Users/ziweishi/Documents/msi/BTS_data_2022-11-01/MSI_Images')
#
# path_re = "/Users/ziweishi/Users/ziweishi/Documents/msi/BTS_data_2022-11-01/MSI_Images"
#
# for i in list:
#     if i in request_list:
#         new_path = os.path.join(path_re,i)
#         old_path = os.path.join(path,i)
#         shutil.move(old_path,new_path)







# os.mkdir('/Users/ziweishi/Documents/coding/try1')

from pathlib import Path

# Path('/Users/ziweishi/Documents/coding/').mkdir( parents=True, exist_ok=True )

# os.rmdir('/Users/ziweishi/Documents/coding/')
#
# path = "/Users/ziweishi/Data/RequestedData/mask_and_pseudocolor_202212"

# folder = os.listdir(path)
#
# if '.DS_Store' in folder:
#     folder.remove('.DS_Store')

# # burn = os.path.join(path,"BURN_BTS")
# epoc = "/Users/ziweishi/Data/RequestedData/mask_and_pseudocolor_202212"
# # burn_guid = os.listdir(burn)
# epoc_guid = os.listdir(epoc)


# burn_list=[]
# burn_list_content=[]
# epoc_list=[]
# epoc_list_content=[]

# for i in burn_guid:
#     if '.DS_Store' in burn_guid:
#         burn_guid.remove('.DS_Store')
#         print(len(burn_guid))
#     path = os.path.join(burn,i)
#     path_list = os.listdir(path)
#     if '.DS_Store' in path_list:
#         path_list.remove('.DS_Store')
#     for j in path_list:
#         burn_list.append(i)
#         burn_list_content.append(j)
# print(len(burn_list))
#
# for i in epoc_guid:
#     if '.DS_Store' in epoc_guid:
#         epoc_guid.remove('.DS_Store')
#     path_epoc = os.path.join(epoc, i)
#     path_list = os.listdir(path_epoc)
#     if '.DS_Store' in path_list:
#         path_list.remove('.DS_Store')
#     for j in path_list:
#         epoc_list.append(i)
#         epoc_list_content.append(j)
#
# # data1 = zip(burn_list,burn_list_content)
# # final1 = pd.DataFrame(data1, columns=['name','content'])
#
# data2 = zip(epoc_list,epoc_list_content)
# final2 = pd.DataFrame(data2, columns=['name','content'])
#
#
# # final1.to_csv("/Users/ziweishi/Documents/burn_bts.csv")
# final2.to_csv("/Users/ziweishi/Documents/burn_epoc.csv")