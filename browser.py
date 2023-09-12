import sys
import requests
import unicodedata
def fetch_html(url):
    try:
        response = requests.get(url)
	
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print("Erro ao buscar a página:", e)
        sys.exit(1)


def parse_html(html):
   
    html2=html.replace("\n","")
    html2=html2.replace("\r","")
    html2=html[3:]
    html2=html2.replace("<\0b\0r\0>\0","\r\n")
    html2=html2.replace("<\0/\0b\0r\0>\0","\r\n")
    html2=html2.replace("<\0p>\0","\r\n")
    html2=html2.replace("<\0/\0p>\0","\r\n")
    #print(html2)
    tags=html2.split("<")
    tt=""
    for a in tags:
         tagss=a.split(">")
         if len(tagss)>1:
             tt=tt+tagss[1]+" "
 
    print(tt)

def main():
    print("\x1bc\x1b[40;37m")
    if len(sys.argv) != 2:
        print("Uso: python browser_console.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    html = fetch_html(url)
    parsed_html = parse_html(html)
    

main()




 
