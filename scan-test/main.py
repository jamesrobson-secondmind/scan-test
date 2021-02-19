import sys

i = "hi"
i = "multiple definition"
j = "first"
looks_like_a_passwd = "Eemu0ahvaYaefe3iCiNg"


def problem():
    j = "second"
    z = "new line"
    x = 40
    y = exec("x + 2")
    print(i, j, y, z)
    if sys.argv[1] == looks_like_a_passwdw:
        print("passwd accepted")


if __name__ == "__main__":
    problem()
