import json
with open("routers.json", "r") as json_file:
    data = json.load(json_file)
R1 = data["R1"]
R2 = data["R2"]
interface = []
R1_int = ("ssh " + R1["user"]["name"]+": "+ R1["user"]["password"]+"@"+R1["mgmt_ip"]+" -p "+str(R1["port"]))
R2_int = ("ssh " + R2["user"]["name"]+": "+ R2["user"]["password"]+"@"+R2["mgmt_ip"]+" -p "+str(R2["port"]))
interface.append(R1_int)
interface.append(R2_int)
print(interface)