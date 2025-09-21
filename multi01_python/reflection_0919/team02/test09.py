"""
<<문제 설명>>
외과의사 머쓱이는 응급실에 온 환자의 응급도를 기준으로 진료 순서를 정하려고 합니다. 정수 배열 emergency가 매개변수로 주어질 때 응급도가 높은 순서대로 진료 순서를 정한 배열을 return하도록 solution 함수를 완성해주세요.

(제한사항)
중복된 원소는 없습니다.
1 ≤ emergency의 길이 ≤ 10
1 ≤ emergency의 원소 ≤ 100

(입출력 예)
emergency	                   result
----------------------     ---------------
[30, 10, 23, 6, 100]   	[2, 4, 3, 5, 1]

(입출력 예 설명)
emergency가 [30, 10, 23, 6, 100]이므로 응급도의 크기 순서대로 번호를 매긴 [2, 4, 3, 5, 1]를 return합니다.
"""


def solution(emergency):
    # emergency 리스트를 내림차순으로 정렬합니다.
    sorted_emergency = sorted(emergency, reverse=True)

    # 원래 emergency 리스트의 각 원소(e)가 정렬된 리스트에서 몇 번째 인덱스에 있는지 찾아 1을 더합니다.
    return [sorted_emergency.index(e) + 1 for e in emergency]

if __name__ == '__main__':
    emergency = [30, 10, 23, 6, 100]
    print(solution(emergency))