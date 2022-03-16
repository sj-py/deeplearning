# *******************************
# numpy의 기본 지식
# 1차원 배열은 벡터
# 2차원 배열은 행렬
# 벡터와 행렬을 일반화한 것을 텐서
# 3차원 이상은 다차원
# *******************************

import numpy as np

# n차원 array 선언 (n차원 배열 선언)
a = np.array([[1,2], [3,4]])
b = np.array([[3,0], [0,6]])
print(a)
print(b)

# 행렬(각 배열)의 형상 알기 a.shape //형상:각 차원의 크기(원소 수)
# 출력 (2,2) 1행 2개 2행 2개
print(a.shape)
print(b.shape)

# 행렬에 담긴 원소의 자료형
print(a.dtype)
print(b.dtype)

# 행렬의 산술 연산
print(a+b)
print(a*b)
print(a*10)