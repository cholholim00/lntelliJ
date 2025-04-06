import heapq
# UCS(Uniform Cost Search) 알고리즘을 구현하기 위한 예제 코드입니다.
#힙 알고리즘 2개

# 1. 힙 기초 구현해보기

def priority_queue_example1():
    # 최소 힙 초기화
    heap = []
    
    # 힙에 값 추가 (우선순위, 값)
    heapq.heappush(heap, (23, "Task 1")) #
    heapq.heappush(heap, (27, "Task 2")) #
    heapq.heappush(heap, (34, "Task 3")) #
    heapq.heappush(heap, (12, "Task 4")) #
    heapq.heappush(heap, (45, "Task 5")) #
    
    # 힙에서 값 꺼내기 (우선순위가 낮은 값부터 꺼낸다)
    while heap:
        priority, task = heapq.heappop(heap)
        print(f"우선순위: {priority}, 작업: {task}")

# 실행
priority_queue_example1()

print("#####################################################################")

# 2. 최소값,최대값 구현해보기
def find_min_and_max(num):
    #최소 힙 생성
    heapq.heapify(num) # 리스트를 힙 구조로 변환
    min_value = num[0]  # 최소값은 힙의 루트 노드
    max_value = max(num)  # 최대값은 리스트에서 직접 찾기
    return min_value, max_value

# 실행
num = [5, 3, 10, 4, 2]
min_value, max_value = find_min_and_max(num)
print(f"최소값: {min_value}, 최대값: {max_value}")

print("#####################################################################")

# 우선 큐 2개

# 1. 우선순위 큐 기초 구현해보기(문자열로)

def priority_queue_example2():
    # 우선순위 큐 초기화
    queue = []
    
    # 우선순위 큐에 값 추가 (우선순위, 작업)
    heapq.heappush(queue, ("사이버", "Task A"))  # 우선순위 3
    heapq.heappush(queue, ("해킹", "Task B"))  # 우선순위 5
    heapq.heappush(queue, ("보안", "Task C"))  # 우선순위 2
    heapq.heappush(queue, ("네트워크", "Task B"))  # 우선순위 1
    heapq.heappush(queue, ("프로그래밍", "Task E"))  # 우선순위 4
    
    print("우선순위 큐 상태:", queue)
    
    # 우선순위가 낮은 값부터 꺼내기
    while queue:
        priority, task = heapq.heappop(queue)
        print(f"우선순위: {priority}, 작업: {task}")

# 실행
priority_queue_example2()

print("#####################################################################")

# 2. 우선순위 큐로 숫자를 정렬해보기

def priority_queue_sort():
    # 우선순위 큐 초기화
    queue = []
    
    # 우선순위 큐에 숫자 추가
    numbers = [5, 1, 8, 3, 2]
    for num in numbers:
        heapq.heappush(queue, num)
    
    print("우선순위 큐 상태:", queue)
    
    # 우선순위가 낮은 숫자부터 꺼내기
    sorted_numbers = []
    while queue:
        sorted_numbers.append(heapq.heappop(queue))
    
    print("정렬된 숫자:", sorted_numbers)

# 실행
priority_queue_sort()

print("#####################################################################")

def main():
    print("실행할 기능을 선택하세요:")
    print("1: 힙 기초 구현")
    print("2: 최소값, 최대값 찾기")
    print("3: 우선순위 큐 기초 구현 (문자열)")
    print("4: 숫자 정렬")
    
    choice = input("선택 (1/2/3/4): ")
    print("#####################################################################")

    # 스위치 문과 유사한 딕셔너리 구조
    options = {
        "1": priority_queue_example1,
        "2": lambda: print(f"최소값: {find_min_and_max([5, 3, 10, 4, 2])[0]}, 최대값: {find_min_and_max([5, 3, 10, 4, 2])[1]}"),
        # lambda 내부에서 복잡한 처리를 제거하고, 함수 호출만 수행하도록 단순화했습니다.
        "3": priority_queue_example2,
        "4": priority_queue_sort
    }

    # 선택된 함수 실행
    if choice in options:
        options[choice]()
    else:
        print("잘못된 선택입니다.")

# 실행
if __name__ == "__main__":
    main()