import smtplib
from urllib.request import urlopen
from bs4 import BeautifulSoup

def flipkart():
        global url
        html = urlopen(url)
        soup = BeautifulSoup(html.read())
        a=soup.find("div" , {"class":"_30jeq3 _16Jk6d"})# get the price tag from the url through inspect
        b=a.get_text()    #--- to get the amount of item in tag format
        b=b[1:]
        num='0123456789'
        temp=''
        for i in b:
            if i=='.':
                break
            if i in num:
                temp+=i
        checker=eval(temp)   
        return(checker)

def amazon():
    global url
    html = urlopen(url)
    soup=BeautifulSoup(html.read())
    a=soup.find('span',{'class':'a-size-medium a-color-price priceBlockBuyingPriceString'})
    a=a.get_text()
    num='0123456789'
    temp=''
    for i in a:
        if i=='.':
            break
        if i in num:
            temp+=i
    checker=eval(temp)   
    return(checker)

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()  
    server.login('username','abhi1861@')  #-- here you have to enter the password and username of sender email
    subject = "Price of your item has fallen down below Rs. "+str(amt)
    body = " the price of the item you wanted nas fallen below , please check it on "+url
    msg = f"Subject: {subject} \n\n {body} "
    server.sendmail(
    'abheeshtavemuri23@gmail.com', #-- this is the email id of the reciever 
    msg
    )
    print("HEY USER, EMAIL HAS BEEN SENT SUCCESSFULLY.")
    server.quit()

def price(finamt , curramt ):
    while finamt < curramt :
        if token == 1 :
            curramt = amazon()
        elif token == 2:
            curramt = flipkart()    
    if finamt > curramt:
        send_mail()
        
token=0    
checker = 99999
url = input('enter the url which you want to get notify for ')
amt=int(input('enter the amount below which you want to be notified '))
if ('www.amazon.in' in url) or ('www.amazon.com' in url) :
    price(amt , amazon())
    token = 1
elif ('www.flipkart.com' in url) or ('www.flipkart.in' in url ):
    price(amt , flipkart())
    token = 2