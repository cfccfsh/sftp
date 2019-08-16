import os
# from threading import Thread
# from

PATH = "/home/fsh/58crawl"

def readfile(path):
    # 读取文件目录下的文件
    files = os.listdir(path)
    # 每5次进行一次存取
    count = 1
    res = ""
    amount_file_list = []
    for file in files:
        file = path+"/"+file
        # 判断是否为文件夹，是则进入文件夹
        list_file = if_dir(file)
        amount_file_list.extend(list_file)
    for file in amount_file_list:
        size = os.path.getsize(file)
        if size != 0:
            with open(file,"r") as f:
                while file:
                    line = f.readline()
                    if line != "":
                        if count%5 != 0 :
                            res += line
                            count += 1
                        else:
                            res = res+line
                            yield res
                            res = ""
                            count = 1
                    else:
                        list_str = list(res)
                        print("".join(list_str))
                        yield res
                        break
        else:
             print([])


def if_dir(file):
    list_path = []
    if os.path.isdir(file):
        list_dir = os.listdir(file)
        for item in list_dir:
            if os.path.isdir(item):
                return if_dir(item)
            else:
                list_path.append(item)
    else:
        list_path.append(file)
    return list_path


if __name__ == '__main__':
    path = "/home/fsh/PycharmProjects/SftpToMysql"
    a = readfile(path)
    print(a)
    for x in a:
        print(x)
    print(2 % 5)
# import os
#
# print(os.path.isdir("/home/fsh/58crawl/.idea/inspectionProfiles"))