import json


class Config_Parser(object):
    def __init__(self):
        self.app_data = {}

    def parse_file(self, filePath):
        with open(filePath, "r") as f:
            data = json.load(f)
            apps = data["applications"]
            file_data = [dict() for item in range(len(apps))]
            i = 0

            for key, value in apps.items():
                self.app_data.update({i: (key, value["Path"], value["exe"], value["URL_Path"])})
                i += 1
            return self.app_data

                
            
                

                




if __name__ == "__main__":
    print("Config Parser Test Module Running")

    filePath = r"packages/applications.json"

    cp = Config_Parser()
    app_data = cp.parse_file(filePath)
    print("Length: {} ".format(len(app_data)))
    print(app_data[1][0])




    print("Finished executing")