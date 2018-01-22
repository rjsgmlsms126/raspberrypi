import sqlite3
name = '이세돌'
cell_phone = '010-3333-3333'
email = 'lee@gmail.com'
with sqlite3.connect("contact.db") as con:
    sql = """
    INSERT INTO CONTACTS(NAME, CELL_PHONE, EMAIL)
    VALUES(?, ?, ?)
    """;
    try:
        con.execute(sql, (name, cell_phone, email))
        print('데이터 삽입 저장 완료')
    except Exception as err:
        print('데이터베이스 에러 : %s' % err)
    else:
        con.commit()