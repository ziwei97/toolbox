import pandas as pd
import boto3
import numpy as np

s3 = boto3.resource('s3')
dynamodb = boto3.resource('dynamodb')

#replace table name based on request
table_name = 'DFU_Master_ImageCollections'
table = dynamodb.Table(table_name)

#get attributes from dynamodb
def get_attribute(table,guid,attr):

    response = table.get_item(
        Key={
            'ImgCollGUID': guid
        }
    )
    # print(response)
    return response["Item"][attr]

df = pd.read_excel("/Users/ziweishi/Desktop/Matched_ImgCollGUID.xlsx")

list = df["ImgCollGUID"].to_list()
subjectid = df["SubjectID"].to_list()
visit_time = df["VisitTime"].to_list()

guid_list = []
subjectid_list=[]
visit_time_list=[]

a=0
for i in list:
    try:
        subset1 = i[1:-1]
        subset = subset1.split(", ")
        for j in subset:
            guid_list.append(j[1:-1])
            subjectid_list.append(subjectid[a])
            visit_time_list.append(visit_time[a])
    except:
        guid_list.append(np.nan)
        subjectid_list.append(subjectid[a])
        visit_time_list.append(visit_time[a])
    a+=1

assessing_list = []
q=0
for p in guid_list:
    print(q)
    try:
        assess = get_attribute(table,p,"Assessing")
        assessing_list.append(assess)
    except:
        assessing_list.append(np.nan)
    q+=1

data = zip(subjectid_list,visit_time_list,guid_list,assessing_list)
dfu_assessing_check = pd.DataFrame(data,columns=["SubjectID","VisitTime","GUID","Assessing_Image"])
dfu_assessing_check.to_excel("/Users/ziweishi/Desktop/dfu_assessing_check.xlsx")