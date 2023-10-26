import os 
import requests
import pandas as pd
import pickle


#### VARS ####

data_path="data"
raw_data_filename = "german_credit_data_biased_training.csv"
raw_data_path=os.path.join(data_path,raw_data_filename)

train_data_filename = "train_gcr.csv"
test_data_filename = "test_gcr.csv"
train_data_path=os.path.join(data_path,train_data_filename)
test_data_path=os.path.join(data_path,test_data_filename)

pipeline_filename = "feature_encode.pkl"
pipeline_path = os.path.join(data_path, pipeline_filename)

model_name="credit_risk_prediction"
model_path = os.path.join(data_path, model_name+".pkl")

deployment_name="credit_risk_prediction"

deployment_space_id_DEV="c4238e9c-1cbd-4776-aa6e-4f6b1f865ed1"
deployment_space_id_PROD="c4238e9c-1cbd-4776-aa6e-4f6b1f865ed1"

#### UTILS ####

def download_data_to_filesystem(raw_data_path):
    """
    Download the german_credit_data_biased_training.csv data from a given URL and save it to the specified file path.

    Parameters:
    - raw_data_path (str): Destination path where the CSV will be saved.
    """
    url = "https://raw.githubusercontent.com/IBM/monitor-wml-model-with-watson-openscale/master/data/german_credit_data_biased_training.csv"
    response = requests.get(url)

    # Check if the request was successful
    if response.status_code == 200:
        
        # Ensure the directory exists
        directory = os.path.dirname(raw_data_path)
        if not os.path.exists(directory):
            os.makedirs(directory)

        # Write the content to the file
        with open(raw_data_path, "wb") as file:
            file.write(response.content)
        print("Downloaded and saved as "+raw_data_path)
    else:
        print("Failed to download the CSV file. Status code:", response.status_code)
        
        
def check_for_file_in_filesystem(path):
    """
    Check existence of path in filesystem
    """
    if os.path.exists(path):
        return True
    else:
        print("File not found in specified path.")
        return False   


def load_model(filename):
    """
    Load model from the specified file path.

    Parameters:
    - filename (str): Path to the model file.

    Returns:
    - object: The deserialized model/pipeline object.
    """
    check_for_file_in_filesystem(filename)
    with open (filename,"rb") as f:
        pipeline = pickle.load(f)
    return pipeline


def load_data_from_db2():
    '''
    currently not implemented due to issues with the flight service
    '''
    # data_request = {
    #         'connection_name': """DB2_DATA""",
    #         'interaction_properties': {
    #             'select_statement': 'SELECT * FROM "CUSTOMER_DATA"."GERMAN_CREDIT_RISK_TRAINING" FETCH FIRST 5000 ROWS ONLY'
    #         }
    #     }

    # read_client = itcfs.get_flight_client()


    # flightInfo = itcfs.get_flight_info(read_client, nb_data_request=data_request)

    # df = itcfs.read_pandas_and_concat(read_client, flightInfo, timeout=240)
    # create empty dataframe to have a valid return type
    
    # throw an exception to signal that this functionality is not available
    print("not implemented")
    raise Exception("not implemented")


def load_german_credit_risk_data():
    """
    checks if it can find the data in db2 or on the local filesystem.
    If necessary downloads it from the internet. 
    Returns it as a dataframe

    Returns:
        pandas df: german credit risk data
    """
    try:
        return load_data_from_db2()
    except:
        print("Error while loading data from db2. downloading csv file to filesystem instead")

    if os.path.isfile(raw_data_path):
        print("File already exists in filesystem.")
    else:
        download_data_to_filesystem(raw_data_path)
    print("loading data to pandas dataframe")
    return pd.read_csv(raw_data_path)


def save_data_in_filesystem(df,filename):
    """
    Save Data in Filesystem

    Passed filename should involve path

    """
    try:
        if filename[-3:] == "csv":
            df.to_csv(filename,index=False)
            print(f"File {filename} persisted successfully as csv")
        else:
            with open(filename, 'wb') as f:
                pickle.dump(df, f)
            print(f"File {filename} pickled successfully")
    except Exception as e:
        print(e)
        print(f"File serialization for {filename} failed")
        
        
def load_data_from_filesystem(path):
    """
    Check existence of path in filesystem.
    If it does exist, loads csv via path
    If it does NOT exist, try to load data from Db2
    """
    body = check_for_file_in_filesystem(path)
    if body:
        suffix = path[-3:]
        # Check whether path ends on csv
        if suffix == "csv":
            gcf_df = pd.read_csv(path)
        else:
            with open(path) as f:
                gcf_df = pickle.load(f)
        return gcf_df