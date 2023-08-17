numbers = [1,1,1,1,1]
target = 3

def solution(numbers, target, depth):
	answer = 0
	
	def dfs(numbers, target, depth):
		nonlocal answer
		
		if depth == len(numbers):
			sum = 0
			for e in numbers:
				sum += e
			if sum == target:
				answer += 1
		else:
			numbers[depth] *= 1
			dfs(numbers, target, depth + 1)
			numbers[depth] *= -1
			dfs(numbers, target, depth + 1)
			
	dfs(numbers, target, depth)
	print(answer)
	return answer

solution(numbers, target, 0)  
	