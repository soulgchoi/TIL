import csv

with open('lunch.csv', 'r', encoding='utf-8') as f:  # 파일을 열고나서 f라고 부르겠다  # 열린 파일은 이 아래 블럭에서만 동작
    items = csv.reader(f)
    for item in items:
        print(item)
