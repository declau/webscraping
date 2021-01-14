import requests
import smtplib

from bs4 import BeautifulSoup


URL = 'https://www.mercadolivre.com.br/sony-playstation-4-slim-1tb-standard-jet-black/p/MLB10813733?pdp_filters=deal:MLB3608#searchVariation=MLB10813733&position=1&type=product&tracking_id=0853ad62-7d25-4904-8f78-08ef7c80290d'

headers = {
    "User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36'}


def ckeck_price():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(attrs={"ui-pdp-title"}).get_text()

    price = soup.find(attrs={"price-tag-fraction"}).get_text()
    converted_price = float(price[0:5])

    discount_price = soup.find(attrs={"ui-pdp-price__second-line"}).get_text()
    converted_discount_price = float(discount_price[2:7])

    print(converted_price)
    print(converted_discount_price)
    print(title)

    if(converted_discount_price < 3.000):
        send_email()

def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('email', 'password')

    subject = 'Price fell down!'
    hello = 'Hello my friend!'
    body = 'Check the Mercado Livre link https://www.mercadolivre.com.br/sony-playstation-4-slim-1tb-standard-jet-black/p/MLB10813733?pdp_filters=deal:MLB3608#searchVariation=MLB10813733&position=1&type=product&tracking_id=0853ad62-7d25-4904-8f78-08ef7c80290d'

    message = f"Subject: {subject}\n\n{hello}\n\n{body}"
    
    server.sendmail(
        'email.from',
        'email.to',
        message
    )
    print('HEY E-MAIL HAS BEEN SENT!')

    server.quit()

ckeck_price()