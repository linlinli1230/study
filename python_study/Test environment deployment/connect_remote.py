#自动化搭建远程linux系统项目环境
import  paramiko

#创建SSHClient实例对象
ssh=paramiko.SSHClient()

#信任远程机器，允许访问，为固定格式
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

#连接远程机器：地址，端口，用户密码
ssh.connect("192.168.218.3",22,"root","134872")

print('查询指定目录是否存在旧的项目')
stdin,stdout,stderr=ssh.exec_command('ls /var/www/html')
output=stdout.read().decode()
print(output)
if 'thinksns' in output:
    print('存在旧版本，需要先删除')
    '''
    找到运行程序的pid并kill
    parts = output.spilt(' ') #分割输出结果存入列表
    parts = [part for part in parts if part] #去掉列表中的空格
    pid=parts[1]
    ssh.exec_command('kill -9  '+ pid)
    '''
    print('删除原来的项目包')
    ssh.exec_command('rm -rf /var/www/html/thinksns')

print('上传文件')
sftp=ssh.open_sftp()
sftp.put(r'I:\资料\thinksns项目\ThinkSNS_v4.6.1.zip','/var/www/html/ThinkSNS_v4.6.1.zip')
sftp.close()

print('解压项目包...')
#stdin,stdout,stderr =ssh.exec_command('unzip /var/www/html/ThinkSNS_v4.6.1.zip -d /var/www/html')
#stdout.read()#ssh连接可能会在解压缩完成之前关闭。添加stdout.read()，以强制打开连接，直到解压完成

ssh.exec_command('rm -rf /var/www/html/ThinkSNS_v4.6.1.zip')

print ("创建目录修改权限")
ssh.exec_command('mkdir /var/www/html/thinksns/storage')
ssh.exec_command('cd /var/www/html/thinksns;chmod -R 777 storage data install config')
print('项目已配置好，请在浏览器打开项目http://192.168.218.3/thinksns/')






'''
#执行linux命令
ssh.exec_command('echo "this is a text." > /linlin/file1.py')#创建文件并写入内容
#变量分别对应输入，输出，输出错误管道
stdin,stdout,stderr=ssh.exec_command('cat /linlin/file1.py')
#读取输出结果
con=stdout.read().decode()
print(con)
'''