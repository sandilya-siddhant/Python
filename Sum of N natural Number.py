#Assignment - Write a program to calculate the sum of N natural No.

n=int(input("Write any No.:"))
total_sum = 0
for i in range (1,n+1):
    total_sum += i
    print(total_sum)
