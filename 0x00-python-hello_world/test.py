def solution(A, B, C):

    new_list = []

    LA = A
    LB = B
    LC = C

    la = 0
    lb = 0
    lc = 0

    if A:
        for i in range(A):

            new_list.append("a")
    if B:
        for i in range(B):

            new_list.append("b")
    if C:
        for i in range(C):

            new_list.append("c")

    return new_list


if __name__ == '__main__':
    print(solution(1, 2, 3))
