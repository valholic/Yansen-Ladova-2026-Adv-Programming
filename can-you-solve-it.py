#Before
T = int(input().strip())
for Case in range(1, T + 1):
    print(f"Case {Case}:", end=" ")

    # BUG: reads only two numbers, not four
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        step1 = 0
    else:
        n = x + y - 1
        step1 = (n * n + 3 * n) // 2 + (x + 1)

    # BUG: reads another two numbers separately
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        step2 = 0
    else:
        n = x + y - 1
        step2 = (n * n + 3 * n) // 2 + (x + 1)

    print(step2 - step1)


#After
T = int(input().strip())
for Case in range(1, T + 1):
    x1, y1, x2, y2 = map(int, input().split())

    # hitung step1
    if x1 == 0 and y1 == 0:
        step1 = 0
    else:
        n = x1 + y1 - 1
        step1 = (n * n + 3 * n) // 2 + (x1 + 1)

    # hitung step2
    if x2 == 0 and y2 == 0:
        step2 = 0
    else:
        n = x2 + y2 - 1
        step2 = (n * n + 3 * n) // 2 + (x2 + 1)

    print(f"Case {Case}: {step2 - step1}")