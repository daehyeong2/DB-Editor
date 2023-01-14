import pymysql
import time

conn = pymysql.connect(host="localhost", user="root", password="1234", db="DataBase", charset="utf8")
cursor = conn.cursor()
curs = conn.cursor(pymysql.cursors.DictCursor)
curs.execute("select * from table1;")
rows = curs.fetchall()

def home():
    n = int(input("1 : 항목 추가\n2 : 항목 삭제\n3 : 전체 항목 보기\n4 : 항목 수정\n5 : 프로그램 종료 및 변경사항 저장\n선택 : "))
    if n==1:
        n2,n3,n4,n5 = input("데이터 입력 ( 이름, 컬럼1, 컬럼2, 컬럼3 ) : ").split()
        cursor.execute(f'INSERT INTO table1 (name, Column1, Column2, Column3) VALUES ("{n2}", "{n3}", "{n4}", "{n5}")')
        print("데이터 추가 완료!")
        time.sleep(1)
        print("------------------------------")
        home()
    elif n==2:
        n2 = input("삭제할 데이터 이름 입력 : ")
        cursor.execute(f"DELETE FROM table1 WHERE name='{n2}'")
        print("삭제 완료!")
        time.sleep(1)
        print("------------------------------")
        home()
    elif n==3:
        for row in(rows):
            print("------------------------------")
            print(f"name : {row['name']}")
            print(f"Column1 : {row['Column1']}")
            print(f"Column2 : {row['Column2']}")
            print(f"Column3 : {row['Column3']}")
        n = input("돌아가기 (y/n) : ")
        if n == "y":
            print("------------------------------")
            home()
        else:
            print("저장 완료.\n프로그램을 종료합니다.")
            return
    elif n==4:
        n = input("수정할 항목의 이름 입력 : ")
        n2 = input("수정할 컬럼 입력 : ")
        n3 = input("수정할 내용 입력 : ")
        cursor.execute(f'update table1 set {n2}="{n3}" where name="{n}"')
        print("수정 완료.")
        print("------------------------------")
        home()
    elif n==5:
        time.sleep(1)
        print("저장 완료.\n프로그램을 종료합니다.")
        pass
    else:
        home()

home()

conn.commit()
conn.close()