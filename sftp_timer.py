import time
from main import main


BASIC_PATH = "/data02/cgp_sftp"
USER = "cp"
PASSWORD = "12345"
HOST = "192.168.2.203"
local_path = input("请输入临时文件存放地址>>")

while True:
    time_now = time.strftime("%H:%M:%S", time.localtime()) # 刷新
    if time_now == "22:02:00":
        main(basic_path=BASIC_PATH, user=USER, password=PASSWORD,
             host=HOST, local_path=local_path, timeout=10)
    time.sleep(2)