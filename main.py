from deal_or_no_deal import deal_or_no

print("I am your host Howie Mandel. Welcome to Deal or No Deal!")
guest_name = input("Enter your name: ")
guest_case = int(input("Enter select a case (1 - 26): "))

round_flag = [1, 6]
game1 = deal_or_no(guest_name, guest_name)
game1.print_cases()

game1.select_open_case()


def round(flag):
    Next = flag[1] -1
    while flag[1] != 1:
        if flag[0] == 1:
            game1.print_cases()
        elif flag[0] == 2:
            game1.print_cases()
        elif flag[0] == 3:
            game1.print_cases()
        elif flag[0] == 4:
            game1.print_cases()
        elif flag[0] == 5:
            game1.print_cases()
        elif flag[0] >= 6 and flag[0] <= 8:
            game1.print_cases()
        elif flag[0] == 9:
            game1.print_cases()
        flag[1]-=1
    flag[0]+=1
    flag[1] = Next
    return
    
    



