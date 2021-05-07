import json


class Chess:
    with open('config/cache.json', 'r') as outfile:
        data = json.load(outfile)

    board = data['board']
    color = data['color']
    turn = data['turn']
    check = data['check']
