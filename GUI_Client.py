import pickle
import socket
import tkinter as tk
import tkinter.font as tkFont
from tkinter import messagebox, simpledialog, END, Entry

buffer_size = 10000
PORT = 60000
SERVER_IP = "127.0.0.1"
encoding_type = "utf-8"
Client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
Client.connect((SERVER_IP, PORT))
class Flighs_App:
    global buffer_size
    global PORT
    global SERVER_IP
    global encoding_type
    global Client
    def Sending_Function(self,Message):
        message_send = Message.encode(encoding_type)
        Client.sendall(message_send)
    def Reciving_Function(self):
        message_received = pickle.loads(Client.recv(buffer_size))
        return message_received
    def Get_User_Name(self):
        try:
            Name = ""
            while str(Name) == "" or Name == None or str(Name) == "None":
                Name = simpledialog.askstring('USER Name', 'Enter The USER Name')
            self.Sending_Function(str(Name))
            self.Show_Message_Box(f"\n  ## LIST OF CLIENTS CONNECTED TO THE SERVER ## \n {str(self.Reciving_Function())}")
            return Name
        except:
            print("Error Getting The User Name!")
    def Get_City_Name(self):
        try:
            City = ""
            while str(City) == "" or City == None or str(City) == "None":
                City = simpledialog.askstring('City Name', 'Enter The City Name')
            return City
        except:
            print("Error Geting City Flgihts ")
    def Get_Flight_Number(self):
        try:
            Flight_Number = ""
            while str(Flight_Number) == "" or Flight_Number == None or str(Flight_Number) == "None":
                Flight_Number = simpledialog.askstring('Flight Number', 'Enter Flight Number')
            return Flight_Number
        except:
            print("Error While Geting Flgiht Number!!")
    def Show_Message_Box(self,Message):
        messagebox.showinfo("Response: ",Message)
    def Create_Table(self,List,Title):
        self.e = None
        root = tk.Tk()
        root.title(Title)
        total_rows = len(List)
        total_columns = len(List[0])
        for i in range(total_rows):
            for j in range(total_columns):
                self.e = Entry(root, width=25, fg='black',font=('Arial', 11, 'bold'))
                if List[i][j] is not None:
                    self.e.insert(END, List[i][j])
                else:
                    self.e.insert(END, "None")
                self.e.grid(row=i, column=j)
    def Get_Arrived_Flights(self):
        self.Sending_Function("1")
        Receviced_Data = self.Reciving_Function()
        i = 0
        j = 0
        List = []
        List.insert(j, ["Flight No", "airport", "ArrivalEstemated","Arrivalgate","terminal"])
        j=j+1
        while j <= (len(Receviced_Data) / 5):
            List.insert(j, [Receviced_Data[i], Receviced_Data[i + 1], Receviced_Data[i + 2],Receviced_Data[i + 3],Receviced_Data[i + 4]])
            j = j + 1
            i = i + 5
        self.Create_Table(List,"Arrived Flights")
    def Get_Delayed_Flights(self):
        self.Sending_Function("2")
        Receviced_Data = self.Reciving_Function()
        i = 0
        j = 0
        List = []
        List.insert(j, ["Flight No", "airport", "ArrivalEstemated", "Arrivalgate", "terminal"])
        j = j + 1
        while j <= (len(Receviced_Data) / 6):
            List.insert(j, [Receviced_Data[i], Receviced_Data[i + 1], Receviced_Data[i + 2], Receviced_Data[i + 3],
                            Receviced_Data[i + 4],Receviced_Data[i + 5]])
            j = j + 1
            i = i + 6

        print(list)
        self.Create_Table(List, "Delayed Flights")
    def Get_Flights_By_City_Name(self):
        City = self.Get_City_Name()
        self.Sending_Function("3")
        self.Sending_Function(City)
        Receviced_Data = self.Reciving_Function()
        i = 0
        j = 0
        List = []
        List.insert(j, ["Flight No","DepartureAirport","timezone","ArrivalEstimated","Arrivalgate","Terminal"])
        j = j+1
        while j <= (len(Receviced_Data)/6):
            List.insert(j, [Receviced_Data[i], Receviced_Data[i + 1], Receviced_Data[i + 2], Receviced_Data[i + 3], Receviced_Data[i + 4], Receviced_Data[i + 5]])
            j = j+1
            i = i+6
        self.Create_Table(List, "Flights Coming From : " + str(City))

    def Get_Flight_By_Flight_Number(self):
        Flight = self.Get_Flight_Number()
        self.Sending_Function("4")
        self.Sending_Function(Flight)
        Receviced_Data = self.Reciving_Function()
        i = 0
        j = 0
        List = []
        List.insert(j, ["Flight No","date","DepartureAirport","DepartureTerminal","departureGate","ArrivalAirport","ArrivalTerminal","ArrivalGate"])
        j = j +1
        while j <= (len(Receviced_Data)/8):
            List.insert(j,[Receviced_Data[i], Receviced_Data[i + 1], Receviced_Data[i + 2], Receviced_Data[i + 3], Receviced_Data[i + 4], Receviced_Data[i + 5], Receviced_Data[i + 6], Receviced_Data[i + 7]])
            j = j+1
            i = i + 8
        self.Create_Table(List, "Flight : " + str(Flight))
    def Get_Active_Client(self):
        self.Sending_Function("5")
        self.Show_Message_Box(    f"\n  ## CLIENTS CONNECTED TO THE SERVER ## \n {str(self.Reciving_Function())}")
    def Client_Window_Destroy(self):
        self.Sending_Function("6")
        self.Show_Message_Box(  f"\n  ## CONNECTED TO THE SERVER ## \n {self.Reciving_Function()}")
        self.Show_Message_Box(" Yazeed 3mk say BAY BAY ")
        root.destroy()
    def __init__(self, root):
        self.e = None
        root.protocol("WM_DELETE_WINDOW", self.Client_Window_Destroy)
        root.title(" API Flights System")
        width=415
        height=410
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        Font = tkFont.Font(family="Times New Roman",size=14)



        Exit_Button = tk.Button(root)
        Exit_Button["bg"] = "Azure"
        Exit_Button["font"] = Font
        Exit_Button["fg"] = "Red"
        Exit_Button["justify"] = "center"
        Exit_Button["text"] = "EXIT"
        Exit_Button.place(x=180, y=350, width=50, height=50)
        Exit_Button["command"] = self.Client_Window_Destroy



        Active_Clients_Button = tk.Button(root)
        Active_Clients_Button["bg"] = "Maroon"
        Active_Clients_Button["font"] = Font
        Active_Clients_Button["fg"] = "white"
        Active_Clients_Button["justify"] = "center"
        Active_Clients_Button["text"] = "ALL ACTIVE CLIENTS"
        Active_Clients_Button.place(x=120, y=280, width=200, height=50)
        Active_Clients_Button["command"] = self.Get_Active_Client



        Arrived_Flights_Button=tk.Button(root)
        Arrived_Flights_Button["bg"] = "black"
        Arrived_Flights_Button["font"] = Font
        Arrived_Flights_Button["fg"] = "white"
        Arrived_Flights_Button["justify"] = "center"
        Arrived_Flights_Button["text"] = "Get All Arrived Flights"
        Arrived_Flights_Button.place(x=10,y=10,width=380,height=50)
        Arrived_Flights_Button["command"] = self.Get_Arrived_Flights



        City_Flights_Button = tk.Button(root)
        City_Flights_Button["bg"] = "Blue"
        City_Flights_Button["font"] = Font
        City_Flights_Button["fg"] = "white"
        City_Flights_Button["justify"] = "center"
        City_Flights_Button["text"] = "Get Flights From Specific City"
        City_Flights_Button.place(x=10, y=130, width=380, height=50)
        City_Flights_Button["command"] = self.Get_Flights_By_City_Name



        Delayed_Flights_Button=tk.Button(root)
        Delayed_Flights_Button["bg"] = "Grey"
        Delayed_Flights_Button["font"] = Font
        Delayed_Flights_Button["fg"] = "white"
        Delayed_Flights_Button["justify"] = "center"
        Delayed_Flights_Button["text"] = "Get All Delayed Flights"
        Delayed_Flights_Button.place(x=10,y=65,width=380,height=50)
        Delayed_Flights_Button["command"] = self.Get_Delayed_Flights



        Spicific_Flight_Button = tk.Button(root)
        Spicific_Flight_Button["bg"] = "Green"
        Spicific_Flight_Button["font"] = Font
        Spicific_Flight_Button["fg"] = "white"
        Spicific_Flight_Button["justify"] = "center"
        Spicific_Flight_Button["text"] = "Particular Flight Details"
        Spicific_Flight_Button.place(x=10, y=205, width=380, height=50)
        Spicific_Flight_Button["command"] = self.Get_Flight_By_Flight_Number




        
        Client_Name = self.Get_User_Name()
        root.title(str(Client_Name) + " - API Flights System")
if __name__ == "__main__":
    root = tk.Tk()
    Flighs_App = Flighs_App(root)
    root.mainloop()

