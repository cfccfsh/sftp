import os
import SaveToMySQL

HOST = "127.0.0.1"
PORT = 3306
USER = "root"
PASSWORD = "123456"
DATABASE = "SaveData"
TABLE = "data"
SPLIT_BY = "  "


class ReadFile(object):
    def __init__(self, path):
        self.path = path
        self.count = 1
        self.res = ""

    def save_sql(self, datas):
        db = SaveToMySQL.SaveToMySQL(host=HOST, port=PORT,
                                     user=USER,
                                     password=PASSWORD,
                                     database=DATABASE,
                                     table=TABLE,
                                     datas=datas)
        return db

    def read_remove_file(self):
        list_file = os.listdir(self.path)
        for file in list_file:
            file = self.path + "/" + file
            size = os.path.getsize(file)
            if size != 0:
                with open(file, "r") as f:
                    while file:
                        line = f.readline()
                        if line != "":
                            if self.count % 5 != 0:
                                self.res += line
                                self.count += 1
                            else:
                                self.res = self.res + line
                                db = self.save_sql(self.res)
                                db.save_to_MySQL(SPLIT_BY)
                                self.res = ""
                                self.count = 1
                        else:
                            if self.res != "":
                                db = self.save_sql(self.res)
                                db.save_to_MySQL(SPLIT_BY)
                                os.remove(file)
                                break
                            else:
                                os.remove(file)
                                break
            else:
                print([])


if __name__ == '__main__':
    path = "/home/fsh/AUG08"
    re = ReadFile(path)
    re.read_remove_file()
