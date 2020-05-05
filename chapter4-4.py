def collect():
    PETER = NANCY = MARY = none = 0
    for i in range(1, 11):
        print("1: PETER")
        print("2: NANCY")
        print("3: MARY")
        count = eval(input("WHICH ONE DO YOU PREFER : "))
        if count == 1:
            PETER += 1
        elif count == 2:
            NANCY += 1
        elif count == 3:
            MARY += 1
        else:
            none += 1
        print("\n PETER: %d , NANCY: %d , MARY: %d" % (PETER, NANCY, MARY))

    print("\n PETER: %d , NANCY: %d , MARY: %d" % (PETER, NANCY, MARY))
    print("Invalid:%d" % (none))


if __name__ == "__main__":
    collect()
