#!C:/Users/user/AppData/Local/Programs/Python/Python38/python
print('''Content-type:text/html\r\n\r\n''')
import cgi, cgitb, config
cgitb.enable()
frm=cgi.FieldStorage()
id=frm.getvalue('id')
try:
    cursor=config.db.cursor()
    delete="DELETE FROM blog WHERE id={}".format(id)
    cursor.execute(delete)
    config.db.commit()
    config.db.close()
    print('''<script>
    window.location="profile.py?msg=Data delete successfully"
    </script>''')
except Exception as e:
    print('''<script>
    window.location="profile.py?msg={}"
    </script>'''.format(e))

