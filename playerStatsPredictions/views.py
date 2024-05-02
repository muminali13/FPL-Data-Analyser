import pandas as pd
from django.shortcuts import render

from django.contrib.auth.decorators import login_required

@login_required(login_url="login")
def playerStatsPredictions(request):

    df = pd.read_csv('scripts/data/fpl_player_data.csv')
    
    print(df.info())
    print(df)
    context = {
        "data": df
    }
    return render(request, "playerStatsPredictions/playerStatsPredictions.html", context)

