import pandas as pd
import download_request
import boto3
s3 = boto3.resource('s3')
dynamodb = boto3.resource('dynamodb')
table_name = 'BURN_Master_ImageCollections'
table = dynamodb.Table(table_name)

df = pd.read_csv("/Users/ziweishi/Documents/database/BURN_Master_ImageCollections.csv")

df1 = df[df["StudyName"]=="BURN_ePOC"]
df2 = df1[df1["Status"]=="acquired"]


print(len(df2))

list_df2 = df2["ImgCollGUID"].to_list()

name_list=[]
mask_list=[]

for i in list_df2:
    files = download_request.get_attribute(table,i,"Mask")
    for j in files:
        name_list.append(i)
        mask_list.append(j)



data_tuples = zip(name_list,mask_list)
final = pd.DataFrame(data_tuples, columns=["guid","Mask"])
final.to_csv("/Users/ziweishi/Documents/checking.csv",encoding='utf-8')