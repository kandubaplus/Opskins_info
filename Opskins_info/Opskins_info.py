import urllib.request
from bs4 import BeautifulSoup


def get_html(url):
    user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
    headers={'User-Agent':user_agent,}
    request=urllib.request.Request(url,None,headers)
    response = urllib.request.urlopen(request)
    return response.read()


def parse(html,idd,r,e):
    
    soup = BeautifulSoup(html,'html.parser')
    table = soup.find('div',class_="col-lg-12")
    try:
        q = table.prettify()
    except AttributeError:
        r.write(idd)
        print("Not valid id")   
    else:
        e.write(idd)
        print(q)
        
def main():
    f = open('ids.txt','r')
    e = open('good.txt','w')
    r = open('bad.txt','w') 
    ids = f.readline()
    id = []
    while ids:
        id.append(ids)
        ids = f.readline()
    f.close()
    for i in range(len(id)):
        print(id[i])
        parse(get_html(url = "https://opskins.com/?loc=shop_users_page&steamid="+id[i]),id[i],r,e)


main()
