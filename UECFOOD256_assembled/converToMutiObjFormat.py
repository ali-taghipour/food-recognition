import os
import shutil

def delete_duplicate_image_label():
    imagesLength = 0
    
    for dirpath, dirnames, filenames in os.walk("."):
        if "images" in dirpath:
            imagesLength += +len(filenames)

    for i in range(1,imagesLength+1):
        print(f"process on image/lable {i}")
        simList = []
        for dirpath, dirnames, filenames in os.walk("."):
            for filename in filenames:
                if filename.endswith(f"-{i}.txt"):
                    simList.append({"labelPath":dirpath[2:], "filename":filename[0:-4], "labelFolder":dirpath[2:].replace("\\",",").split(",")[0]})
        if(len(simList) > 1):
            file = open(f"{simList[0]["labelPath"]}/{simList[0]["filename"]}.txt","a")
            classFile = open(f"deletedClasses/{i}.txt","a")
            for item in simList[1:]:
                classFile.write(f"{item["filename"].split("-")[0]} {item["labelFolder"]} {simList[0]["labelFolder"]} \n")
                file2 = open(f"{item["labelPath"]}/{item["filename"]}.txt","r")  
                file.write(f"\n{file2.read()}")
                file2.close()
                os.remove(f"{item["labelPath"]}/{item["filename"]}.txt")
                os.remove(f"{item["labelFolder"]}/images/{item["filename"]}.jpg")
            file.close()  
            classFile.close()

def transfer_image_label():
    #print(len(os.listdir('deletedClasses')))

    for filename in os.listdir("deletedClasses"):
        file = open(f"deletedClasses/{filename}","r")
        #print(len(file.readlines()))
        for line in file.readlines():
            line = line.split(" ")
            for label in os.listdir(f"{line[2]}/labels"):
                if(label.split("-")[0] == line[0]):
                    file2 = open(f"{line[2]}/labels/{label}")
                    if(len(file2.readlines()) == 1):
                        file2.close()
                        shutil.move(f"{line[2]}/labels/{label}", f"{line[1]}/labels/{label}")
                        shutil.move(f"{line[2]}/images/{label[:-4]}.jpg", f"{line[1]}/images/{label[:-4]}.jpg")
                        break
        file.close()
        os.remove(f"deletedClasses/{filename}")


if __name__ == "__main__":
    #delete_duplicate_image_label()
    transfer_image_label()






