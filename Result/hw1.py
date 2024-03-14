a=input('당신의 주민번호를 입력하세요:')
if len(a)!=14:
    print('올바른 주민번호 입력하세요')
else:
    birth_year=int(a[:2])
    gender=int(a[7])
    if gender==1 or gender==3:
        birth_year+=1900
        gender="남자"
    if gender==2 or gender==4:
        birth_year += 1900
        gender = "여자"

birth_month=a[2:4]
birth_day=a[4:6]
print("나는 {}년 {}월 {}일에 태어난 {}입니다.".format(birth_year,birth_month,birth_day,gender))