import os
import shutil


t_mask_path = "/Users/ziweishi/Documents/p3_mask"
label_path = "/Users/ziweishi/Users/ziweishi/Data/phase3_label"


t_mask_list = os.listdir(t_mask_path)
label_list1=os.listdir(label_path)

if ".DS_Store" in t_mask_list:
    t_mask_list.remove(".DS_Store")

if ".DS_Store" in label_list1:
    label_list1.remove(".DS_Store")

label_list = [i for i in label_list1 if i in t_mask_list]
print(len(label_list))



for i in label_list:

    file_path = os.path.join(label_path,i)
    file_list = os.listdir(file_path)
    if ".DS_Store" in file_list:
        file_list.remove(".DS_Store")


    for z in file_list:
        print(type(z[0:5]))
        if z[0:5]=="Final":
            j="Label_"+z
            print(j)
            final_path = os.path.join(file_path,z)
            target_path_guid = os.path.join(t_mask_path,i)
            target_path = os.path.join(target_path_guid,j)
            shutil.copyfile(final_path, target_path)
