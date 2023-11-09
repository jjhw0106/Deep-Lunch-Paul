def solution(citations):
    answer = 0
    n = len(citations)
    # 내림정렬 후 n번째 책의 인용회수가 n보다 크면 앞의 index애들도 n보다 클것이기 때문에 따져 볼 필요가 없다.
    # n번재 요소 뒤의 애들은 n보다 작아서 통과된 것이기 때문에 신경안써도 된다
    citations.sort(reverse=True)
    for _ in range(n,0,-1):
        if(citations[n-1] >= n):
            return n
        n -= 1

    return answer

print(solution([1,5,5,5,5]))