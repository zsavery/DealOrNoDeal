import random
class deal_or_no(object):
    #cases_int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    #values = [.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
    #random.shuffle(values)
    def __init__(self, g_case, name):
        self.g_case = g_case
        self.name = name
        self.cases = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
                                   12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
        self.values = [.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000,
                               10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]
        random.shuffle(self.values)
        return
        
    def banker(self):
        size = len(self.cases)
        total = 0 
        for i in self.cases:
            total+=i
        offer = total/size * .65
        print("It is time for the banker's offer.\n\n", self.name, "the banker has offered: $", offer)
        response = input(" do you wish to accept [Yes] or [No].\n->".format(offer))
        if response == "Yes":
            print(self.name, "you now have", offer)
            return True
        else:
            return False
        
    def print_cases(self):
        size = len(self.cases)
        half_size = int(size/2)
        i = 0
        while i < size:
            if(i == half_size):
                print()
            if(i < half_size):
                print("[", self.cases[i], "]", end=" ")
            else:
                print("[", self.cases[i], "]", end=" ")
            i+=1
        print()
        return

    def select_open_case(self):
        def open_case(case_selection):
            index = 0
            size = len(self.cases)
            if case_selection in self.cases:
                while index < size:
                    if self.cases[index] == case_selection:
                        print(
                            "Inside case number [", self.cases[index], "]", end=" ")
                        print(" is [", self.values[index], "].", end="\n")
                        del self.values[index], self.cases[index]
                        break
                    index += 1
            return

        sel = int(input("Enter case selection: "))
        open_case(sel)
        return
