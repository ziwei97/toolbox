import boto3
import os
import pandas as pd

s3 = boto3.resource('s3')
dynamodb = boto3.resource('dynamodb')

#replace table name based on request
table_name = 'BURN_Master_ImageCollections'
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


def download_raw(table,raw_list,attrs):
    fold = os.path.join("/Users/ziweishi/Documents", "new_request_msi")
    os.makedirs(fold)
    for i in raw_list:
        name = get_attribute(table,i,"Bucket")
        folder = os.path.join(fold, i)
        os.makedirs(folder)
        for j in attrs:
            try:
                attr = get_attribute(table,i,j)
                # pathlib.Path(path).parent.mkdir(exist_ok=True, parents=True)
                path = os.path.join(folder, j)
                os.makedirs(path)
                for s in attr:
                    file_name = s.split('/')[-1]
                    file_path = os.path.join(path, file_name)
                    # s3.meta.client.download_file(name, attr[0], str(path))
                    s3.Bucket(name).download_file(str(s), str(file_path))
            except Exception as e:
                print(e.args)


# #input the guid list based on file path
data = pd.read_excel("/Users/ziweishi/Desktop/Book7.xlsx",sheet_name="Sheet1")
list =data["GUID"].to_list()

# #replace image type name
attrs = ["Raw","Assessing","PseudoColor","Reference"]

download_raw(table,list,attrs)



# s3 = boto3.resource('s3')
# dynamodb = boto3.resource('dynamodb')
# table_name = 'DFU_Master_ImageCollections'
# table = dynamodb.Table(table_name)
#
# data = pd.read_excel("/Users/ziweishi/Desktop/check_cja.xlsx",sheet_name="epoc")
# # df = data[data["SubjectID"].isin(["011-005","010-022","010-027"])]
# # df1=df[df["Status"]!="NaN"]
# # df2=df[["ImgCollGUID","SubjectID","Status"]]
# # table="DFU_Master_ImageCollections"
#
# guid_list = data["epoc_id"].to_list()
# print(len(guid_list))
#
# guid = []
# file = []
#
#
# for i in guid_list:
#
#     # raw_list=get_attribute(table,i,"Raw")
#     # for j in raw_list:
#     #     raw_name=j.split("/")[-1]
#     #     guid.append(i)
#     #     file.append(raw_name)
#
#
#     try:
#         ass = get_attribute(table,i,"Assessing")
#     except:
#         ass=["/none"]
#     for x in ass:
#         guid.append(i)
#         file.append(x.split("/")[-1])

    # try:
    #     mask = get_attribute(table,i,"Mask")
    # except:
    #     mask = ["/none"]
    #
    # for y in mask:
    #     guid.append(i)
    #     file.append(y.split("/")[-1])
    #
    # try:
    #     pse = get_attribute(table,i,"PseudoColor")
    # except:
    #     pse = ["/none"]
    #
    # for z in pse:
    #     guid.append(i)
    #     file.append(z.split("/")[-1])


# data = zip(guid,file)
# final=pd.DataFrame(data,columns=["guid","file"])
# final.to_csv("/Users/ziweishi/Documents/assessing.csv")


