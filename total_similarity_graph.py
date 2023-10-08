import pickle
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

dic_file_path = f"total_dic.pkl"
with open(dic_file_path, 'rb') as file:
    total_dic = pickle.load(file)

total_dic = dict(sorted(total_dic.items(), key=lambda item: item[1])) # value를 기준으로 딕셔너리를 오름차순 정렬

# 유사도로 line 그래프 그리기
plt.figure(figsize=(10, 6))
plt.title('[ Average Similarity from Assignments 1 (Question-1,2,3,4)]\n', fontsize=14)

# 그래프 데이터 추출
keys = list(total_dic.keys())
similarity_values = list(total_dic.values())
x = np.arange(len(total_dic))

max_value = np.array(similarity_values[-1])
average = sum(similarity_values) / len(similarity_values)
# red_threshold = average + (max_value-average)*4/5
red_threshold = 90

for i in range(len(similarity_values) - 1, -1, -1):
    if similarity_values[i] > red_threshold:
        threshold_index = i
    else:
        break

x = np.arange(len(similarity_values))
plt.plot(x[:threshold_index], similarity_values[:threshold_index], markersize=5, marker='o', linestyle='-', color='blue', label='Below Threshold')
plt.plot(x[threshold_index:], similarity_values[threshold_index:], markersize=5,marker='o', linestyle='-', color='red', label='Above Threshold')

plt.xlabel('\nComparison Between Two Students: Avg (Similarity for Assignments 1~4)')
plt.ylabel('Similarity')
plt.grid(True)

# 그래프에 빨간 점선을 추가
plt.axhline(y = red_threshold, color='red', linestyle='--', label='average')
# 그래프에 파란 점선을 추가
plt.axhline(y = (average), color='green', linestyle='--', label='average')

# 그래프 출력
plt.show()

total_reverse_dic = dict(sorted(total_dic.items(), key=lambda item: item[1], reverse=True))
threshold_dic = {}

# 값이 red_threshold(90) 이상인 키-값 출력
for key, value in total_reverse_dic.items():
    if value >= red_threshold:
        threshold_dic[key] = value
    else:
        break

save_df = True
if save_df ==True:
    data = {
        'Student A': [key[0] for key in threshold_dic.keys()],
        'Student B': [key[1] for key in threshold_dic.keys()],
        'Similarity': list(threshold_dic.values())
    }

    df = pd.DataFrame(data)

    # 데이터프레임을 엑셀 파일로 저장
    df.to_excel('Similarity_Data.xlsx', index=False)

else:
    print(threshold_dic)
    print(len(threshold_dic))