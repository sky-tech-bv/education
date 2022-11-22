def main():
    outfile = open('golf_club.txt', 'r')
    for line in outfile:
        value = line.rsplit('\n')
        print(value)
    print("It's done")
    outfile.close()
if __name__ == '__main__':
    main()