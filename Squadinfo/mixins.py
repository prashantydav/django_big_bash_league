from bs4 import BeautifulSoup as bs
import requests
from players.models import match , Squad

def squad_name():
    sq = []
    lin = []
    url = 'https://www.espncricinfo.com/series/big-bash-league-2021-22-1269637/squads'
    req = requests.get(url,headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
            })
    soup = bs(req.content,'html.parser')
    title = soup.find_all('div',class_ = 'squad-row d-flex justify-content-md-between py-2 align-content-center flex-wrap')
    for i in title:
        squad = i.find('a',class_='black-link d-none d-md-inline-block pl-2')
        # lin.append(squad['href'])
        sq.append(squad.text)
        a = squad.text.split(' ')
        st = a[0][0] + a[1][0]
        lin.append(st)
    return sq

def match_results():
    mat = []
    teams = []
    url = 'https://www.espncricinfo.com/series/big-bash-league-2021-22-1269637/match-results'
    req = requests.get(url,headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
            })
    soup = bs(req.content,'html.parser')
    link = soup.find_all('a',class_ = 'match-info-link-FIXTURES')
    for i in link:
        team = []
        
        l = i['href'].split('/')
        code = l[3].split('-')[-1]
        mat.append(code)
        url1 = 'https://www.espncricinfo.com'+i['href']
        req1 = requests.get(url1,headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
            })
        soup1 = bs(req1.content,'html.parser')
        name = soup1.find_all('a',class_='name-link')
        for j in name:
            teams.append(j.text)
    return(mat , teams)


def value_stored():
    match.objects.all().delete()
    Squad.objects.all().delete()
    print('deleted')
    for i in range(len(match_results()[0])):
        l = match_results()
        m = 2*i 
        n = i+1
        match.objects.create(match_id = l[0][i],team1 = l[1][m] , team2 = l[1][n])
        print('object created!!')
    for i in squad_name():
        Squad.objects.create(name = i)
        print('squad created!!')
    
