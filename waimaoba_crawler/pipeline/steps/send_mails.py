import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

from waimaoba_crawler.settings import APPLICATION_PASSWORD, SENDER_EMAIL


# Ben's Email: t104360038@ntut.org.tw


def send_email(contact_person, company_email):
    msg = MIMEMultipart("alternative")
    msg["Subject"] = 'Greetings from AAA Company'
    msg["From"] = SENDER_EMAIL
    msg["To"] = company_email

    # ----------- write the HTML part --------------------
    variable = {'{contact_person}': contact_person}
    with open('dev_template.html', mode='r', encoding='utf-8') as file:
        html = file.read()

    for key in variable.keys():
        html = html.replace(key, variable[key])
    part = MIMEText(html, "html")
    msg.attach(part)

    # ----------- attach the imbeded image--------------------
    fp = open('../images/company_logo.jpeg', 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    # Specify the  ID according to the img src in the HTML part
    img.add_header('Content-ID', '<CompanyLogo>')
    msg.attach(img)

    fp = open('../images/product_dm.JPG', 'rb')
    img = MIMEImage(fp.read())
    fp.close()
    # Specify the  ID according to the img src in the HTML part
    img.add_header('Content-ID', '<ProductDM>')
    msg.attach(img)
    # ---------------------------------------------------------

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(SENDER_EMAIL, APPLICATION_PASSWORD)
        smtp.send_message(msg)


send_email('Steve', 'stevehsieh2797@gmail.com')