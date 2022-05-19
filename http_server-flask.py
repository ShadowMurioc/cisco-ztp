from flask import Flask, send_from_directory

HOSTNAME_NUM = 100

ZTP_Floder = "ZTP_File/"
ZTP_Filename = "ztp.py"
ZTP_Template = "ztp.py.template"

app = Flask(__name__)


def create_py():
    with open(ZTP_Template) as file:
        ztp_py_temp = file.readlines()
    ztp_py_temp.insert(1, f"HOSTNAME_NUM={str(HOSTNAME_NUM)}\n")
    with open(ZTP_Floder+ZTP_Filename, "w") as newfile:
        newfile.writelines(ztp_py_temp)
    print("ZTP File Already Generated")


@app.get("/ztp.py")
def index():
    global HOSTNAME_NUM
    create_py()
    HOSTNAME_NUM += 1
    return send_from_directory(directory=ZTP_Floder,
                               path=ZTP_Filename,
                               as_attachment=False)


if __name__ == '__main__':
    app.run(host='151.1.11.101', port=80)