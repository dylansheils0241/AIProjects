import random

outFileName="C:\\Users\\Administrator\\Desktop\\AIProject\\XORdata.txt"
f=open(outFileName, "w+")

for i in range(1000):
    a = (random.randint(1, 100))
    b = (random.randint(1, 100))
    c = (a ^ b)
    f.write(str(bin(a)) + " " + str(bin(b)) + " " + str(bin(c)) + "\r\n")
    
f.close()

print("Done")
