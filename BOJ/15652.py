import sys

a = [int(i) for i in sys.stdin.readline().split()]
chk = [0] * a[0]  # 숫자의 범위
arr = [0] * a[1]  # 배열의 자리수


def back(k, pre):  # k가 현재 상태, pre가 이전상태
    if k == a[1]:
        print(*arr)
        return
    else:
        for idx, i in enumerate(chk):  # idx가 0, 1, 2, 3
            if arr[pre] <= idx + 1:
                arr[k] = idx + 1  # 1, 2, 3, 4값 기입
                back(k + 1, k)

back(0, 0)