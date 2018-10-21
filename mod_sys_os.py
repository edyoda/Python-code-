import sys
import os 

# print(sys.version)
# print(sys.executable)
# print(sys.platform)
# print(sys.argv)
# print(sys.path)

# fp = open("test5.txt","w")
# sys.stdout = fp
# print("Hi")

# fp = open("test6.txt","a")
# sys.stderr = fp 
# print(10 / 0)

# Fixed overhead 

# s = 0
# print(sys.getsizeof(s))

# mod1 change 2 algo
# 			1 timestamp based 
# 			2 hashbased => 3.7  

# mod2 cmod1  
os.chdir(r"E:\Tools")
print(os.getcwd())
print(os.listdir())
# os.system(os.listdir()[1])

os.system("dir")