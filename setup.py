import subprocess
b = subprocess.getstatusoutput(f'pip3 install termcolor')
print(" ")
print(b[1])

