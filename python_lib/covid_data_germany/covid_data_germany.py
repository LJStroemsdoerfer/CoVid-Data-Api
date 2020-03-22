"""
covid_data_germany.py contains the python api to access Covid-19 data for 
Germany, published by the NPGEO Corona Hub.

Slots:
--------

data        -> contains a pandas DataFrame
source      -> states the data source
date        -> stores the date, the data was crawled
url_county  -> stores the url of the county data
url_state   -> stores the url of the state data
"""

import json
import pandas as pd
import urllib.request
import datetime

# initiate class
class covid_data_germany:

    def __init__(self):

        # define the slots
        self.data = None
        self.source = "NPGEO Corona DataHub"
        self.date = None
        self.url_county = "https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/RKI_Landkreisdaten/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=false&outSR=4326&f=json"
        self.url_state = "https://services7.arcgis.com/mOBPykOjAyBO2ZKk/arcgis/rest/services/Coronaf%C3%A4lle_in_den_Bundesl%C3%A4ndern/FeatureServer/0/query?where=1%3D1&outFields=*&returnGeometry=false&outSR=4326&f=json"

    def get_data(self, level = "county"):

        # check which level to get
        if level == "county":

            # set url to county url
            url = self.url_county

        # if state level
        else:

            # set url to state url
            url = self.url_state

        # crawl the data
        with urllib.request.urlopen(url) as url:

            # request the json file
            data = json.loads(url.read().decode())
        
        # loop over dict
        for i in range(len(data["features"])):

            # if first row, then create the df
            if i == 0:

                # create the df
                df = pd.DataFrame(data["features"][i]["attributes"], index = [0])

            # if df already exists
            else:

                # append to the dataset
                df = df.append(pd.DataFrame(data["features"][i]["attributes"], index = [0]), ignore_index = False, sort = False)

        # write timestamp to object
        self.date = datetime.datetime.now()

        # write data to object
        self.data = df

    
