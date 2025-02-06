
def new(t, dict):
    if t not in dict:
        dict[t] = [0, 0, 0.00, 0, 0]
    return dict

def point(t, p, pt1, pt2, dict):
    dict[t][0] += 1
    dict[t][1] += p
    dict[t][3] += pt1
    dict[t][4] += pt2
    dict[t][2] = round(dict[t][3] / dict[t][4], 3)
    return dict

fp = open("torneo.txt", "r", encoding='utf-8')

teams = {}
for row in fp.readlines():
    row = row.strip().split(':')
    row[0] = row[0].split('-')
    team1 = row[0][0].strip()
    team2 = row[0][1].strip()
    row[1] = row[1].split('-')
    pt1 = int(row[1][0])
    pt2 = int(row[1][1])

    teams = new(team1, teams)
    teams = new(team2, teams)

    if pt1>pt2:
        teams = point(team1, 3, pt1, pt2, teams)
        teams = point(team2, 1, pt2, pt1, teams)
    elif pt2>pt1:
        teams = point(team2, 3, pt2, pt1, teams)
        teams = point(team1, 1, pt1, pt2, teams)
    else:
        teams = point(team1, 2, pt1, pt2, teams)
        teams = point(team2, 2, pt2, pt1, teams)
fp.close()

print("%20s %7s %5s  %5s %3s %3s" %('SQUADRA', 'GIOCATE', 'PUNTI', 'Q', 'PF', 'PS'))
print("-------------------------------------------------")
for team in sorted(teams.items(), key = lambda item : item[1][1], reverse=True):
    print("%20s %7d %5d  %4.3f %3d %3d" %(team[0], team[1][0], team[1][1], team[1][2], team[1][3], team[1][4]))
