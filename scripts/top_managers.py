import requests , json, csv
import pandas as pd

from .gameweek import get_recent_gameweek_id

def get_top_managers():

    # Overall FPL league ID
    overallLeageID = 314

    # adds the top 10 team ID's to this array
    teamID = 0

    url = "https://fantasy.premierleague.com/api/leagues-classic/"+str(overallLeageID)+"/standings/"

    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)
    managerParsed = parsed['standings']['results']

    # open 3 files for writing
    manager_data = open('scripts/data/2023-24/managers/top_manager.csv', 'w', newline='', encoding="utf-8")
    gw_data = open('scripts/data/2023-24/managers/top_manager_gwInfo.csv', 'w', newline='', encoding="utf-8")
    gw_picks = open('scripts/data/2023-24/managers/top_manager_gwPicks.csv', 'w', newline='', encoding="utf-8")

    # create the 3 csv writer objects
    csvwriter1 = csv.writer(manager_data)
    csvwriter2 = csv.writer(gw_data)
    csvwriter3 = csv.writer(gw_picks)

    # get csv of top  manager information and write to top_manager.csv
    manager = managerParsed[0]
       
    header = ['rank','entry','player_name','entry_name','total']
    csvwriter1.writerow(header)
        
    csvwriter1.writerow([manager['rank'],manager['entry'],manager['player_name'],
                    manager['entry_name'],manager['total']])

    teamID = manager['entry']

    # call the api and update both top_managers_gwInfo.csv and top_managers_gwPicks.csv
    x = get_recent_gameweek_id()

    url = "https://fantasy.premierleague.com/api/entry/"+str(teamID)+"/event/"+str(x)+"/picks/"
    response = requests.get(url)
    data = response.text
    parsed = json.loads(data)

    # write data to top_managers_gwInfo.csv
    header = ['team_id','gw','points','bench','gw_rank','transfers','hits','total_points',
        'overall_ank','team_value','chip']

    csvwriter2.writerow(header)

    try:
        csvwriter2.writerow([teamID,x, parsed['entry_history']['points'], parsed['entry_history']['points_on_bench'],
                        parsed['entry_history']['rank'], parsed['entry_history']['event_transfers'],
                        parsed['entry_history']['event_transfers_cost'], parsed['entry_history']['total_points'],
                        parsed['entry_history']['overall_rank'], int(parsed['entry_history']['value'])/10, parsed['active_chip']])
    except:
        pass

    # write data to top_managers_gwPicks.csv
    for i in range(len(parsed['picks'])):
        if i == 0:
            header = ['team_id','gw','id','position','multiplier']
            csvwriter3.writerow(header)
        csvwriter3.writerow([teamID, x, parsed['picks'][i]['element'], parsed['picks'][i]['position'], parsed['picks'][i]['multiplier']])

    manager_data.close()
    gw_data.close()
    gw_picks.close()

    # do some formatting on top_managers_gwPicks by adding the name of the player picked from player_idlist.csv
    df = pd.read_csv('scripts/data/2023-24/managers/top_manager_gwPicks.csv')

    df1 = pd.read_csv('scripts/data/2023-24/player_idlist.csv') 
    df2 = pd.read_csv('scripts/data/2023-24/cleaned_players.csv') 
    
    df1['full_name'] = df1[['first_name', 'second_name']].apply(lambda x: ' '.join(x), axis=1)
    df2['full_name'] = df2[['first_name', 'second_name']].apply(lambda x: ' '.join(x), axis=1)
    df1.drop(['first_name', 'second_name'], axis=1, inplace=True)
    df2.drop(['first_name', 'second_name'], axis=1, inplace=True)

    merged = df1.merge(df2, on=['full_name'])
    merged = merged.merge(df, on=['id'])

    merged.rename({'id': 'player_id'}, axis=1, inplace=True)
    merged = merged.sort_values(by=['position'])

    merged.to_csv('scripts/data/2023-24/managers/top_manager_gwPicks.csv',index=False)


def get_current_top_team():
    # get_top_managers()
    
    df = pd.read_csv('scripts/data/2023-24/managers/top_manager_gwPicks.csv')
    return df


