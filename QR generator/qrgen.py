import pyqrcode

from pyqrcode import QRCode

s = "https://google.com"
url = pyqrcode.create(s)

url.svg("google.svg",scale=8)