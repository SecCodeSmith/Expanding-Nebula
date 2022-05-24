from Solution import solution

if solution([[True, True, False, True, False, True, False, True, True, False], [True, True, False, False, False, False, True, True, True, False], [True, True, False, False, False, False, False, False, False, True], [False, True, False, False, False, False, True, True, False, False]]) == 11567:
    print("1: Test pass")
else:
    print("1: Test fail")

if solution([[True, False, True], [False, True, False], [True, False, True]]) == 4:
    print("2: Test pass")
else:
    print("2: Test fail")

if solution([[True, False, True, False, False, True, True, True], [True, False, True, False, False, False, True, False], [True, True, True, False, False, False, True, False], [True, False, True, False, False, False, True, False], [True, False, True, False, False, True, True, True]]) == 254:
    print("3: Test pass")
else:
    print("3: Test fail")