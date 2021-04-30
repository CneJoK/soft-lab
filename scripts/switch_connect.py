import yaml
with open("switches.yaml", "r") as yaml_file:
    data = yaml.load(yaml_file)
R1 = data["SW1"]
R2 = data["SW2"]
interface = []
R1_int = ("ssh " + R1["user"]["name"]+": "+ R1["user"]["password"]+"@"+R1["mgmt_ip"]+" -p "+str(R1["port"]))
R2_int = ("ssh " + R2["user"]["name"]+": "+ R2["user"]["password"]+"@"+R2["mgmt_ip"]+" -p "+str(R2["port"]))
interface.append(R1_int)
interface.append(R2_int)
print(interface)