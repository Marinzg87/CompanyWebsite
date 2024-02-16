import smtplib


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    user_name = "m.bogusz.zg@gmail.com"
    password = "wxphabpbyfbnhnrf"
    receiver = "m.bogusz.zg@gmail.com"

    with smtplib.SMTP_SSL(host, port) as server:
        server.login(user_name, password)
        server.sendmail(user_name, receiver, message)
