import random
lap_num = 0
tires_good = True
final_lap = 30
position = random.randint(1, 30)
racer = input("Enter your name or vehicle number: ")
print("Lap: {}".format(lap_num))
print("On your mark\nReady\nSet\nGO!")

while lap_num < final_lap:
    lap_num += 1
    position = random.randint(1, 30)

    def tire_condition(position):
        tire = random.randint(1, 5)
        if tire == 1 or tire == 2:
            return round(position/2)
        elif tire == 3:
            return position
        else:
            pit_stop = random.randint(1, 8)
            position += pit_stop
            if position >= 30:
                position = 30
                return position
        return position

    if position == 1 or position == 21:
        print("Racer " + racer +
              " has taken {0}st on lap {1}.".format(position, lap_num))
    elif position == 2 or position == 22:
        print("Racer " + racer +
              " has taken {0}nd on lap {1}.".format(position, lap_num))
    elif position == 3 or position == 23:
        print("Racer " + racer +
              " has taken {0}rd on lap {1}.".format(position, lap_num))
    else:
        print("Racer " + racer +
              " has taken {0}th on lap {1}.".format(position, lap_num))

    position = tire_condition(position)

    if lap_num == final_lap:
        if position == 1 or position == 21:
            print("Final lap! Racer " + racer +
                  " has taken {0}st.".format(position))
        elif position == 2 or position == 22:
            print("Final lap! Racer " + racer +
                  " has taken {0}nd.".format(position))
        elif position == 3 or position == 23:
            print("Final lap! Racer " + racer +
                  " has taken {0}rd.".format(position))
        else:
            print("Final lap! Racer " + racer +
                  " has taken {0}th place.".format(position))
