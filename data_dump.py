import pymongo
import pandas as pd
import json

from sensor.config import mongo_client


DATABASE_NAME= "aps"
COLLECTION_NAME= "sensor"
DATA_FILE_PATH= "/config/workspace/aps_failure_training_set1.csv"


if __name__=="__main__":
    df= pd.read_csv(DATA_FILE_PATH)
    print(f"No. of rows and columns are:",{df.shape})

    # Convert Data frame to JSON so that we can store the data in MongoDB

    df.reset_index(inplace=True, drop=True)

    json_record= list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    #Inserting the records to Mongo DB

    mongo_client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)





