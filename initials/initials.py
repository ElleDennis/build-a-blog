def get_initials(fullname):
    fullnameCap = fullname.title()
    names = fullnameCap.split()
    initials = ""
    for aname in names:
        initials = initials + aname[0]
    return initials


def main():
    for_answer = input("What is your full name?")
    print(for_answer)
    print(get_initials(for_answer))

if __name__ == '__main__': main()
