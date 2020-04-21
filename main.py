from deal_or_no_deal import deal_or_no
import deal_or_no_deal as DND

print("I am your host Howie Mandel. Welcome to Deal or No Deal!")
guest_name = input("Enter your name: ")
guest_case = int(input("Enter select a case (1 - 26): "))

round_flag = [1, 6, False]
game1 = deal_or_no(guest_name, guest_name)

def round(flag):
    while flag[2] == False:
        if flag[1] != 1:
            Next = flag[1] -1
        else:
            Next = flag[1]
        while flag[1] != 1:
            if flag[0] >= 1 and flag[0] <= 9:
                game1.print_cases()
                game1.select_open_case()
                flag[2] = game1.banker()
            elif flag[0] == 10:
                game1.print_cases()
                #offer swap
                #if refuse open g_case, else open last case
                flag[2] = True


            flag[1]-=1
        flag[0]+=1
        flag[1] = Next
    return
    
round(round_flag)




