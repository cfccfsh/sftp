import paramiko


class HandlerFtpFile():
    def __init__(self, host, server_path, local_path):
        """
        :param host: 主机名
        :param server_path: 远程路径
        :param local_path: 本地路径
        """
        self.host = host
        self.server_path = server_path
        self.local_path = local_path

    def sftp_down_remove_file(self, user, password, timeout=10):
        """
        下载文件，注意：不支持文件夹
        :param user: 用户名
        :param password: 密码
        :param timeout: 超时时间(默认)，必须是int类型
        :return: bool
        """
        try:
            t = paramiko.Transport((self.host, 22))
            t.banner_timeout = timeout
            t.connect(username=user, password=password)
            sftp = paramiko.SFTPClient.from_transport(t)
            files = sftp.listdir(self.server_path)
            for file in files:
                try:
                    file_path = self.server_path + "/"+file
                    local_file_path = self.local_path +"/" + file
                    print(file_path)
                    sftp.get(file_path, local_file_path)
                    sftp.remove(file_path)

                except Exception as e:
                    print(e)
            t.close()
            return True
        except Exception as e:
            print(e)
            return False

    # def ssh_exec_command(self,user,password, cmd, timeout=10):
    #     """
    #     使用ssh连接远程服务器执行命令
    #     :param user: 用户名
    #     :param password: 密码
    #     :param cmd: 执行的命令
    #     :param timeout: 超时时间(默认)，必须是int类型
    #     :return: dict
    #     """
    #     result = {'status': 1, 'data': None}  # 返回结果
    #     try:
    #         ssh = paramiko.SSHClient()  # 创建一个新的SSHClient实例
    #         ssh.banner_timeout = timeout
    #         # 设置host key,如果在"known_hosts"中没有保存相关的信息, SSHClient 默认行为是拒绝连接, 会提示yes/no
    #         ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    #         ssh.connect(self.host, 22, user, password, timeout=timeout)  # 连接远程服务器,超时时间1秒
    #         stdin, stdout, stderr = ssh.exec_command(cmd, get_pty=True, timeout=timeout)  # 执行命令
    #         print(1)
    #         out = stdout.readlines()  # 执行结果,readlines会返回列表
    #         # 执行状态,0表示成功，1表示失败
    #         channel = stdout.channel
    #         status = channel.recv_exit_status()
    #         ssh.close()  # 关闭ssh连接
    #
    #         # 修改返回结果
    #         result['status'] = status
    #         result['data'] = out
    #         return result
    #     except Exception as e:
    #         print(e)
    #         print("错误, 登录服务器或者执行命令超时!!! ip: {} 命令: {}".format(self.host, cmd))
    #         return False


if __name__ == '__main__':
    host = "192.168.2.203"
    local_path = "/home/fsh/AUG08/test.text"
    user = "cgp"
    password = "cgp12345"
    server_path = "/data/test.text"
    dir_path = "/data/"
    ftp = HandlerFtpFile(host=host, local_path=local_path, server_path=server_path)
    ftp.sftp_down_remove_file(user="cgp", password=password)
    # status = ftp.ssh_exec_command(user=user,password=password,cmd="rm "+server_path)
    # print(status)
