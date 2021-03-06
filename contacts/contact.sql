DROP TABLE IF EXISTS CONTACTS;
CREATE TABLE CONTACTS(
    _ID        INTEGER PRIMARY KEY AUTOINCREMENT ,
    NAME       TEXT(15),
    CELL_PHONE TEXT(15),
    EMAIL      TEXT(50),
    ADDRESS    TEXT(256),
    BIRTHDAY   TEXT(15)
);


INSERT INTO CONTACTS VALUES(0, '홍길동', '010-1111-2222', 'hong@naver.com',
'서울시 강남구', '2012-12-12');
INSERT INTO CONTACTS(NAME, CELL_PHONE, EMAIL) VALUES('고길동', '010-1111-
3333', 'gogd@naver.com');
INSERT INTO CONTACTS(NAME, CELL_PHONE, EMAIL) VALUES('마이콜', '010-1111-
4444', 'micol@gmail.com');
INSERT INTO CONTACTS(NAME, CELL_PHONE, EMAIL) VALUES('도우너', '010-1111-
5555', 'donut@naver.com');
INSERT INTO CONTACTS(NAME, CELL_PHONE, EMAIL) VALUES('가길동X', '010-1111-
2222', 'hong@naver.com');
INSERT INTO CONTACTS(NAME, CELL_PHONE, EMAIL) VALUES('나길동', '010-1111-
3333', 'gogd@naver.com');
INSERT INTO CONTACTS(NAME, CELL_PHONE, EMAIL) VALUES('다이콜', '010-1111-
4444', 'micol@gmail.com');
INSERT INTO CONTACTS(NAME, CELL_PHONE, EMAIL) VALUES('라우너', '010-1111-
5555', 'donut@naver.com');
INSERT INTO CONTACTS(NAME, CELL_PHONE, EMAIL) VALUES('마길동X', '010-1111-
2222', 'hong@naver.com');
INSERT INTO CONTACTS(NAME, CELL_PHONE, EMAIL) VALUES('바길동', '010-1111-
3333', 'gogd@naver.com');
INSERT INTO CONTACTS(NAME, CELL_PHONE, EMAIL) VALUES('사이콜', '010-1111-
4444', 'micol@gmail.com');
INSERT INTO CONTACTS(NAME, CELL_PHONE, EMAIL) VALUES('아우너', '010-1111-
5555', 'donut@naver.com');
INSERT INTO CONTACTS(NAME, CELL_PHONE, EMAIL) VALUES('자길동X', '010-1111-
2222', 'hong@naver.com');
INSERT INTO CONTACTS(NAME, CELL_PHONE, EMAIL) VALUES('차길동', '010-1111-
3333', 'gogd@naver.com');
INSERT INTO CONTACTS(NAME, CELL_PHONE, EMAIL) VALUES('카이콜', '010-1111-
4444', 'micol@gmail.com');
INSERT INTO CONTACTS(NAME, CELL_PHONE, EMAIL) VALUES('타우너', '010-1111-
5555', 'donut@naver.com');
INSERT INTO CONTACTS(NAME, CELL_PHONE, EMAIL) VALUES('파길동X', '010-1111-
2222', 'hong@naver.com');
