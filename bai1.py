#Bài 1. Biểu diễn số A thành một ma trận (sẽ giới hạn kích thước số A không quá lớn)
#Ví dụ: 
#-	P=2147483647; W=8; Số nguyên a=     
#KQ: A= [2    79   120     1]
#-	P=2147483647; W=8; Số nguyên a=568424364
#KQ: A= [33   225   119   172]
import math

P = 2147483647
W = 8
a = 568424364
#chuongtrinhcon
def chuyenmang(p,w,a):
    m = math.ceil(math.log2(p))
    #print m 
    t = math.ceil(m/w)
    #print t 
    A = []
    for i in range(1,t+1):
        tmp = a//(2**((t-i)*w))
        a = a - tmp*(2**((t-i)*w))
        A.append(tmp)
    return A
print (chuyenmang(P,W,a))


      