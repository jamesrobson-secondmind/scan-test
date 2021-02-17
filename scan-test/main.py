i = "hi"
i = "multiple definition"
j = "first"


def problem():
    j = "second"
    x = 40
    y = exec("x + 2")
    print(i, j, y)


if __name__ == "__main__":
    problem()
