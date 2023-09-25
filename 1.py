x = int(input('Введите искомое число: '))
list = [x for x in range(100)]
list = sorted(list)
k = 0
left, right = 0, len(list)-1
while left <= right:
    k += 1
    mid = (left + right) // 2
    if list[mid] == x:
        break
    elif list[mid] < x:
        left = mid + 1
    else:
        right = mid - 1
print('Number of steps: ', k)
