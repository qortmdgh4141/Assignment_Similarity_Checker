import pickle
import pandas as pd

# 데이터 불러오기
file_path = f'raw_data/similarity_data_Assignment+1+(Question-1).csv'
df = pd.read_csv(file_path)
quiz_name = df.at[0, 'Quiz name']
df = df[['WriterA - Name', 'WriterB - Name', 'Similarity']]

result_dict = {} # 결과를 저장할 빈 딕셔너리 생성

# 각 행에 대해서 반복
for i in range(len(df)):
    a_name = df.at[i, 'WriterA - Name']
    b_name = df.at[i, 'WriterB - Name']
    similarity_value = df.at[i, 'Similarity']

    tuple_ab = tuple(sorted([a_name, b_name])) # A 학생과 B 학생의 값을 가져와서 정렬한 후, 튜플로 변환
    result_dict[tuple_ab] = similarity_value # 튜플을 딕셔너리의 key로 사용하고, 유사도 값을 딕셔너리의 value로 설정

# 딕셔너리 저장
save_dic = False
if save_dic == True:
    dic_file_path = f"{quiz_name}.pkl"
    with open(dic_file_path, 'wb') as file:
        pickle.dump(result_dict, file)

    with open(dic_file_path, 'rb') as file:
        loaded_dict = pickle.load(file)
    print(loaded_dict)
    print(len(loaded_dict))

else:
    quiz_name_list = ["Assignment 1 (Question-1)", "Assignment 1 (Question-2)",
                      "Assignment 1 (Question-3)", "Assignment 1 (Question-4)"]

    for quiz_name in (quiz_name_list):
        dic_file_path = f"dic_Data\\{quiz_name}.pkl"
        with open(dic_file_path, 'rb') as file:
            loaded_dict = pickle.load(file)
        print(loaded_dict)
        print(len(loaded_dict))