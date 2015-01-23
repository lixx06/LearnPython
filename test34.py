# coding: UTF-8

import subprocess

cmd = "bash"
begin = 101
end = 200
while begin < end:
    p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE,
                   stdin = subprocess.PIPE,
                   stderr = subprocess.PIPE)
    p.stdin.write("ping -c 2 192.168.1." + str(begin) + "\n")
    p.stdin.close()
    p.wait()
    print "execution result: %s"%p.stdout.read()
    begin = begin + 1


