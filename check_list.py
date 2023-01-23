import json
from json import JSONDecoder, JSONDecodeError
import re

with open("/Users/ziweishi/Downloads/database_json/ePOC_ImageCollection.json") as openfile:
    for line in openfile:
        json_object = json.load(line)
        print(json_object)
