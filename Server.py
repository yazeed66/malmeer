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
                    if
            
            )
