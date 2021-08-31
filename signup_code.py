#!C:/Users/user/AppData/Local/Programs/Python/Python38/python
print("Content-type:text/html\r\n\r\n")
import cgi, os, cgitb, random, config
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
fileitem = form['image']
name=form.getvalue('name')
email=form.getvalue('email')
address=form.getvalue('address')
phone=form.getvalue('phone')
password=form.getvalue('password')
if fileitem.filename:
    # strip leading path from file name to avoid directory traversal attacks
    fn = os.path.basename(fileitem.filename)
    mfn=str(random.random())+fn
    fpath = 'user_image/' + mfn
    f = open('C:/xampp/htdocs/foodblog/blog/' + fpath, 'wb', 10000)
    # Read the file in chunks
    for chunk in fbuffer(fileitem.file):
        f.write(chunk)
    f.close()
    cursor=config.db.cursor()
    try:
        cursor = config.db.cursor()
        src="SELECT email FROM user WHERE email='{}'".format(email)
        cursor.execute(src)
        rec=cursor.fetchall()
        if rec:
            print('''<h1> You are already registered <h1>''')
        else:
            sql="INSERT INTO user (name,email,address,phone,password,image) VALUES ('{}','{}','{}','{}','{}','{}')".format(name,email,address,phone,password,fpath)
            cursor.execute(sql)
            config.db.commit()
            config.db.close()
            print('''<script>
        window.location="TESTSIGN.py?msg=File Uploaded successfully"
        </script>''')
    except Exception as e:
        print(e)

else:
    print('''''')