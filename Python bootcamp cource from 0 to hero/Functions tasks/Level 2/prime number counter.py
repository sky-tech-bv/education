'''
COUNT PRIMES: Write a function that returns the number of prime numbers that exist up to and including a given number
count_primes(100) --> 25
By convention, 0 and 1 are not prime.
'''

def count_primes(num):
    primes_counter = 0
    for item in range(1, num+1): 
        if item > 1:
            for i in range(2,item):
                if (item%i)==0:
                    break
            else:
                primes_counter += 1
    return primes_counter
                
        
print(count_primes(100))
print(count_primes(200))
print(count_primes(1121))