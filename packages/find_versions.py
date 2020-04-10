import os


class Find_Versions(object):
    def __init__(self, path):
        self.path = path
        self.versions = []
        self.file_path = []

    def return_versions(self, Base_Dir):
        #Check that application is in base directory
        if Base_Dir.lower() == "true":
            self.versions.append(self.path)

        else:
            dirs = os.listdir(self.path)
            for version in dirs:
                self.versions.append(os.path.join(self.path, version))

        return self.versions
        

    def return_exe_path(self, exe_name):
        for version in self.versions:
            #First check the base directory for the application name
            if exe_name in os.listdir(version):
                self.file_path.append(os.path.join(version, exe_name))
            else:
                for root, dirs, files in os.walk(version):
                    for file in files:
                        if file.endswith(str(exe_name)):
                            self.file_path.append(os.path.join(root, file))

        return self.file_path



if __name__ == "__main__":
    print("Test module for find_versions.py")

    folder_path = r"/media/enda/750GB/4.TestData/1.Apps/SM1"

    fv = Find_Versions(folder_path)
    versions = fv.return_versions("True")
    print("\nVersions: {} \n".format(versions))

    print(fv.return_exe_path("valeo.exe"))


    print("Finished executing")