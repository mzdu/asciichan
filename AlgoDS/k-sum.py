def kSum(A, k, target):
    from collections import deque
    dq = deque()
    dq.append([target, set(A)])
    res = 0
    while dq:
        size = len(dq)
        k -= 1
        for _ in xrange(size):
            val, candidates = dq.popleft()
            while candidates:
                candVal = candidates.pop()
                childVal = val - candVal
                if k == 0 and childVal == 0:
                    res += 1
                childCands = set(candidates)
                dq.append([childVal, childCands])
    return res    


A = [1,2,3,4,5]
k = 3
target = 6

print kSum(A, k, target)