import base64



def icon2py():
    'icon存入py'
    open_icon = open("icon.ico","rb")
    b64str = base64.b64encode(open_icon.read())
    open_icon.close()
    write_data = "img = %s" % b64str
    f = open(".\icon.py","w+")
    f.write(write_data)
    f.close()

if __name__ == '__main__':
    icon2py()