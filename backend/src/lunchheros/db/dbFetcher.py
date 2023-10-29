import numpy as np
import pandas as pd
import json
import os 

                

 
async def get_encoded_data(time_slot: int, location: str, data):
    print("get_encoded_data")
    # Transform data
    #print(f"Data {time_slot} {location} {data}")
    #df = pd.DataFrame(data)

    
    # One-hot encode data
    #one_hot_encoded_df = pd.get_dummies(df, columns=['WIP'])  # wip - replace with actual column names
    #one_hot_encoded_df.to_dict(orient='records') 
    
    #return one_hot_encoded_df


def parse_user_id_tolist(test_data):
    data = json.loads(test_data)

    # Extract the id values into a python list
    ids = [x['id'] for x in data]

    # Convert the python list to a numpy array
    numpy_array = np.array(ids).tolist()

    return numpy_array
