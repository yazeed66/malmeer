import os
import sys
import json
import socket
import pickle
import threading
import urllib.request
from datetime import datetime
buffer_size =1000
PORT = 55550
encoding_type="utf-8"
SERVER_IP="127.0.0.3"
SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
SERVER.Bind((SERVER_IP , PORT))
NumOfAcceptedClients=10
JsonFile="GI.json"
ClientLists = []
ShutDownServer = True
accessKey = "a2824f8004d5a49d6c5118a51214a95e"
LimitOfRetrievedRecords = 100

def Get_Flights_Data():
    try:
        while True:
            AirportCode=""
            while AirportCode ==""
            AirportCode=str(input("Enter the Airport Code"))
            WebUrl = urllib.request.urlopen
            (
                "http://api.aviationstack.com/v1/flights?access_key=" + str(access_key) + "&limit=" + str(
                    limit_of_retrieved_records) + "&arr_icao=" + str(Airportcode)
                    data = webUrl.read()
                    jsonData = json.loads(data)
                    if int(jsonData)["pagination"]["count"]>0:
                       break
                     else:
                     print("No Data Found for the Airport Code you entered:" + str(AirportCode))

                     with open(JsonFile,'w') as file:
                 json.dump(jsonData, file, indent=4)
        
            
    except:
        print("[" + str(datetime.now()) + "]" + " - " + "Error While Saving FLIGHTS DATA!")
        sys.exit(0)
def SERVER_SHUTDOWN():
    global SERVER
    print("SERVER IS SHUTINGDOWN.....")
    SERVER.close()
    os._exit(0)
def Get_All_Arrived_Flights():
    try:
        Search_Flag = False
        Response = []
        with open(JsonFile) as f:
            data = json.load(f)
            for x in data["data"]:
                if str(x["flight_status"]) == "landed":
                    Response.append(x["flight"]["iata"])
                    Response.append(x["departure"]["airport"])
                    Response.append(x["arrival"]["estimated"])
                    Response.append(str(x["arrival"]["gate"]))
                    if x["arrival"]["terminal"] == "":
                        Response.append("NULL")
                    else:
                        Response.append(str(x["arrival"]["terminal"]))
                    Search_Flag = True
        if Search_Flag == True:
            return pickle.dumps(Response)
        else:
            return pickle.dumps("There is no Arrived Flights !")
    except Exception as e:
        print("[" + str(datetime.now()) + "]" + " - " + "Error While Getting Arrived Flights!")
        return pickle.dumps("Excepetion Result : " + str(e) + "[" + str(
            datetime.now()) + "]" + " - " + "Error While Getting Arrived Flights!")
# Get All Delayed Flights
def Get_All_Delayed_Flights():
    try:
        Search_Flag = False
        Response = []
        with open(JsonFile) as f:
            data = json.load(f)
            for x in data["data"]:
            
            )
