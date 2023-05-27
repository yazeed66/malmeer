import socket
import pickle


buffer_size = 10000
PORT = 60000
SERVER_IP = "127.0.0.1"
encoding_type = "utf-8"
Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Client.connect((SERVER_IP, PORT))

def ask_for_client_name():
    print(" write the USER Name or write (Quit) To Exit: ")
    Client_name = ""
    while Client_name == "":
        Client_name = str(input("Enter USER Name: "))
    if Client_name.lower() == "Quit":
        print("USER : Bye Bye ")
        exit(0)
    Sending_Function(Client_name)
    print(f"\n  ## LIST OF USERS CURRENTLY CONNECTED TO THE SERVER ## \n {str(Reciving_Function())}")

def Reciving_Function():
    message_received = pickle.loads(Client.recv(buffer_size))
    return message_received

def Sending_Function(Mes):
    message_send = Mes.encode(encoding_type)
    Client.sendall(message_send)






def serve_client():
    global Receviced_Data
    while True:
        print("Select An Option:")
        print("1- All The Arrived Flights.")
        print("2- All The Delayed Flights:")
        print("3- All Flights Coming From a Specific City:")
        print("4- Details Of a Particular Flight:")
        print("5- Get A List of The Connected USERS:")
        print("6- Quit")
        Selected_Option = int(input())
        if Selected_Option == 1:
            Sending_Function("1")
            Receviced_Data = Reciving_Function()
            Response = ""
            Response += (
                "{:<6} | {:<17} | {:<25} | {:<8} | {:<8} \n".format('IATA'.center(6), 'Departure Airport'.center(25),
                                                                    'ArivalEstimated'.center(25),
                                                                    'Gate'.center(8), 'Terminal'.center(7)))
            Response += (
                "{:<6} | {:<17} | {:<25} | {:<8} | {:<8} \n".format('------'.center(6), '-----------------'.center(25),
                                                                    '-----------------'.center(25),

                                                                    '--------'.center(8), '--------'.center(7)))

            i = 0
            j = 0
            j = j + 1
            while j <= (len(Receviced_Data) / 5):
                Response += ("{:<6} | {:<17} | {:<25} | {:<8} | {:<8} \n".format(str(Receviced_Data[i]).center(6),
                                                                                 str(Receviced_Data[i + 1]).center(25),
                                                                                 str(Receviced_Data[i + 2]).center(25),
                                                                                 str(Receviced_Data[i + 3]).center(7),
                                                                                 str(Receviced_Data[i + 4]).center(7),
                                                                                 ))

                j = j + 1
                i = i + 5
            print(Response)
