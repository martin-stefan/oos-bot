import requests
from bs4 import BeautifulSoup
import smtplib

url = ''

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'}


def check_price():
  page = requests.get(url, headers=headers)

  soup = BeautifulSoup(page.content, 'html.parser')

  title = soup.find(id="productTitle").get_text()

  price = soup.find(id="priceblock_ourprice").get_text()

  converted_price = float(price[0:5])

  if (converted_price < 1.700):
    send_mail()


def send_mail():
  server = smtplib.SMTP('stmp.gmail.com', 587)
  server.ehlo()
  server.starttls()
  server.ehlo()

  server.login('user', 'password')
  subject = 'Price fell down'
  body = "Checl amazon link"

  msg = f"subject {subject}\n\n{body}"
  server.sendmail (
    'from', 
    'to',
    msg
  )
  server.quit()

check_price()