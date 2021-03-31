for _ in range(int(input())):
    n = int(input())

    dp = [[0 for _ in range(n)] for _ in range(2)]
    maps = []

    for _ in range(2):
        maps.append(list(map(int, input().split())))
        
    dp[0][0] = maps[0][0]
    dp[1][0] = maps[1][0]  
        
    for x in range(1, n):
        for y in range(2):
            a = dp[y][x-1]-maps[y][x-1]
            b = dp[y-1][x-1] if y == 1 else dp[y+1][x-1]
            if b > a:
                dp[y][x] = b + maps[y][x]
            else:
                dp[y][x] = a + maps[y][x]
        
    print(max(dp[0][-1], dp[1][-1]))   
        