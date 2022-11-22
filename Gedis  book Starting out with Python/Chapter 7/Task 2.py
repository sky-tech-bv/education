import random
def main():
    aver = 7
    list = []
    result = 0
    for x in range (aver):
        list.append(random.randint(0,9))
    print(list)
    for num in list:
        print(num)
if __name__ == '__main__':
    main()