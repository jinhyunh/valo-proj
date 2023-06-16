import valo_api.endpoints


def demo_func():
    return valo_api.endpoints.get_mmr_history_by_name("v1", "na", "Devendro", "3876")


def poop_sock():
    return valo_api.endpoints.get_match_details("v2", 'c564397c-6f24-4c69-a03d-9bfc6cfd0e06')


"""
1. Play around with the Valorant API, get familiar with the parameters and endpoint calls
2. Figure out how to get match details, write up a function that does this cleanly and saves matches to a json
    a. One solution: Get a list of X matches, pass that into the get_match_details endpoint
    b. Better solution...?
3. Once I have a json, find a good way to convert json to data format (Dataframe, etc)
    a. Structure 1: each row is for kill/death instance, columns has which gun, which skin, was it kill or death, 
        location, etc... Basically whatever stat I want tied to the kill/death
4. Data analysis, for next week going to do gun skin analysis
    a. Bigger project, heatmap of where I get kills/death on each map, make it customizable: sort by whether it be kills
        vs deaths, sort by agent, sort by map, sort by avg enemy rank, etc...
"""


if __name__ == '__main__':
    print(poop_sock())
    print(type(poop_sock()))
