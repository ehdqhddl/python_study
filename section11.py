# Section11
# 파이썬 외부 파일 처리
# 파이썬 Excel, CSV 파일 읽기 및 쓰기

# CSV : MIME - text/csv

# 예제 1
print()
print('--------------예제 1--------------')
print()

import csv

with open('./resource/sample1.csv','r') as f:
    reader = csv.reader(f)
    # 확인
    print(reader)

    next(reader) # Header를 스킵할 때 사용

    for csv_data in reader:
        print(csv_data)


# 예제 2
print()
print('--------------예제 2--------------')
print()

with open('./resource/sample2.csv','r') as f:
    reader = csv.reader(f,delimiter = '|')

    next(reader) # Header를 스킵할 때 사용

    for csv_data in reader:
        print(csv_data)


# 예제 3 (Dict 변환)
print()
print('--------------예제 3--------------')
print()
with open('./resource/sample1.csv','r') as f:
    reader = csv.DictReader(f)

    for csv_data in reader:
        for k,v in csv_data.items():
            print(k,v)
        print('-------------------------')


# 예제 4
print()
print('--------------예제 4--------------')
print()

w = [[1,2,3],[4,5,6],[7,8,9],[11,12,13],[14,15,16],[17,18,19]]

with open("./resource/sample3.csv","w", newline='') as f:
    wt = csv.writer(f)

    for v in w:
        wt.writerow(v) # 데이터의 전처리가 필요할 때 

# 예제 5
print()
print('--------------예제 5--------------')
print('내용 입력 예제')
print()

with open("./resource/sample4.csv","w", newline='') as f:
    wt = csv.writer(f)
    wt.writerows(w) # 전처리 없이 한번에 내용을 입력할 때


# 예제 6 Excel 읽기 (XSL,XLSX)
# openpyxl, xlswriter, xlrd, xlwt, xlutils 다양하게 있지만,
# pandas 를 주로 사용(openpyxl, xlrd를 내부적으로 사용)
# pip install xlrd
# pip install openpyxl
# pip install pandas
# 가상환경에서 실행시 반드시 인터프리터를 설정해주어야 함. 
# Shift + Ctrl + P 눌러서 Python interpreter 검색하여 설정

import pandas as pd

# sheetname = '시트명' 또는 숫자, header = 숫자, skiprow = 숫자

xlsx = pd.read_excel('./resource/sample.xlsx')

# 상위 데이터 확인
print(xlsx.head())

# 데이터 확인
print(xlsx.tail())

# 데이터 확인 (행, 열)
print(xlsx.shape)


# 엑셀 or CSV 다시 쓰기
xlsx.to_excel('./resource/result.xlsx',index = False)
xlsx.to_csv('./resource/result.csv',index = False)