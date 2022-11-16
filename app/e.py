import smtplib

ms = smtplib.SMTP("smtp.gmail.com", 587)

ms.starttls()

ms.login("fastapifastapi@gmail.com","sroaeqihedcmvczs")

mgs = "testing stuffs"

ms.sendmail("fastapifastapi@gmail.com","lawalafeez820@gmail.com", mgs)

ms.quit()