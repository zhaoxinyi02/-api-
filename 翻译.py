import random
import requests
import hashlib
import pyperclip


url = "https://fanyi-api.baidu.com/api/trans/vip/translate"
appid = ""  #这个双引号里替换成你的appid
password = ""  #这个双引号里替换成你的密钥
ran = str(random.randint(1000000000,9999999999))

def get_txt():
    txt = pyperclip.paste()
    return txt
def get_sign(txt):
    sign = appid + txt + ran + password
    signMD5 = hashlib.md5(sign.encode('utf-8')).hexdigest()
    return signMD5

def get_result(signMD5,txt):
    r = requests.get(url+"?q="+txt+"&from=en&to=zh&appid="+appid+"&salt="+ran+"&sign="+signMD5)
    r = eval(r.text)
    r = r["trans_result"][0]
    print(r["dst"])

def main():
    txt = get_txt()
    while True:
        txt_2 = get_txt()
        if txt_2 == txt:
            continue
        else:
            txt = txt_2
            signMD5 = get_sign(txt)
            get_result(signMD5, txt)


if __name__ == "__main__":
    main()
