import math


def minDistance(word1, word2):
    wl1, wl2 = len(word1), len(word2)
    dp = [[0] * (wl2 + 1) for _ in range(wl1 + 1)]

    for i in range(wl1 + 1):
        dp[i][0] = i

    for j in range(wl2 + 1):
        dp[0][j] = j

    for i in range(1, wl1 + 1):
        for j in range(1, wl2 + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1

    trace = []
    y1 = y = wl1
    x1 = x = wl2

    # for r in dp:
    #     print(r)

    i = 0
    while y > 0 or x > 0:
        # print(f"i={i}")
        # print(f"dp[{y}][{x}]={dp[y][x]}")
        # print(f"word2[{y - 1}]={word1[y - 1]},word2[{x - 1}]={word2[x - 1]}")

        m = math.inf
        dx_dy = [(-1, -1), (-1, 0), (0, -1)]
        for dx, dy in dx_dy:
            if x + dx >= 0 and y + dy >= 0:
                if dp[y+dy][x+dx] < m:
                    y1 = y + dy
                    x1 = x + dx
                    m = dp[y1][x1]
                    # print(f"dx={dx}, dy={dy}, max={m}")

        # print(f"dp[{y1}][{x1}]={dp[y1][x1]}, max={m}")
        # print(f"word1[{y1-1}]={word1[y1-1]},word2[{x1-1}]={word2[x1-1]}")

        if x - x1 == 1 and y - y1 == 1:
            if dp[y1][x1] == dp[y][x]:
                trace.append(word2[x-1])
            else:
                trace.append(f"({word1[y-1]},{word2[x-1]})")
        elif y1 == y:
            trace.append(f"+({word2[x-1]})")
        elif x1 == x:
            trace.append(f"-({word1[y-1]})")
        else:
            raise f"can't reach that point! i={i}; x,y=({x},{y}); x1,y1=({x1},{y1})"

        y = y1
        x = x1
        i += 1

    trace.reverse()
    trace = "_".join(trace)
    # print(word1)
    # print(trace)
    # print(word2)
    return dp[wl1][wl2], trace

#     h o r  s  e
#   0 1 2 3  4  5
# r 1
# o 2       y1 y2
# s 3       y3  x
# x = i,j = 3,5
# "horse"
# "ros"
#
# horse -> rorse (replace 'h' with 'r')
# rorse -> rose (remove 'r')
# rose -> ros (remove 'e')
#
# y1 = dp[2, 4]
# "hors"
# "ro"
# dp[2,4] = 1+1+1= 3
#
# y2 = dp[2, 5]
# "horse"
# "ro" + "s"
#
# y3 = dp[3, 4]
# "hors" + "e"
# "ros"
#
#
# m = 5
# n = 3
