# Created by Yasir khalid
# Purpose was to parse .json files from Postman to analyze platform's registration data

import json
import pandas as pd

with open('./Datasets/response.json') as f:
    data = json.load(f)

courseID = []
createDate = []
courseName= []

temp = data["data"]
for x in temp:
    print("Course ID: ", x["_id"])
    courseID.append(x["_id"])
    print("Created At: ", x["createdAt"])
    createDate.append(x["createdAt"])
    print("Name: ", x["name"])
    courseName.append(x["name"])
    print()
    
export = { "Course ID": courseID,
          "Created at": createDate,
          "Name": courseName
    }

courseIDs = pd.DataFrame(export)
courseIDs.to_csv("course-IDs.csv") 
