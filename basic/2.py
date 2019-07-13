# import my_module as mm
from my_module import find_index, test  # it's better way than below one
# from my_module import *
import sys

courses = ['History', 'Math', 'Physics', 'CompSci']

index = find_index(courses, 'Math')
# print(index)
# print(test)

print(sys.path)

'''
How to add python environment variable :

1. 방법:
내 PC 속성 >> 고급 시스템 설정 >> 환경변수 >> 사용자 변수(새로 만들기)
>> 변수 이름 : PYTHONPATH >> 변수 값 : '추가할 경로' >> 저장

2. 확인:
cmd 실행 >> python 입력 >> import sys 입력 >> sys.path 입력 >> 확인
'''