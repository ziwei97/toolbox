import pandas as pd
import boto3

data = pd.read_excel("/Users/ziweishi/Desktop/Book1.xlsx",sheet_name="epoc_s3")

list = data["ImgCollGUID"].to_list()
# burnNum_pat_loc, BurnIndex

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('BURN_Master_ImageCollections')
# site = []
# DeviceType = []
# ImageCollTime = []
# ImageCollectionID = []
# JsonFileName = []
# burnindex=[]
# subjectid = []
# burnNum_pat_loc = []

Agreement = []
Final = []



import datetime

for i in list:
    response = table.get_item(
        Key={
            'ImgCollGUID': i
        }
    )
    try:
        Agreement.append(response["Item"]["Agreement"])
    except:
        Agreement.append("No Final Truth")

    try:
        Final.append(response["Item"]["FinalTruth"])
    except:
        Final.append("No path")


    # try:
    #     site.append(response["Item"]["Site"])
    #
    # except:
    #     site.append(" ")
    #
    # try:
    #     DeviceType.append(response["Item"]["DeviceType"])
    # except:
    #     DeviceType.append(" ")
    #
    # try:
    #     date1 = response["Item"]["CaptureDate"]
    #     date_string = datetime.datetime.year(date1)+'-'+datetime.datetime.month(date1)+'-'+datetime.datetime.day(date1)
    #     date_time_string = datetime.datetime.hour(date1)+'.'+datetime.datetime.minute(date1)+'.'+datetime.datetime.second(date1)
    #     string_time = date_string+'_'+date_time_string
    #     ImageCollTime.append(string_time)
    # except:
    #     raw = str(response["Item"]["Raw"])
    #     final = raw.replace('[','').replace(']','').split(',')
    #     final = sorted(final)
    #
    #     p = final[0][-29:-10]
    #
    #     ImageCollTime.append(p)
    #
    # # try:
    # #     ImageCollectionID.append(response["Item"]["ImageCollectionID"])
    # # except:
    # #     ImageCollectionID.append(" ")
    #
    # try:
    #     JsonFileName.append(response["Item"]["JsonFileName"])
    # except:
    #     JsonFileName.append(" ")
    #
    # try:
    #     burnindex.append(response["Item"]["Wound"])
    # except:
    #     burnindex.append(" ")
    #
    # try:
    #     subjectid.append(response["Item"]["SubjectID"])
    # except:
    #
    #     subjectid.append(" ")
    #
    # try:
    #     burnnum=response["Item"]["SubjectID"]
    #     pat = response["Item"]["AnatomicalLocation"]
    #     wound = response["Item"]["Wound"]
    #     loc = response["Item"]["DeviceType"]
    #     burnNum_pat_loc_1 = "('"+burnnum+"','"+pat+"','"+wound+"','"+loc+"')"
    #     burnNum_pat_loc.append(burnNum_pat_loc_1)
    # except:
    #     burnNum_pat_loc.append(' ')


# print(site)
# print(DeviceType)
# print(ImageCollTime)
# print(ImageCollectionID)

# print(len(site))
# print(len(DeviceType))
# print(len(ImageCollTime))
# print(len(ImageCollectionID))
# print(len(JsonFileName))



# final =pd.DataFrame()
# final['ImgCollGUID']=list
# final['Site']=site
# final['DeviceType']=DeviceType
# final['ImageCollTime']=ImageCollTime
# final['ImageCollectionID']=ImageCollectionID
# final['JsonFileName'] = JsonFileName

# JsonFile = []
#
# for c in JsonFileName:
#     c1 = c + ".json"
#     JsonFile.append(c1)


data_tuples = zip(list,Agreement,Final)
final = pd.DataFrame(data_tuples, columns=['Guid','Agreement','FinalTruth'])
final.to_csv("//Users/ziweishi/Documents/final.csv",encoding='utf-8')
# datatime = []