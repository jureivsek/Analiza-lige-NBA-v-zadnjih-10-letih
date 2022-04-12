from statistics import mean
import pandas as pd
import numpy as np
import json
import matplotlib.pyplot as plt

#podatki deset sezon prebrane iz excel tabele
podatki1 = pd.read_excel('11-12.xlsx', names=["N","TEAM","WIN%","PTS","FGM","FGA","FG%","3PM","3PA","3P%","REB","AST","+/-"])
podatki2 = pd.read_excel('12-13.xlsx', names=["N","TEAM","WIN%","PTS","FGM","FGA","FG%","3PM","3PA","3P%","REB","AST","+/-"])
podatki3 = pd.read_excel('13-14.xlsx', names=["N","TEAM","WIN%","PTS","FGM","FGA","FG%","3PM","3PA","3P%","REB","AST","+/-"])
podatki4 = pd.read_excel('14-15.xlsx', names=["N","TEAM","WIN%","PTS","FGM","FGA","FG%","3PM","3PA","3P%","REB","AST","+/-"])
podatki5 = pd.read_excel('15-16.xlsx', names=["N","TEAM","WIN%","PTS","FGM","FGA","FG%","3PM","3PA","3P%","REB","AST","+/-"])
podatki6 = pd.read_excel('16-17.xlsx', names=["N","TEAM","WIN%","PTS","FGM","FGA","FG%","3PM","3PA","3P%","REB","AST","+/-"])
podatki7 = pd.read_excel('17-18.xlsx', names=["N","TEAM","WIN%","PTS","FGM","FGA","FG%","3PM","3PA","3P%","REB","AST","+/-"])
podatki8 = pd.read_excel('18-19.xlsx', names=["N","TEAM","WIN%","PTS","FGM","FGA","FG%","3PM","3PA","3P%","REB","AST","+/-"])
podatki9 = pd.read_excel('19-20.xlsx', names=["N","TEAM","WIN%","PTS","FGM","FGA","FG%","3PM","3PA","3P%","REB","AST","+/-"])
podatki10 = pd.read_excel('20-21.xlsx', names=["N","TEAM","WIN%","PTS","FGM","FGA","FG%","3PM","3PA","3P%","REB","AST","+/-"])
seznampodatkov = [podatki1,podatki2,podatki3,podatki4,podatki5,podatki6,podatki7,podatki8,podatki9,podatki10]


# po ekipah
ekipe = ["ATL", "BKN", "BOS", "CHA", "CHI", "CLE", "DAL", "DEN", "DET", "GSW", "HOU", "IND", "LAC", "LAL", "MEM", "MIA", "MIL", "MIN", "NOP", "NYK", "OKC", "ORL", "PHI", "PHX", "POR", "SAC", "SAS", "TOR", "UTA", "WAS"]

def e(ime):         #ime ekipe, da dobimo do katerega mesta v stolpcu dostopamo
    for i, e in enumerate(ekipe):
        if ime == e:
            return i
            break

#po letih
leta = ["11/12","12/13","13/14","14/15","15/16","16/17","17/18","18/19","19/20","20/21"]

nov = []
# def graf mal za testerat
dol = list(range(len(podatki3['FGM'])))
podatki = podatki3['FGM']
for i in podatki:
    nov.append(i)

y = nov
x = dol
print(x)
print(y)

plt.plot(x, y)
plt.title("test test ena dva")
plt.show()



def teams_trait(sez, trait, sezpod, xlabel, ylabel, title, me = False):
    "za parametra vzame seznam ekip, ponavadi z neko lastnostjo(naprimer zmagovalce po letih) in primerja v eni izmed lastnosti"
    x = leta
    y = []
    števec = 0
    for i in sez:
        y.append(sezpod[števec][trait][e(i)] * 100)
        števec += 1
    plt.plot(x, y, 'o', color = 'black')

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    if me:
        y_mean = [np.mean(y)]*len(x)
        plt.plot(x, y_mean, label = "Mean")
    plt.show()

def teams_trait1(sez, trait, sezpod, xlabel, ylabel, title, me = False):
    "za parametra vzame seznam ekip, ponavadi z neko lastnostjo(naprimer zmagovalce po letih) in primerja v eni izmed lastnosti"
    x = leta
    y = []
    števec = 0
    for i in sez:
        y.append(sezpod[števec][trait][e(i)])
        števec += 1
    plt.plot(x, y, 'o', color = 'black')

    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    if me:
        y_mean = [np.mean(y)]*len(x)
        plt.plot(x, y_mean, label = "Mean")
    plt.show()


sez_zmag = ["DAL", "OKC","SAS","GSW","GSW","GSW","GSW","GSW","LAL","PHX"]

gsw = ["GSW","GSW","GSW","GSW","GSW","GSW","GSW","GSW","GSW","GSW"]

teams_trait(sez_zmag, 'WIN%', seznampodatkov,"sezona","odstotek zmag zmagovalca[%]","odstotek zmag zmagovalcev lige NBA v zadnjih 10 letih", True)

teams_trait1(gsw, '3P%', seznampodatkov,"sezona","uspešnost meta za 3 točke[%]","uspešnost meta za 3 točke moštva Golden State ", True)


def best_win():
    "poišče ekipo z najboljšim povprečjem zmag"
    naj = ''
    win = 0
    for i in ekipe:
        mean = 0
        for j in seznampodatkov:
            mean += j['WIN%'][e(i)]
        mean = mean/10
        if mean > win:
            win = mean
            naj = i
    x = e(naj)
    y = podatki10['TEAM'][x]
    return(y, round(win * 100, 1))

def worst_win():
    "poišče ekipo z najslabšim povprečjem zmag"
    naj = ''
    win = 100
    for i in ekipe:
        mean = 0
        for j in seznampodatkov:
            mean += j['WIN%'][e(i)]
        mean = mean/10
        if mean < win:
            win = mean
            naj = i
    x = e(naj)
    y = podatki10['TEAM'][x]
    return(y, round(win * 100, 1))

t, p = best_win()           #best mean win percentage, mean percentage of 1o years
print("ekipa z najbolšjim povprečjem zmag v zadnjih desetih letih je " + str(t) + ' z ' + str(p))
t, p = worst_win()          #worst mean win percentage, mean percentage of 1o years
print("ekipa z najslabšim povprečjem zmag v zadnjih desetih letih je " + str(t) + ' z ' + str(p) + '%')

def worst_best_comparison(e1, e2):
    "nariši graf najboljše in jaslabše ekipe(gledano s strani win%) in primerjaj z meti za 3 točke"
    win1 = []
    win2 = []
    tr1 = []
    tr2 = []
    x = leta
    for i in seznampodatkov:
        win1.append(i['WIN%'][e(e1)]*100)
        win2.append(i['WIN%'][e(e2)]*100)
        tr1.append(i['3P%'][e(e1)])
        tr2.append(i['3P%'][e(e2)])

    plt.plot(x, win1,label = 'San Antonio Spurs win percentage', color = 'black')
    plt.plot(x, win2,label = 'Minnesota Timberwolves win percentage', color = 'grey')
    plt.plot(x, tr1,label = 'San Antonio Spurs three point percentage', color = 'orange')
    plt.plot(x, tr2,label = 'Minnesota Timberwolves three point percentage', color = 'green')
    plt.xlabel('sezona')
    plt.ylabel('[%]')
    plt.legend()
    plt.show()
    
#Število zadetih trojk v sezoni 2011/12 in sezoni 2020/21.
y = [x for x in podatki1['3PM']]
plt.plot(ekipe, y, color="blue", label="2011/12")
y = [x for x in podatki10['3PM']]
plt.plot(ekipe,y, color="green", label="2020/21")
plt.ylabel("3PM")
plt.legend()
plt.title("Število zadetih trojk v sezoni 2011/12 in sezoni 2020/21.")
plt.show()
plt.close()

#Število vrženih metov na tekmo v sezoni 2011/12 in sezoni 2020/21.
y = [x for x in podatki1['FGA']]
plt.plot(ekipe, y, color="blue", label="2011/12")
y = [x for x in podatki10['FGA']]
plt.plot(ekipe,y, color="green", label="2020/21")
plt.ylabel("FGA")
plt.legend()
plt.title("Število vrženih metov na tekmo v sezoni 2011/12 in sezoni 2020/21.")
plt.show()
plt.close()
    
    
worst_best_comparison('SAS', 'MIN')



    

