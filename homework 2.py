nums = []
sums1 = 0
sums2 = 0
for i in range(1, 1001):
    if i % 2 != 0:
        nums.append(i ** 3)
    for idx in range(len(nums)):
     num_sum = 0
     j = nums[idx]
     while j:
         num_sum += j % 10
         j = j // 10
         if num_sum % 7 == 0:
             sums1 += nums[idx]
             nums[idx] += 17
             num_sum = 0
             j = nums[idx]
             while j:
                 num_sum += j % 10
                 j = j // 10
                 if num_sum % 7 == 0:
                     sums2 += nums[idx]
                     print(sums1)
                     print(sums2)