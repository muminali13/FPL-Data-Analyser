import pandas as pd

from django.shortcuts import render
from scripts.gameweek import get_recent_gameweek_id


def liveTracker(request):

    df = pd.read_csv('scripts/data/2023-24/fixtures.csv')
    df_team = pd.read_csv('scripts/data/2023-24/teams.csv')

    m = df_team.set_index('id')['name'].to_dict()
    v = df[['team_h', 'team_a']]
    df[v.columns] = v.replace(m)

    gameweek = get_recent_gameweek_id()

    thisWeek = []
    nextWeek = []

    for i, fixture in df.iterrows():
        if fixture.event == gameweek:
            thisWeek.append(fixture)
        elif fixture.event == gameweek+1:
            nextWeek.append(fixture)

    context = {
        "current_fixtures":thisWeek,
        "next_fixtures":nextWeek
    }

    return render(request, "liveTracker/liveTracker.html", context)