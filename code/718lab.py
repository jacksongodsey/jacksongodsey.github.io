def something(x):
    if x == 1:
        done = ("done", "Done")
        d = ("d", "D")
        str1 = input()
        rev1 = ""
        for i in str1:
            if str1 in done:
                return
            elif str1 in d:
                return
            else:
                rev1 = i + rev1
        print(rev1)
        str2 = input()
        rev2 = ""
        for i in str2:
            if str2 in done:
                return
            elif str2 in d:
                return
            else:
                rev2 = i + rev2
        print(rev2)
        str3 = input()
        rev3 = ""
        for i in str3:
            if str3 in done:
                return
            elif str3 in d:
                return
            else:
                rev3 = i + rev3
        print(rev3)


something(1)
