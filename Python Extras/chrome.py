import os, sys, stat

os.chmod(r"C:\Users\moham\AppData\Local\Google\Chrome\User Data\Default\Current Tabs",stat.S_IRWXO)


Current_Tabs_Source = open(r"C:\Users\moham\AppData\Local\Google\Chrome\User Data\Default\Current Tabs", "r")
Current_Tabs_Raw = Current_Tabs_Source.read()
print(Current_Tabs_Raw) #just for checking
