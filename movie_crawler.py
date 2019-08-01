import requests
import telegram
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler


bot = telegram.Bot(token = '747175876:AAEGIH6RciBRcO4xe24Gd_Ly0hjuTPF-XN8')
url = 'http://www.cgv.co.kr//common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0013&date=20190804'

month = url[-4:-2]
day = url[-2:]

def job_funtion():
    html = requests.get(url)
    soup = BeautifulSoup(html.text, 'html.parser')
    imax = soup.select_one('span.imax')
    if(imax):
        imax = imax.find_parent('div', class_ = 'col-times')
        title = imax.select_one('div.info-movie > a > strong').text.strip()
        #bot.sendMessage(chat_id = 961188212, text = month +'월' + day + '일 영화 ' + title + '의 IMAX 예매가 열렸습니다.')
        bot.sendMessage(chat_id = 961188212, text = '[알림톡] ' + month +'월 ' + day + '일 | 영화 ' + title + '의 IMAX 예매가 열렸습니다.')
        sched.pause()
    #else:
    #    bot.sendMessage(chat_id = 961188212, text = month +'월' + day + '일 IMAX 예매가 아직 열리지 않았습니다.')

sched = BlockingScheduler()
sched.add_job(job_funtion, 'interval', seconds = 5)
sched.start()
