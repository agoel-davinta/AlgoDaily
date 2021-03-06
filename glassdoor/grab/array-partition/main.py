def solution(T):
    # find the max from the front
    greater = len(T) * [0]
    greater[0] = T[0]
    for i in range(1, len(T)):
        greater[i] = max(T[i], greater[i-1])
    # find the min from the end
    smaller = len(T) * [0]
    smaller[-1] = T[-1]
    for i in range(len(T)-2, -1, -1):
        smaller[i] = min(T[i], smaller[i+1])
    # when max[i-1] <= max[i] < min[i+1], it is the target index of the last item in the winter peroid
    for i in range(len(T)-1):
        if i == 0:
            if greater[i] <= smaller[i+1]:
                return i + 1
        else:
            now = greater[i]
            g = greater[i-1]
            s = smaller[i+1]
            if g <= now and now <= s:
                return i+1
    # wont go here because the question mentions that there must be one result
    return -1


# 3
print(solution([5, -2, 3, 8, 6]))
# 4
print(solution([-5, -5, -5, -42, 6, 12]))
# 4
print(solution([5, -2, 3, -1, 6]))
# 4
print(solution([1, 2, 3, 4, 5, 6]))
# 1
print(solution([1, 1]))
