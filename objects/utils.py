from requests import get

from objects import cfg


def osu_status():
    res = 0
    
    try:
        if get(f'https://osu.{cfg.env.target}').status_code < 500:
            res = 200
    except:
        res = 0
    return res

def web_status():
    res = 0
    
    try:
        if get(f'https://{cfg.env.target}').status_code != 200:
            res = 0
        else:
            res = 200
    except:
        res = 0
    return res

def scores_status():
    res = 0
    
    try: # cringe yea yea 
        if get(f'https://osu.{cfg.env.target}').status_code < 500:
            res = 200
    except:
        res = 0
    return res

def api_status():
    res = 0
    
    try:
        if get(f'https://api.{cfg.env.target}/get_player_scores').status_code < 500:
            res = 200
    except:
        res = 0
    
    return res

def status():
    return {
        'Website': web_status(),
        'Bancho': osu_status(),
        'Scores': scores_status(),
        'API': api_status()
    }