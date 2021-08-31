#!C:/Users/INDRANI/AppData/Local/Programs/Python/Python38/python
print("Content-type:text/html\r\n\r\n")
import cgi, os, cgitb, random, config, check_cookie
from datetime import date
cgitb.enable()
#print(random.random())
try: # Windows needs stdio set for binary mode.
    import msvcrt
    msvcrt.setmode (0, os.O_BINARY) # stdin  = 0
    msvcrt.setmode (1, os.O_BINARY) # stdout = 1
except ImportError:
    pass

form = cgi.FieldStorage()
# Generator to buffer file chunks
def fbuffer(f, chunk_size=10000):
    while True:
        chunk = f.read(chunk_size)
        if not chunk: break
        yield chunk
# A nested FieldStorage instance holds the file
fileitem = form['image']
title=form.getvalue('title')
blog=form.getvalue('blog')
id=form.getvalue('id')
date = date.today()
uid = check_cookie.user_data[0]
# Test if the file was uploaded
if fileitem.filename:
    # strip leading path from file name to avoid directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    mfn=str(random.random())+fn
    fpath = 'blog_image/' + mfn
    f = open('C:/xampp/htdocs/foodblog/Blog/Blog/Blog' + fpath, 'wb', 10000)
    # Read the file in chunks
    for chunk in fbuffer(fileitem.file):
        f.write(chunk)
    f.close()
    cursor2=config.db.cursor()
    sql="UPDATE blogs SET title='{}',blog='{}',date='{}',imagepath='{}' WHERE id='{}'".format(title,blog,date,fpath,id)
    if cursor2.execute(sql):
        config.db.commit()
        config.db.close()
        print('''<script>
        window.location="Home.py?msg=File Uploaded successfully"
        </script>''')
    else:
        print('''<script>
                window.location="Home.py?msg=File not Uploaded successfully"
        </script>''')
else:
    print('''''')
    #message = 'The file "' + os.path.basename(fileitem.filename) + '" was not uploaded successfully'

