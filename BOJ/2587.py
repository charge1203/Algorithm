nums = []

for _ in range(5):
    nums.append(int(input()))  # 여기 헷갈렸음

print(int(sum(nums)/len(nums)))  # int 해야함

nums.sort()
print(nums[2])