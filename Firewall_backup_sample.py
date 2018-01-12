#!/usr/bin/python

import paramiko
import time

timestamp = time.strftime("%Y%m%d")

copy = "copy run ftp://path/to/folder-"+timestamp+" "

def disable_paging(remote_conn):

    remote_conn.send("terminal length 0\n")
    time.sleep(1)
    output = remote_conn.recv(1000)
    return output

if __name__ == '__main__':

    ip = 'x.x.x.x'
    username = 'fw-username'
    password = 'fw-password'
remote_conn_pre = paramiko.SSHClient()

remote_conn_pre.set_missing_host_key_policy(
         paramiko.AutoAddPolicy())

remote_conn_pre.connect(ip, username=username, password=password,)
remote_conn = remote_conn_pre.invoke_shell()
output = remote_conn.recv(1000)

disable_paging(remote_conn)

remote_conn.send("\n")
remote_conn.send(" "+copy+" \n")
remote_conn.send("\n")
remote_conn.send("\n")
remote_conn.send("\n")
time.sleep(2)
