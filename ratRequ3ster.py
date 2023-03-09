import requests
import base64
from datetime import datetime
import json
from lib import rpc
import yaml
import os
from PIL import Image
import customtkinter
import tkinter
import time
import ast

class Requester:

    def __init__(self, lol_location):

        self.location = lol_location

        self.port = None
        self.password = None
        self.process_id = None

        self.root_url = None
        self.host = None
        self.encoded_auth = None
        self.auth = None
        self.accept = "application/json"
        self.content_type = "application/json"

    def GetLockFileData(self):

        file = open(self.location + "\\lockfile", "r")
        fileData = file.read()
        file.close()
        fileData = fileData.split(":")
        self.RedefineAttributs(fileData)

    def GetInstantTime(self):

        now = datetime.now()
        return(now)

    def RedefineAttributs(self, dataList):

        self.port = dataList[2]
        self.password = dataList[3]
        self.process_id = dataList[1]

        self.root_url = "https://127.0.0.1:" + self.port
        self.host = "127.0.0.1:" + self.port

        combination = "riot:" + self.password
        bytes_enc = combination.encode("ascii")
        b64byte = base64.b64encode(bytes_enc)
        self.encoded_auth = b64byte.decode("ascii")
        self.auth = "Basic " + self.encoded_auth

    def PrintAllAttributs(self):

        print("------------------------------")
        print("| LEAGUE CLIENT INFORMATIONS |")
        print("------------------------------")
        print("> PORT : " + self.port)
        print("> PASSWORD : " + self.password)
        print("> PROCESS ID : " + self.process_id)

        print("---------------------------------")
        print("| REQUESTS HEADERS INFORMATIONS |")
        print("---------------------------------")
        print("> ROOT URL : " + self.root_url)
        print("> HOST : " + self.host)
        print("> ENCODED AUTHORIZATION : " + self.encoded_auth)
        print("> AUTHORIZATION : " + self.auth)
        print("")

    def MakeGetRequest(self, url):

        if self.root_url != None :

            responseString = ""
            responseString+="\n"
            responseString+="------------------------------------------------\n"           
            responseString+="> Attributs definition ⏳\n"
            responseString+="------------------------------------------------\n"
            responseString+="| REQUEST INFORMATIONS |\n"
            responseString+="------------------------------------------------\n"
            responseString+="GET " + self.root_url + url + "\n"
            responseString+="Host: " + self.host + "\n"
            responseString+="Authorization: " + self.auth + "\n"
            responseString+="Accept: " + self.accept + "\n"
            responseString+="------------------------------------------------\n"
            responseString+="\n"
            responseString+="------------------------------------------------\n"
            responseString+="> Attributs defined ✅\n"
            responseString+="> Fetching data ⏳\n"
            responseString+="------------------------------------------------\n"
            
            headers = {
                "Host": self.host,
                "Authorization": self.auth,
                "Accept": self.accept,
            }

            prepared_url = self.root_url + url

            responseString+="\n"
            responseString+="------------------------------------------------\n"
            responseString+="> Fetched successfully ✅\n"
            responseString+="> Preparing request ⏳\n"
            responseString+="------------------------------------------------\n"

            try:
                requests.packages.urllib3.disable_warnings()

            except Exception as e:
                responseString+="\n"
                responseString+="------------------------------------------------\n"
                responseString+="> Request sent ✅\n"
                responseString+="------------------------------------------------\n"
                responseString+="\n"
                responseString+="-------------------------------------------------\n"
                responseString+="| RESPONSE INFORMATIONS |\n"
                responseString+="-------------------------------------------------\n"
                responseString+="\n"
                responseString+=str(e)

            resp = requests.get(prepared_url, headers=headers, verify=False)
            responseString+="\n"
            responseString+="------------------------------------------------\n"
            responseString+="> Request sent ✅\n"
            responseString+="------------------------------------------------\n"
            responseString+="\n"
            responseString+="-------------------------------------------------\n"
            responseString+="| RESPONSE INFORMATIONS |\n"
            responseString+="-------------------------------------------------\n"
            responseString+="\n"
            responseString+=json.dumps(resp.json(), indent=4)

            return responseString


    def MakePostRequest(self, url, data):

        if self.root_url != None :

            responseString = ""
            responseString+="\n"
            responseString+="------------------------------------------------\n"           
            responseString+="> Attributs definition ⏳\n"
            responseString+="------------------------------------------------\n"
            responseString+="| REQUEST INFORMATIONS |\n"
            responseString+="------------------------------------------------\n"
            responseString+="POST " + self.root_url + url + "\n"
            responseString+="Host: " + self.host + "\n"
            responseString+="Authorization: " + self.auth + "\n"
            responseString+="Accept: " + self.accept + "\n"
            responseString+="------------------------------------------------\n"
            responseString+="\n"
            responseString+="------------------------------------------------\n"
            responseString+="> Attributs defined ✅\n"
            responseString+="> Fetching data ⏳\n"
            responseString+="------------------------------------------------\n"
            
            headers = {
                "Host": self.host,
                "Authorization": self.auth,
                "Accept": self.accept,
            }

            prepared_url = self.root_url + url

            responseString+="\n"
            responseString+="------------------------------------------------\n"
            responseString+="> Fetched successfully ✅\n"
            responseString+="> Preparing request ⏳\n"
            responseString+="------------------------------------------------\n"

            try:
                requests.packages.urllib3.disable_warnings()
                resp = requests.post(prepared_url, headers=headers, data=data, verify=False)
                responseString+="\n"
                responseString+="------------------------------------------------\n"
                responseString+="> Request sent ✅\n"
                responseString+="------------------------------------------------\n"
                responseString+="\n"
                responseString+="-------------------------------------------------\n"
                responseString+="| RESPONSE INFORMATIONS |\n"
                responseString+="-------------------------------------------------\n"
                responseString+="\n"
                responseString+=json.dumps(resp.json(), indent=4)
                return responseString

            except Exception as e:
                responseString+="\n"
                responseString+="------------------------------------------------\n"
                responseString+="> Request sent ✅\n"
                responseString+="------------------------------------------------\n"
                responseString+="\n"
                responseString+="-------------------------------------------------\n"
                responseString+="| RESPONSE INFORMATIONS |\n"
                responseString+="-------------------------------------------------\n"
                responseString+="\n"
                responseString+=str(e)
                return responseString




    def MakePutRequest(self, url, data):

        if self.root_url != None :

            responseString = ""
            responseString+="\n"
            responseString+="------------------------------------------------\n"           
            responseString+="> Attributs definition ⏳\n"
            responseString+="------------------------------------------------\n"
            responseString+="| REQUEST INFORMATIONS |\n"
            responseString+="------------------------------------------------\n"
            responseString+="PUT " + self.root_url + url + "\n"
            responseString+="Host: " + self.host + "\n"
            responseString+="Authorization: " + self.auth + "\n"
            responseString+="Accept: " + self.accept + "\n"
            responseString+="------------------------------------------------\n"
            responseString+="\n"
            responseString+="------------------------------------------------\n"
            responseString+="> Attributs defined ✅\n"
            responseString+="> Fetching data ⏳\n"
            responseString+="------------------------------------------------\n"
            
            headers = {
                "Host": self.host,
                "Authorization": self.auth,
                "Accept": self.accept,
            }

            prepared_url = self.root_url + url

            responseString+="\n"
            responseString+="------------------------------------------------\n"
            responseString+="> Fetched successfully ✅\n"
            responseString+="> Preparing request ⏳\n"
            responseString+="------------------------------------------------\n"

            try:
                requests.packages.urllib3.disable_warnings()
                resp = requests.put(prepared_url, headers=headers, data=data, verify=False)
                responseString+="\n"
                responseString+="------------------------------------------------\n"
                responseString+="> Request sent ✅\n"
                responseString+="------------------------------------------------\n"
                responseString+="\n"
                responseString+="-------------------------------------------------\n"
                responseString+="| RESPONSE INFORMATIONS |\n"
                responseString+="-------------------------------------------------\n"
                responseString+="\n"
                responseString+=json.dumps(resp.json(), indent=4)

            except Exception as e:

                responseString+="\n"
                responseString+="------------------------------------------------\n"
                responseString+="> Request sent ✅\n"
                responseString+="------------------------------------------------\n"
                responseString+="\n"
                responseString+="-------------------------------------------------\n"
                responseString+="| RESPONSE INFORMATIONS |\n"
                responseString+="-------------------------------------------------\n"
                responseString+="\n"
                responseString+=str(e)

            return responseString

    def MakeDeleteRequest(self, url):

        if self.root_url != None :

            responseString = ""
            responseString+="\n"
            responseString+="------------------------------------------------\n"           
            responseString+="> Attributs definition ⏳\n"
            responseString+="------------------------------------------------\n"
            responseString+="| REQUEST INFORMATIONS |\n"
            responseString+="------------------------------------------------\n"
            responseString+="DELETE " + self.root_url + url + "\n"
            responseString+="Host: " + self.host + "\n"
            responseString+="Authorization: " + self.auth + "\n"
            responseString+="Accept: " + self.accept + "\n"
            responseString+="------------------------------------------------\n"
            responseString+="\n"
            responseString+="------------------------------------------------\n"
            responseString+="> Attributs defined ✅\n"
            responseString+="> Fetching data ⏳\n"
            responseString+="------------------------------------------------\n"
            
            headers = {
                "Host": self.host,
                "Authorization": self.auth,
                "Accept": self.accept,
            }

            prepared_url = self.root_url + url

            responseString+="\n"
            responseString+="------------------------------------------------\n"
            responseString+="> Fetched successfully ✅\n"
            responseString+="> Preparing request ⏳\n"
            responseString+="------------------------------------------------\n"

            try:
                requests.packages.urllib3.disable_warnings()
                resp = requests.delete(prepared_url, headers=headers, verify=False)
                responseString+="\n"
                responseString+="------------------------------------------------\n"
                responseString+="> Request sent ✅\n"
                responseString+="------------------------------------------------\n"
                responseString+="\n"
                responseString+="---------------------------------------------------------------------------------------------------\n"
                responseString+="| RESPONSE INFORMATIONS [for Delete request : 204 = Request effective ✅ ]|\n"
                responseString+="---------------------------------------------------------------------------------------------------\n"
                responseString+="\n"
                responseString+="> Status code : " + str(resp.status_code)

            except Exception as e:
                responseString+="\n"
                responseString+="------------------------------------------------\n"
                responseString+="> Request sent ✅\n"
                responseString+="------------------------------------------------\n"
                responseString+="\n"
                responseString+="---------------------------------------------------------------------------------------------------\n"
                responseString+="| RESPONSE INFORMATIONS [for Delete request : 204 = Request effective ✅ ]|\n"
                responseString+="---------------------------------------------------------------------------------------------------\n"
                responseString+="\n"
                responseString+=str(e)



            return responseString

        


customtkinter.set_appearance_mode("System")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


class App(customtkinter.CTk):

    def __init__(self):

        super().__init__()

        self.client_id = "1083401496764362803"
        self.LEAGUE_PATH = None
        self.REQU3STER = None
        self.logs_index = 0

        self.title("ratRequ3ster")

        self.geometry(f"{1220}x{700}")
        self.minsize(1220, 720)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((0, 2), weight=0)
        self.grid_rowconfigure(0, weight=0)
        self.grid_rowconfigure((1, 2, 3), weight=1)
        self.iconbitmap("src/img/yellowDotLogo.ico")

        self.sidebar_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0)
        self.sidebar_frame.grid(row=0, column=0, rowspan=4, sticky="nsew")
        self.sidebar_frame.grid_rowconfigure(1, weight=1)

        self.logo_image = customtkinter.CTkImage(Image.open("src/img/yellowDotLogo.png"), size=(140, 130))
        self.logo_label = customtkinter.CTkLabel(self.sidebar_frame, text="", font=customtkinter.CTkFont(size=21, weight="bold"), image=self.logo_image, compound="left")
        self.logo_label.grid(row=0, column=0, padx=0, pady=(20, 10))

        # Left Frame
        self.tabview = customtkinter.CTkTabview(self.sidebar_frame, width=230)
        self.tabview.grid(row=1, column=0, padx=20, pady=(20, 20), sticky="nsew")
        self.tabview.add("Home")
        self.tabview.add("Settings")
        self.tabview.tab("Home").grid_columnconfigure(0, weight=1)
        self.tabview.tab("Home").grid_rowconfigure((0, 1, 2), weight=0)
        self.tabview.tab("Home").grid_rowconfigure(4, weight=1)
        self.tabview.tab("Home").grid_rowconfigure((5, 6), weight=0)
        self.tabview.tab("Settings").grid_columnconfigure(0, weight=1)  

        self.welcome_label = customtkinter.CTkLabel(self.tabview.tab("Home"), text="Welcome in\nratRequ3ster!", font=customtkinter.CTkFont(size=21, weight="bold"), text_color="#1F6AA5", anchor="w")
        self.welcome_label.grid(row=0, column=0, padx=20, pady=(10, 10))

        self.devby_label = customtkinter.CTkLabel(self.tabview.tab("Home"), text="dev by akira", font=customtkinter.CTkFont(size=18, weight="normal"), anchor="w")
        self.devby_label.grid(row=1, column=0, padx=20, pady=(10, 10))

        self.lcuDoc_label = customtkinter.CTkButton(self.tabview.tab("Home"), text="Open LCU Doc" , font=customtkinter.CTkFont(size=15, weight="normal"), anchor="w", compound="left", command=self.openLcuDoc, width=50, height=40)
        self.lcuDoc_label.grid(row=2, column=0, padx=20, pady=(10, 10))


        self.logs_label = customtkinter.CTkLabel(self.tabview.tab("Home"), text="Logs :", font=customtkinter.CTkFont(size=14, weight="normal"))
        self.logs_label.grid(row=4, column=0, padx=20, pady=0, sticky="s")

        self.scrollbarx = tkinter.Scrollbar(self.tabview.tab("Home"), orient=tkinter.HORIZONTAL)

        self.logs = tkinter.Listbox(self.tabview.tab("Home"), font=customtkinter.CTkFont(size=12, weight="normal"), background='#bfbfbf', fg="black", width=30, height=10, xscrollcommand=self.scrollbarx.set)
        self.logs.grid(row=5, column=0, padx=2, pady=0, sticky="s")

        self.scrollbarx.config(command=self.logs.xview)
        self.scrollbarx.grid(row=6, column=0, padx=0, pady=0, sticky="s")

        self.appearance_mode_label = customtkinter.CTkLabel(self.tabview.tab("Settings"), text="Theme :", anchor="w")
        self.appearance_mode_label.grid(row=0, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.tabview.tab("Settings"), values=["Light", "Dark", "System"],command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=1, column=0, padx=20, pady=(10, 10))

        self.discordRPC_label = customtkinter.CTkLabel(self.tabview.tab("Settings"), text="Discord RPC :", anchor="w")
        self.discordRPC_label.grid(row=2, column=0, padx=20, pady=(10, 0))
        self.discordRPC_optionemenu = customtkinter.CTkOptionMenu(self.tabview.tab("Settings"), values=["On", "Off"], command=self.ToggleDiscordRpc)
        self.discordRPC_optionemenu.grid(row=3, column=0, padx=20, pady=(10, 10))

        self.selectPathImage = customtkinter.CTkImage(Image.open("src/img/path.png"), size=(30, 30))
        self.selectPath = customtkinter.CTkButton(master=self.tabview.tab("Settings"), text="Select League Path", image=self.selectPathImage, compound="left", command=self.askPath, width=50, height=40)
        self.selectPath.grid(row=4, column=0, columnspan=20, sticky="nsew", padx=20, pady=(10, 0))


        # MIDDLE COLUMN

        self.middle_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0, fg_color="#242424")
        self.middle_frame.grid(row=0, column=1, rowspan=4, sticky="nsew")
        self.middle_frame.grid_rowconfigure((0, 1, 2, 3), weight=0)
        self.middle_frame.grid_rowconfigure(4, weight=1)

        self.middle_frame.grid_columnconfigure((0, 1, 2, 3), weight=1)

        self.logoImage = customtkinter.CTkImage(Image.open("src/img/boxLogo.png"), size=(80, 70))
        self.titleLabel = customtkinter.CTkLabel(master=self.middle_frame, text="  Requ3st Constructor", font=customtkinter.CTkFont(size=25, weight="bold"), image=self.logoImage, compound="left")
        self.titleLabel.grid(row=0, column=0, columnspan=4, padx=15, pady=(25, 0), sticky="w")

        self.urlEntry = customtkinter.CTkEntry(self.middle_frame, placeholder_text="Endpoint URL", width=180)
        self.urlEntry.grid(row=1, column=0, columnspan=4, padx=(10, 10), pady=(15, 15), sticky="we")

        self.reqType_optionemenu = customtkinter.CTkOptionMenu(self.middle_frame, values=["GET", "POST", "PUT", "DELETE"])
        self.reqType_optionemenu.grid(row=2, column=3,padx=(10, 0), pady=(15, 15), sticky="e")

        self.sendButton = customtkinter.CTkButton(self.middle_frame, text="Send", width=100, command=self.sendRequ3stTask)
        self.sendButton.grid(row=2, column=4, padx=(5, 10), pady=(15, 15), sticky="e")

        self.response = customtkinter.CTkLabel(master=self.middle_frame, text="Requ3st response :", font=customtkinter.CTkFont(size=18, weight="normal"))
        self.response.grid(row=3, column=0, padx=(15, 0), pady=(15,10), sticky="w")

        self.responseTextbox = customtkinter.CTkTextbox(master=self.middle_frame)
        self.responseTextbox.grid(row=4, column=0, columnspan=5, padx=(15, 15), pady=(5, 15), sticky="nwes") 

        # RIGHT COLUMN

        self.right_frame = customtkinter.CTkFrame(self, width=140, corner_radius=0, fg_color="#2b2b2b")
        self.right_frame.grid(row=0, column=2, rowspan=4, sticky="nsew")
        self.right_frame.grid_rowconfigure((3), weight=1)
        self.right_frame.grid_rowconfigure((0, 1, 2, ), weight=0)

        self.dataLabel = customtkinter.CTkLabel(master=self.right_frame, text="JSON data [For POST/PUT Requ3sts] :", font=customtkinter.CTkFont(size=21, weight="normal"))
        self.dataLabel.grid(row=0, column=0, padx=20, pady=(35, 5))

        self.dataTextbox = customtkinter.CTkTextbox(master=self.right_frame, width=350, height=300)
        self.dataTextbox.grid(row=1, rowspan=3, column=0, padx=3, pady=(5, 15), sticky="ns") 


        self.FullStart()

    def FullStart(self):

        self.AddLog("ratRequ3ster UI started.")
        self.appearance_mode_optionemenu.set("Dark")
        self.CheckRpcSet()
        self.loadLeaguePath()
        self.CreateRequ3ster()

    def AddLog(self, str):

        self.logs.insert(self.logs_index, self.getClearLog(str))
        self.logs_index += 1

    def getClearLog(self, str):

        now = datetime.now()  
        current_time = now.strftime("%H:%M:%S")
        newlog = "[" + current_time + "] " + str 
        return newlog

    def CreateRequ3ster(self):

        if self.LEAGUE_PATH != None:

            try: 
                requ = Requester(self.LEAGUE_PATH)
                self.REQU3STER = requ
                self.REQU3STER.GetLockFileData()
                self.REQU3STER.MakeGetRequest("/lol-chat/v1/me")
                self.AddLog("Requ3ster Object created.")

            except Exception as e:
                self.AddLog("Error when creating Requ3ster. Please make sure that League is started.")
                self.REQU3STER = None

        else:
            self.AddLog("Error when creating Requ3ster.Please verify League path.")

    def sendRequ3stTask(self):
        
        if self.REQU3STER != None:

            if self.urlEntry.get() != None :

                method = self.reqType_optionemenu.get()
                
                if method == "GET":
                    
                    try:
                        r = self.REQU3STER.MakeGetRequest(self.urlEntry.get())
                        self.responseTextbox.delete("1.0", tkinter.END)
                        self.responseTextbox.insert("1.0", r)

                    except requests.exceptions.ConnectionError as e:
                        self.AddLog("Please make sure that League is started.")
                
                elif method == "POST":

                    try:
                        dataDict = ast.literal_eval(self.dataTextbox.get("1.0", tkinter.END))
                        self.responseTextbox.delete("1.0", tkinter.END)
                        r = self.REQU3STER.MakePostRequest(self.urlEntry.get(), data=json.dumps(dataDict))
                        self.responseTextbox.insert("1.0", r)
                    except SyntaxError as e:
                        self.AddLog("Please add JSON Data to perform requ3st.")


                elif method == "PUT":

                    try:
                        dataDict = ast.literal_eval(self.dataTextbox.get("1.0", tkinter.END))
                        self.responseTextbox.delete("1.0", tkinter.END)
                        r = self.REQU3STER.MakePutRequest(self.urlEntry.get(), json.dumps(dataDict))
                        self.responseTextbox.insert("1.0", r)
                    except SyntaxError as e:
                        self.AddLog("Please add JSON Data to perform requ3st.")

                elif method == "DELETE":

                    self.responseTextbox.delete("1.0", tkinter.END)
                    r = self.REQU3STER.MakeDeleteRequest(self.urlEntry.get())
                    self.responseTextbox.insert("1.0", r)

        else:

            self.CreateRequ3ster()
            self.AddLog("Requ3ster was not created. Please try again.")

    def askPath(self):

        folder_selected = customtkinter.filedialog.askdirectory()
        self.LEAGUE_PATH = folder_selected
        with open("config/conf.yaml", "r") as conf:
            confData = yaml.safe_load(conf)
            confData["leaguePath"] = self.LEAGUE_PATH

        with open("config/conf.yaml", "w") as conf:
            yaml.dump(confData, conf)

        self.AddLog("League Path modified.")
    
    def openLcuDoc(self):

        os.system("start \"\" https://www.mingweisamuel.com/lcu-schema/tool/#/")
        self.AddLog("LCU Doc opened on browser.")

    def loadLeaguePath(self):

        with open("config/conf.yaml", "r") as conf:
            confData = yaml.safe_load(conf)
            if confData["leaguePath"] != "None":
                self.LEAGUE_PATH = confData["leaguePath"]
        self.AddLog("League path loaded.")

    def change_appearance_mode_event(self, new_appearance_mode):
        customtkinter.set_appearance_mode(new_appearance_mode)
        self.AddLog("Appearance modified.")


    def CheckRpcSet(self):

        with open("config/conf.yaml", "r") as conf:
            confData = yaml.safe_load(conf)
            if confData["discordRPC"] == 1:
                self.StartRPC()
                self.discordRPC_optionemenu.set("On")
            else:
                self.discordRPC_optionemenu.set("Off")
                try:
                    self.rpc_obj.close()
                except:
                    pass

    def StartRPC(self):            

        self.rpc_obj = rpc.DiscordIpcClient.for_platform(self.client_id)
        start_time = time.mktime(time.localtime())
        activity = {
                    "timestamps": {
                "start": start_time
                },
                "details": "LCU API Requ3ster",  
                "assets": {
                    "small_text": "Requ3sting...",  
                    "small_image": "boxlogo",  
                    "large_text": "ratRequ3ster",
                    "large_image": "yellowdotlogo" 
                },
                "buttons" : [{"label" : "github", "url" : "https://github.com/akira-trinity/"}]
            }
        self.rpc_obj.set_activity(activity)
        self.AddLog("Discord RPC started.")

    def ToggleDiscordRpc(self, ChoosenMode):

        if ChoosenMode == "On":
            with open("config/conf.yaml", "r") as conf:
                confData = yaml.safe_load(conf)
                confData["discordRPC"] = 1
                self.AddLog("Discord RPC turned ON.")

            with open("config/conf.yaml", "w") as conf:
                yaml.dump(confData, conf)
        else:
            with open("config/conf.yaml", "r") as conf:
                confData = yaml.safe_load(conf)
                confData["discordRPC"] = 0
                self.AddLog("Discord RPC turned OFF.")

            with open("config/conf.yaml", "w") as conf:
                yaml.dump(confData, conf)

        self.CheckRpcSet()

if __name__ == "__main__":

    app = App()
    app.mainloop()

# BLUE COLOR : #1F6AA5