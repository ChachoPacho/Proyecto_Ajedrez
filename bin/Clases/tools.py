from moves import Movements

for i in range(8):
    for y in range(8):
        move = Movements([i,y])

        print(move.piece)
        for x in move.moves_list:
            print(x)
