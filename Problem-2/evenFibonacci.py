fibList = [1, 2]
sum = 2
while (fibList[-1]<4000000):
  fibList.append(fibList[-1]+fibList[-2])
  if (fibList[-1]%2 == 0 and fibList[-1]<4000000):
    sum += fibList[-1]
    print(fibList[-1])

print(sum)