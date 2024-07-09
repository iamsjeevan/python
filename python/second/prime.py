def is_prime(num):
    if num==1:
        return False
    for i in range(2,(int(num**0.5)+1)):
        if num%i == 0:
            return False
        else:
            return True
def prime_in_range(start,end):
    prime_num=[]
    for i in range(start,end+1):
        if is_prime(i):
            prime_num.append(i)
    return prime_num
start=int(input("enter the start of the prime number "))
end=int(input("enter the end of the prime number "))
print(prime_in_range(start, end))
    