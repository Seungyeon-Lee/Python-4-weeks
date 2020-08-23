# csv

# input => 코드(리스트 + 딕셔너리)
# output => Excel, csv

import pandas

data = {
 "column1" : [1,2,3,4,5,6],
 "column2" : [11,12,13,14,15,16],
 "column3" : [21,22,23,24,25,26],
 "column4" : [31,32,33,None,35,36],
 "column5" : [41,42,43,44,45,None],
}

df = pandas.DataFrame(data)

# df.to_excel('t1.xlsx') # 엑셀 저장
# df.to_csv('t1.csv') # csv저장

# print(df)

c4 = df['column4']
c3 = df['column3']

new_df = pandas.concat([c3, c4], axis = 1) # axis 기본 값은 0
print(df[df['column4'] < 30])