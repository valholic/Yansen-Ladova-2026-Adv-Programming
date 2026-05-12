list_num = list(map(int, input().split()))
result = []

for num in list_num:
    if num == 0:
        continue

    divisor = ()
    for i in range(1, num):
        if num % i == 0:
            divisor += (i,)

    if sum(divisor) == num:
        result.append("PERFECT")
    elif sum(divisor) < num:
        result.append("DEFICIENT")
    else:
        result.append("ABUNDANT")

print("PERFECTION OUTPUT")
for i in range(len(list_num) - 1):
    print(f"{list_num[i]} {result[i]}")
print("END OF OUTPUT")