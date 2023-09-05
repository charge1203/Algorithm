import sys

n = int(sys.stdin.readline())
lst = []

for _ in range(n):
    name, k, e, m = sys.stdin.readline().split()
    lst.append((name, int(k), int(e), int(m)))

lst = sorted(lst, key=lambda x:x[0])
lst = sorted(lst, key=lambda x:x[3], reverse=True)
lst = sorted(lst, key=lambda x:x[2])
lst = sorted(lst, key=lambda x:x[1], reverse=True)

for i in lst:
    print(i[0])


# 모범답안
n = int(input())  #N 입력 받기
students = []  #학생 정보를 담을 리스트

for _ in range(n):  #모든 학생 정보를 입력받기
    students.append(input().split())

'''
[정렬기준]
1) 두 번쨰 원소를 기준으로 내림차순 정렬
2_ 두 번쨰 원소가 같은 경우, 세 번째 원소를 기준으로 오름차순 정렬
3) 세 번째 원소가 같은 경우, 네 번째 원소를 기준으로 내림차순 정렬
4) 네 번째 원소가 같은 경우, 첫 번째 원소를 기준으로 오름차순 정렬
'''
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in students:
    print(student[0])