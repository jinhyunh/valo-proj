import valo_api.endpoints
import json


def get_mmr_history_by_name():
    return valo_api.endpoints.get_mmr_history_by_name("v1", "na", "Devendro", "3876")


def get_match_details():
    return valo_api.endpoints.get_match_details("v2", 'c564397c-6f24-4c69-a03d-9bfc6cfd0e06')


def get_match_history():
    return valo_api.endpoints.get_match_history_by_name_v3("na", "Devendro", "3876", game_mode="Competitive")


def get_json(obj):
    return json.loads(json.dumps(obj, default=lambda o: getattr(o, '__dict__', str(o))))


if __name__ == '__main__':
    match_history = get_match_history()
    match_history_dict = get_json(match_history)
    with open("prac.json", "w") as outfile:
        json.dump(match_history_dict, outfile, indent=4)

