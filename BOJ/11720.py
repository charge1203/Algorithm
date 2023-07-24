n = int(input())

num_list = list(input())
result = 0

while len(num_list) != n:
    print('Enter the same length as the first input number')
    num_list = list(input())

for i in num_list:
    result += int(i)
print(result)