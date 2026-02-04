import requests
from bs4 import BeautifulSoup

s=requests.get('https://www.amazon.in/TRIUMPH-Speed-Phantom-Booking-Ex-Showroom/dp/B0F53FKZ12/?_encoding=UTF8&pd_rd_w=r8353&content-id=amzn1.sym.4ba71204-24f1-4af6-bcb4-a2ca17f99630&pf_rd_p=4ba71204-24f1-4af6-bcb4-a2ca17f99630&pf_rd_r=TFE42WVTZA8H9H8Z3BMN&pd_rd_wg=whPnN&pd_rd_r=55b8cb61-c0ce-4007-b033-8203519ee7d8&ref_=pd_hp_d_btf_ls_gwc_pc_en4_')
html=s.text

soup=BeautifulSoup(html, 'html.parser')
for script in soup(["script", "style"]):
    script.extract()
text = soup.get_text(separator=' ')
print(text)