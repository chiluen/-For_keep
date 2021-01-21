from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def content_setting(sender, receiver, google_doc_address):


    mail_content = """您好，以下的Google doc想請您填寫關於您認識的實驗室人員的資訊。
    這裡為連結：{}，麻煩請填入聯絡資訊，謝謝！
    """.format(google_doc_address)

    content = MIMEMultipart()  
    content["subject"] = "Speech Lab 通訊錄建立"  
    content["from"] = sender  
    content["to"] = receiver 
    content.attach(MIMEText(mail_content))  #郵件內容 
    return content

def sent(sender, password, content):
    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  
            smtp.starttls()  
            smtp.login("leo545035@gmail.com", Password)  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            print("Complete!")
        except Exception as e:
            print("Error message: ", e)

if __name__ == "__main__":

    Password = "kankhjxohtifudkv" #generate by 應用程式密碼(google)
    sender = "leo545035@gmail.com"
    receiver = ["leo545035@gmail.com", "leo545035@gmail.com"]
    google_doc_address = ["aaa.doc", "bbb.doc"]

    # Start sending
    for i in range(len(receiver)):
        content = content_setting(sender,receiver[i],google_doc_address[i])
        sent(sender, Password, content)
