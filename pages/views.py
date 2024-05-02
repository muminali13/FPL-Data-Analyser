from django.shortcuts import render

from django.contrib.auth.decorators import login_required

from scripts.top_managers import get_current_top_team;
from scripts.teams_scraper import get_team_data
from scripts.gameweek import get_recent_gameweek_id


def home(request):

    data = get_current_top_team()
    print(data)

    gk = []
    defs = []
    mids = []
    fwds = []
    bench = []

    for index, player in data.iterrows():
        # print(player)
        if int(player['multiplier']) == 0:
            bench.append(player)
        elif player['element_type'] == 'GK':
            gk.append(player)
        elif player['element_type'] == 'DEF':
            defs.append(player)
        elif player['element_type'] == 'MID':
            mids.append(player)
        elif player['element_type'] == 'FWD':
            fwds.append(player)
            
    
    gameweek = data['gw'][0]
    team = data['team_id'][0]
    context = {'current_gameweek' : gameweek,
               'team_id' : team,
               'team': { 'GK':gk, 'DEF':defs, 'MID':mids, 'FWD':fwds, 'BENCH':bench }
               }
    return render(request, "pages/home.html", context)


@login_required(login_url="login")
def teamViewPage(request):

    # if request.user.is_authenticated():
    team_id = request.user.first_name
    gameweek = get_recent_gameweek_id()

    data = get_team_data(team_id, '23-24', gameweek)

    gk = []
    defs = []
    mids = []
    fwds = []
    bench = []

    for index, player in data.iterrows():
        # print(player)
        if int(player['multiplier']) == 0:
            bench.append(player)
        elif player['element_type'] == 'GK':
            gk.append(player)
        elif player['element_type'] == 'DEF':
            defs.append(player)
        elif player['element_type'] == 'MID':
            mids.append(player)
        elif player['element_type'] == 'FWD':
            fwds.append(player)
            
        context = {'current_gameweek' : gameweek,
               'team_id' : team_id,
               'team': { 'GK':gk, 'DEF':defs, 'MID':mids, 'FWD':fwds, 'BENCH':bench },
               'data': data}
    return render(request, "pages/teamViewPage.html", context)
