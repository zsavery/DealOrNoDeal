from deal_or_no_deal import deal_or_no

print("I am your host Howie Mandel. Welcome to Deal or No Deal!")
guest_name = input("Enter your name: ")
guest_case = int(input("Enter select a case (1 - 26): "))

round_flag = [1, 6, False]
game1 = deal_or_no(guest_case, guest_name)
game1.select_open_case2(guest_case)
def round(flag):
    while flag[2] == False:
        temp = flag[1]
        if flag[0] != 10:
           print("Round", flag[0])
        while temp != 0:
            if flag[0] >= 1 and flag[0] < 10:
                game1.print_cases()
                game1.select_open_case()
                if temp == 1:
                    flag[2] = game1.banker()
            if flag[0] == 10:
                game1.print_cases()
                #offer swap
                #if yes swap
                flag[2] = True
            temp -= 1
        flag[0]+=1
        if flag[1] == 1:
            continue
        else:
            flag[1]= flag[1]-1
        #if flag[2] = True open g_case 
    return
    
round(round_flag)




