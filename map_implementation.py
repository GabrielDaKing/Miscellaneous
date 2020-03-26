map_impl = {}

def set(key, value, time):

	key_time = 10000*key+time

	map_impl[str(key_time)] = value

def get(key,time):

	keys = list(map_impl.keys()).sort()

	smaller_keys = keys.bisect()



def main():
