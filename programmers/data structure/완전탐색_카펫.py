def solution(brown, yellow):
    for i in range(1,brown+yellow):
        if (brown+yellow)%i == 0:
            h = i
            w = (brown+yellow)//i
            if (h-2)*(w-2) == yellow:
                return [w,h]
