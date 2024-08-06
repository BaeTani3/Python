import numpy as np
import matplotlib.pyplot as plt

from sklearn import metrics

# 1. 데이터 준비 : 임의의 랜덤값 100개 생성 (X1, X2) -> (X100, Y100)
#  - 100개의 2차원 데이터 포인트 생성
#  - 각 데이터 포인트는 평균이 6이고 표준편차가 10인 표준정규분포를 따름
X = 10 * np.random.randn(100, 2) + 6 # record 100개 field 2개


from sklearn.cluster import KMeans
# 2.1 K-Means 모델 설정
# K-means 클러스터링 모델을 초기화
# - 클러스터 수를 3으로 설정
# - 클러스터 중심점 계산은 10회 실시
kmeans_model = KMeans(n_clusters=3, n_init=10) 


# 2.2 K-Means 학습 진행
# 데이터에 대하여 K-means 클러스터링을 수행
kmeans_model.fit(X) # fit => 맞춰라! (k-means 학습하라!)

# 3. 학습 후 결과 값 얻기
#  - 클러스터 레이블
#  - 각 클러스터의 중심점 좌표
labels = kmeans_model.labels_  # 각 데이터 포인트의 클러스터 레이블
centers = kmeans_model.cluster_centers_  # 각 클러스터의 중심점

# 4. 클러스터링 결과 시각화
#  - X[:, 0]과 X[:, 1]은 각각 데이터 포인트의 x, y 좌표
#     -> numpy를 활용한 2차원 배열(리스트) 표현법
#     -> numpy는 학기 중 수업 예정
#  - c 파라미터에 클러스터 레이블을 지정하여 다른 클러스터를 다른 색으로 표시.
#     -> 즉 데이터[2차원 배열 X]에서 각 행별로 클러스트 번호(c=label) 매핑
#  - cmap='rainbow'로 색상 맵 설정하여 다양한 색상으로 표현.
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='rainbow')

#  - 각 클러스트별 중심점(Cluseter centroid) 출력
plt.scatter(centers[:, 0], centers[:, 1], c='black', s=200, alpha=0.5)


# 최종 그래프를 화면에 표시.
plt.show()

# 이해를 하려면 3가지를 알아야 한다
# numpy # PCA # matplot