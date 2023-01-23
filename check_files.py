import os
import pandas as pd


bts_path = "/Users/ziweishi/Data/RequestedData/data_for_skin_masks_20221222/BURN_BTS"
dfu_path = "/Users/ziweishi/Data/RequestedData/data_for_skin_masks_20221228/DFU"
#
# bts_list = os.listdir(bts_path)
# if ".DS_Store" in bts_list:
#     bts_list.remove(".DS_Store")
dfu_list = os.listdir(dfu_path)
if ".DS_Store" in dfu_list:
    dfu_list.remove(".DS_Store")
#
# bts_guid_list=[]
# bts_file_list=[]
# for i in bts_list:
#     file_path = os.path.join(bts_path,i)
#     file_list = os.listdir(file_path)
#     if ".DS_Store" in file_list:
#         file_list.remove(".DS_Store")
#     for j in file_list:
#         bts_guid_list.append(i)
#         bts_file_list.append(j)
# bts_final = zip(bts_guid_list,bts_file_list)
# bts_data = pd.DataFrame(bts_final,columns=["bts_guid","bts_file"])
# bts_data.to_csv("/Users/ziweishi/Desktop/bts.csv")




dfu_guid_list=[]
dfu_file_list=[]
for i in dfu_list:
    file_path = os.path.join(dfu_path,i)
    file_list = os.listdir(file_path)
    if ".DS_Store" in file_list:
        file_list.remove(".DS_Store")
    for j in file_list:
        dfu_guid_list.append(i)
        dfu_file_list.append(j)
dfu_final = zip(dfu_guid_list,dfu_file_list)
dfu_data = pd.DataFrame(dfu_final,columns=["dfu_guid","dfu_file"])
dfu_data.to_csv("/Users/ziweishi/Desktop/dfu.csv")