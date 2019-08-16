import pymysql


class SaveToMySQL():
    def __init__(self, host, port, user, password, database, table, datas):
        """
        :param host: 地址
        :param port: 端口号
        :param user: 用户
        :param password: 密码
        :param database: 数据库
        :param table: 表名
        :param datas: 数据
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.table = table
        self.datas = datas[:-1].split("\n")

    def save_to_MySQL(self, split_by):
        try:
            conn = pymysql.connect(host=self.host, port=self.port,
                                   user=self.user,
                                   password=self.password,
                                   database=self.database)
            cursor = conn.cursor()
            for data in self.datas:
                list_data = data.split(split_by)
                list_grade = list_data[-1].split("：")
                time = list_data[2].split("(")[0]
                grade = float(list_grade[-1])
                sql = "insert into %s(name,act,time,grade) value ('%s','%s','%s',%2.1f);" % \
                      (self.table, list_data[0], list_data[1], time, grade)
                cursor.execute(sql)
                conn.commit()
            cursor.close()
            conn.close()
            return True
        except Exception as e:
            print(e)
            return False
