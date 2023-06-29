import valo_api.endpoints
import json
import pandas as pd


def get_mmr_history_by_name():
    return valo_api.endpoints.get_mmr_history_by_name("v1", "na", "Devendro", "3876")


def get_match_details():
    return valo_api.endpoints.get_match_details("v2", 'c564397c-6f24-4c69-a03d-9bfc6cfd0e06')


def get_match_history():
    return valo_api.endpoints.get_match_history_by_name_v3("na", "oxyjin02", "LOFT", size="1", map="", game_mode="Competitive")


def get_json(obj):
    return json.loads(json.dumps(obj, default=lambda o: getattr(o, '__dict__', str(o))))


if __name__ == '__main__':

    match_history = get_match_history()
    match_history_dict = get_json(match_history)
    """
    with open("prac.json", "w") as outfile:
        json.dump(match_history_dict, outfile, indent=4)
    """
    print(match_history_dict[0]["metadata"])
    df = pd.read_json('prac.json')
    df1 = pd.DataFrame(data=match_history_dict[0]["metadata"], index=[0])
    print(df1)

    """
    It looks like there is 3 distinct types of functions needed at the moment,
    the get_json which reads in the dict and formats it.
    
    The functions to format the data(in dict/json) into DataFrame
    
    The functions that make endpoint calls easier
    """

    """
    the "rounds" key in json is a list, i have to loop through list, and for each index of list,
    i have to get all the kill events per round
    
    need a counter for round, 
    
    later i can just add a column to every row for map, match id, etc.
    """