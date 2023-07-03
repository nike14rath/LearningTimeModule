#USING TIME FUNCTION AGAIN
# import time
# def usingWhile():
#   i = 0
#   while i< 50000:
#     print(i)
#     i += 1
# def usingFor():
#   for i in range(1,50001):
#     print(i)
# init =time.time()
# usingWhile()
# a = time.time() - init
# usingFor()
# b = time.time() - init
# print(a)
# print(b-a)
import time
# print(4)
# time.sleep(5)
# print("This is printed after 10 seconds")
t = time.localtime()
time_id = time.strftime('%Y-%m-%d %H:%M:%S')
print(time_id)
