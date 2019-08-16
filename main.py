import handler_sftp
import readfile
import paramiko
from threading import Thread,Lock
import queue

q = queue.Queue(maxsize=10)
lock = Lock()


def run_code(basic_path,dir,user,password,host,local_path):
    """
    读取sftp，本地读取文件，存入数据库
    :param basic_path: 基础路径
    :param dir: 文件夹
    :param user: 用户
    :param password:密码
    :param host: 地址
    :param local_path:本地路径
    :return:
    """
    lock.acquire()
    dir_path = basic_path + dir
    handler = handler_sftp.HandlerFtpFile(host=host, server_path=dir_path,
                                          local_path=local_path)
    handler.sftp_down_remove_file(user=user, password=password)
    read_file = readfile.ReadFile(local_path)
    read_file.read_remove_file()
    lock.release()



def thread_run(basic_path,user,password,host,local_path):
    """
    :param basic_path: 基础路径
    :param user: 用户
    :param password: 密码
    :param host: 地址
    :param local_path: 本地路径
    :return:
    """
    thread_list = []
    for i in range(4):
        if not q.empty():
            dir = q.get()
            t = Thread(target=run_code, args=(basic_path,dir,user,password,host,local_path))
            t.start()
            thread_list.append(t)

    for t in thread_list:
        t.join()


def main(basic_path, user, password, host, local_path, timeout=10):
    """
    :param basic_path: 基本路径
    :param user: 用户
    :param password:密码
    :param host: 地址
    :param local_path: 本地路径
    :param timeout: 超时时限
    :return: bool
    """
    try:
        t = paramiko.Transport((host, 22))
        t.banner_timeout = timeout
        t.connect(username=user, password=password)
        sftp = paramiko.SFTPClient.from_transport(t)
        dirs = sftp.listdir(basic_path)
        for dir in dirs:
            q.put(dir)
        # run_code(basic_path=basic_path,user=user,password=password,
        #          host=host,local_path=local_path)
        thread_run(basic_path=basic_path,user=user,password=password,
                 host=host,local_path=local_path)
        return True
    except Exception as e:
        print(e)
        return False


if __name__ == '__main__':
    basic_path = "/data/"
    user = "cp"
    password = "12345"
    host = "192.168.2.203"
    local_path = "/home/fsh/AUG08"
    main = main(basic_path=basic_path, user=user, password=password,
                host=host, local_path=local_path)
    print(main)
