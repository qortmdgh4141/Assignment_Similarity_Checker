import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

file_path = r'raw_data/similarity_data_Assignment+1+(Question-1).csv'
df = pd.read_csv(file_path)
quiz_name = df.at[0, 'Quiz name']
df = df[['WriterA - Name', 'WriterB - Name', 'Similarity']]

similarity_values = df['Similarity'].tolist() # Similarity 열만 추출하여 리스트에 저장
similarity_values.sort() # Similarity 값을 기반으로 오름차순으로 정렬

# 최댓값, 평균, 임계값
max_value = np.array(similarity_values[-1])
average = sum(similarity_values) / len(similarity_values)
#red_threshold = average + (max_value-average)*4/5
red_threshold = 90

# 큰 인덱스부터 작은 인덱스로 거꾸로 순회
threshold_index=0
count_greater_than_threshold = []
for i in range(len(similarity_values) - 1, -1, -1):
    if similarity_values[i] > red_threshold:
        count_greater_than_threshold.append(similarity_values[i])
        threshold_index = i
    else:
        break
print(f"Number of data points above the threshold: {len(count_greater_than_threshold)}")

# 유사도로 line 그래프 그리기
plt.figure(figsize=(10, 6))
plt.title('[ Similarity from Assignments 1 (Question-1)]\n', fontsize=14)

# 그래프에 similarity_values 그리기
x = np.arange(len(similarity_values))
plt.plot(x[:threshold_index], similarity_values[:threshold_index], markersize=5, marker='o', linestyle='-', color='blue', label='Below Threshold')
plt.plot(x[threshold_index:], similarity_values[threshold_index:], markersize=5,marker='o', linestyle='-', color='red', label='Above Threshold')
plt.xlabel('\n Comparison Between Two Students')
plt.ylabel('Similarity')
plt.grid(True)

plt.axhline(y = red_threshold, color='red', linestyle='--', label='average') # 그래프에 빨간 점선을 추가
plt.axhline(y = (average), color='green', linestyle='--', label='average') # 그래프에 파란 점선을 추가

# 그래프 출력
plt.show()