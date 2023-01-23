import os
import pandas as pd
import download_request
import boto3

s3 = boto3.resource('s3')
dynamodb = boto3.resource('dynamodb')
table_name = 'DFU_Master_ImageCollections'
table = dynamodb.Table(table_name)

data = pd.read_csv("/Users/ziweishi/Documents/database/DFU_Master_ImageCollections.csv")
df = data[data["SubjectID"].isin(["011-005","010-022","010-027"])]
# df1=df[df["Status"]!="NaN"]
df2=df[["ImgCollGUID","SubjectID","Status"]]
table="DFU_Master_ImageCollections"

guid_list = df2["ImgCollGUID"].to_list()
print(len(guid_list))

guid = []
file = []


for i in guid_list:

    raw_list=download_request.get_attribute(table,i,"Raw")
    for j in raw_list:
        raw_name=j.split("/")[-1]
        guid.append(i)
        file.append(raw_name)


    try:
        ass = download_request.get_attribute(table,i,"Assessing")
    except:
        ass=["/none"]
    for x in ass:
        guid.append(i)
        file.append(x.split("/")[-1])

    try:
        mask = download_request.get_attribute(table,i,"Mask")
    except:
        mask = ["/none"]

    for y in mask:
        guid.append(i)
        file.append(y.split("/")[-1])

    try:
        pse = download_request.get_attribute(table,i,"PseudoColor")
    except:
        pse = ["/none"]

    for z in pse:
        guid.append(i)
        file.append(z.split("/")[-1])


data = zip(guid,file)
final=pd.DataFrame(data,columns=["guid","file"])
final.to_csv("/Users/ziweishi/Documents/final.csv")