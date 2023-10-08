import pickle

def load_dic(quiz_name):
    dic_file_path = f"{quiz_name}.pkl"
    with open(dic_file_path, 'rb') as file:
        loaded_dict = pickle.load(file)

    return loaded_dict

# 데이터 불러오기
quiz_name_list = ["Assignment 1 (Question-1)", "Assignment 1 (Question-2)",
                  "Assignment 1 (Question-3)", "Assignment 1 (Question-4)"]
dic_1={}; dic_2={}; dic_3={}; dic_4={};
all_dicts = [dic_1, dic_2, dic_3, dic_4]

for i in range(len(all_dicts)):
    all_dicts[i] = load_dic(quiz_name_list[i])

# main_dic : 가장 큰 크기를 가지는 딕셔너리, sub_dic_lsit : 나머지 딕셔너리
main_dic = max(all_dicts, key=len)
sub_dict_list = [d for d in all_dicts if d != main_dic]
result_dic= {}

# 각 딕셔너리의 key를 기반으로, 평균 유사도 값을 구한 후 딕셔너리에 저장
for key in main_dic:
    key1_value = main_dic[key]
    sub_value = 0
    for i in range(len(sub_dict_list)):
        sub_value += sub_dict_list[i].get(key, 0)

    result_value = ((key1_value + sub_value)) / 4
    result_dic[key] = result_value

# 딕셔너리 저장
save_dic = True
if save_dic == True:
    dic_file_path = f"total_dic.pkl"
    with open(dic_file_path, 'wb') as file:
        pickle.dump(result_dic, file)

    with open(dic_file_path, 'rb') as file:
        loaded_dict = pickle.load(file)
    print(loaded_dict)
    print(len(loaded_dict))

else:
    dic_file_path = f"total_dic.pkl"
    with open(dic_file_path, 'rb') as file:
        loaded_dict = pickle.load(file)
    print(loaded_dict)
    print(len(loaded_dict))