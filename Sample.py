# Sample.py
# 1. 리스트를 선언합니다.
lst = [1, 3, 5, 7, 9]

def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# 2. 반복문을 사용하여 각 요소를 출력합니다.
for i in lst:
     # 3. 현재 반복 중인 요소(i)를 콘솔에 출력합니다.
    print(i)
    
print("리스트의 합 :", calculate_sum(lst))

