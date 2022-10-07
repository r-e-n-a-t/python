# В файле находится N натуральных чисел, записанных через пробел. Среди чисел не хватает одного, чтобы выполнялось условие A[i] - 1 = A[i-1]. Найдите это число.
# Пример: Ввод: 1 2 4 5 -> 3

nums = list(map(int, open('file', 'r').read().split()))
nums.sort()
for i in range(len(nums) - 1): 
    if nums[i] + 1 != nums[i + 1]: print(nums[i] + 1)
