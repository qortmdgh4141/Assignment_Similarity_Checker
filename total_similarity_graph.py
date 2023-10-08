import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 데이터 불러오기
dic_file_path = f"dic_data\\total_dic.pkl"
with open(dic_file_path, 'rb') as file:
    total_dic = pickle.load(file)

total_dic = dict(sorted(total_dic.items(), key=lambda item: item[1])) # value를 기준으로 딕셔너리를 오름차순 정렬

# 데이터 추출
keys = list(total_dic.keys())
similarity_values = list(total_dic.values())
x = np.arange(len(total_dic))

# 최댓값, 평균, 임계값
max_value = np.array(similarity_values[-1])
average = sum(similarity_values) / len(similarity_values)
# red_threshold = average + (max_value-average)*4/5
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

# 유사도로 line 그래프 그리기 (similarity_values 출력)
plt.figure(figsize=(10, 6))
plt.title('[ Average Similarity from Assignments 1 (Question-1,2,3,4)]\n', fontsize=14)

x = np.arange(len(similarity_values))
plt.plot(x[:threshold_index], similarity_values[:threshold_index], markersize=5, marker='o', linestyle='-', color='blue', label='Below Threshold')
plt.plot(x[threshold_index:], similarity_values[threshold_index:], markersize=5,marker='o', linestyle='-', color='red', label='Above Threshold')
plt.xlabel('\nComparison Between Two Students: Avg (Similarity for Assignments 1~4)')
plt.ylabel('Similarity')
plt.grid(True)

plt.axhline(y = red_threshold, color='red', linestyle='--', label='average') # 그래프에 빨간 점선을 추가
plt.axhline(y = (average), color='green', linestyle='--', label='average') # 그래프에 파란 점선을 추가

plt.show()

# 값이 red_threshold(90) 이상인 키-값 출력 (표절 후보)
total_reverse_dic = dict(sorted(total_dic.items(), key=lambda item: item[1], reverse=True))
threshold_dic = {}
for key, value in total_reverse_dic.items():
    if value >= red_threshold:
        threshold_dic[key] = value
    else:
        break

# 데이터프레임을 엑셀 파일로 저장 (표절 후보)
save_df = True
if save_df ==True:
    data = {
        'Student A': [key[0] for key in threshold_dic.keys()],
        'Student B': [key[1] for key in threshold_dic.keys()],
        'Similarity': list(threshold_dic.values())
    }
    df = pd.DataFrame(data)
    df.to_excel('Similarity_Data.xlsx', index=False)

else:
    print(threshold_dic)
    print(len(threshold_dic))