import valo_api.endpoints


def demo_func():
    return valo_api.endpoints.get_mmr_history_by_name("v1", "na", "Devendro", "3876")


def poop_sock():
    return valo_api.endpoints.get_match_details("v2", 'c564397c-6f24-4c69-a03d-9bfc6cfd0e06')

if __name__ == '__main__':
    print(poop_sock())
    print(type(poop_sock()))
