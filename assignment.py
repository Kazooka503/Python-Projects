import sqlite3

fileList = ('information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

txt = (fileList[1])
txt2 = (fileList[4])


conn = sqlite3.connect('test2.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    file_name TEXT \
    )")
    conn.commit()
conn.close()

conn = sqlite3.connect('test2.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_files(file_name) VALUES (?)", \
                [txt])
    cur.execute("INSERT INTO tbl_files(file_name) VALUES (?)", \
                [txt2])
    conn.commit()
conn.close()

print(txt + ", " + txt2)
