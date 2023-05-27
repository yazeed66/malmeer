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
                 if str(x["departure"]["delay"]) != "None":
                    Response.append(x["flight"]["iata"])
                    Response.append(x["departure"]["airport"])
                    Response.append(x["departure"]["estimated"])
                    Response.append(x["arrival"]["estimated"])
                    Response.append(x["arrival"]["gate"])
                    if x["arrival"]["terminal"] == None or x["arrival"]["terminal"] == "" or str(
                            x["arrival"]["terminal"]) == "null":
                        Response.append("None")
                    else:
                        Response.append(x["arrival"]["terminal"])
                    Search_Flag = True
        if Search_Flag == True:
            return pickle.dumps(Response)
        else:
            return pickle.dumps("There is no Delayed Flights !")
    except Exception as e:
        print("[" + str(datetime.now()) + "]" + " - " + "Error While Getting Delayed Flights!")
        return pickle.dumps("Excepetion Result : " + str(e) + "[" + str(
            datetime.now()) + "]" + " - " + "Error While Getting Delayed Flights!")
def Get_Flights_From_Specific_City(City_Name):
    try:
        Search_Flag = False
        Response = []
        with open(JsonFile) as f:
            data = json.load(f)
            for x in data["data"]:
                City = str(x["departure"]["timezone"]).split("/")
                if str(City[-1]).lower() == str(City_Name).lower():
                    Response.append(x["flight"]["iata"])
                    Response.append(x["departure"]["airport"])
                    Response.append(x["departure"]["timezone"])
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
            return pickle.dumps("There is no Flights Comes from: (" + str(City_Name) + ")!")
    except Exception as e:
        print("[" + str(datetime.now()) + "]" + " - " + "Error While Getting Flights From " + City_Name + "!")
        return pickle.dumps("Excepetion Result : " + str(e) + "[" + str(
            datetime.now()) + "]" + " - " + "Error While Getting Flights From " + City_Name + "!")
def Get_Details_of_Particular_Flight(Flight_IATA):
    try:
        Search_Flag = False
        Response = []
        with open(JsonFile) as f:
            data = json.load(f)
            for x in data["data"]:
                IATA = str(x["flight"]["iata"]).lower()
                if IATA.lower() == str(Flight_IATA).lower():
                    Response.append(x["flight"]["iata"])
                    Response.append(x["flight_date"])
                    Response.append(x["departure"]["airport"])
                    Response.append(str(x["departure"]["terminal"]))
                    Response.append(str(x["departure"]["gate"]))
                    Response.append(x["arrival"]["airport"])
                    Response.append(str(x["arrival"]["gate"]))
                    Response.append(str(x["arrival"]["terminal"]))
                    Search_Flag = True
        if Search_Flag == True:
            return pickle.dumps(Response)
        else:
            return pickle.dumps("IATA Flight: (" + str(Flight_IATA) + ") Not Found!")
    except Exception as e:
        print("Excepetion Result : " + str(e) + "[" + str(
            datetime.now()) + "]" + " - " + "Error While Getting Flight Number: " + Flight_IATA + "!")
        return pickle.dumps("Excepetion Result : " + str(e) + "[" + str(
            datetime.now()) + "]" + " - " + "Error While Getting Flight Number: " + Flight_IATA + "!")
def define_connection(connection, name):
    ClientLists.append(name)
    print("[" + str(datetime.now()) + "]" + " - ", name, " IS CONNECTED NOW ")
    print("[" + str(datetime.now()) + "]" + " - ACTIVE CLIENTS: " + str(ClientLists))
    connection.sendall(pickle.dumps(ClientLists))
    while True:
        received_option = connection.recv(buffer_size).decode(encoding_type)
        if str(received_option) == "1":
            print("[" + str(datetime.now()) + "]" + " - " + name + " SELECT OPTION : " + str(received_option))
            connection.sendall((Get_All_Arrived_Flights()))
        elif str(received_option) == "2":
            print("[" + str(datetime.now()) + "]" + " - " + name + " SELECT OPTION : " + str(received_option))
            connection.sendall(Get_All_Delayed_Flights())
        elif str(received_option) == "3":
            print("[" + str(datetime.now()) + "]" + " - " + name + " SELECT OPTION : " + str(received_option))
            Recived_City = connection.recv(buffer_size).decode(encoding_type)
            print("[" + str(datetime.now()) + "]" + " - " + name + " ASK ABOUT CITY : " + str(Recived_City))
            connection.sendall(Get_Flights_From_Specific_City(Recived_City))
        elif str(received_option) == "4":
            print("[" + str(datetime.now()) + "]" + " - " + name + " SELECT OPTION : " + str(received_option))
            Recived_IATA_Flight = connection.recv(buffer_size).decode(encoding_type)
            print(
                "[" + str(datetime.now()) + "]" + " - " + name + " ASK ABOUT IATA Flight : " + str(Recived_IATA_Flight))
            connection.sendall(Get_Details_of_Particular_Flight(Recived_IATA_Flight))
        elif str(received_option) == "5":
            print("[" + str(datetime.now()) + "]" + " - " + name + " SELECT OPTION : " + str(received_option))
            connection.sendall(pickle.dumps(ClientLists))
        elif str(received_option) == "6":
            print("[" + str(datetime.now()) + "]" + " - " + name + " SELECT OPTION : " + str(received_option))
            ClientLists.remove(name)
            connection.sendall(pickle.dumps(ClientLists))
            print("[" + str(datetime.now()) + "]" + " - " + name + " IS DISCONNECTED")
            print("[" + str(datetime.now()) + "]" + " - ACTIVE CLIENTS: " + str(ClientLists))
            connection.close()
            if (int(threading.activeCount()) - 1) == 1 and ShutDownServer == True:
                SERVER_SHUTDOWN()
            break
def start_new_connection():
    global SERVER
    SERVER.listen(NumOfAcceptedClients)
    print("[" + str(datetime.now()) + "]" + " <<<<<<< server is starting >>>>>")
    while True:
        connection, address = SERVER.accept()
        Client_Name = connection.recv(buffer_size).decode(encoding_type)
        if str(Client_Name) == "" or Client_Name == None or str(Client_Name) == "None":
            continue
        thread = threading.Thread(target=define_connection, args=(connection, Client_Name))
        thread.start()
Get_Flights_Data()
start_new_connection()