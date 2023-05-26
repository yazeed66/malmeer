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
