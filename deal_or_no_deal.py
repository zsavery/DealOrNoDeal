class deal_or_no(object):
    cases_int = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    values = [.01, 1, 5, 10, 25, 50, 75, 100, 200, 300, 400, 500, 750, 1000, 5000, 10000, 25000, 50000, 75000, 100000, 200000, 300000, 400000, 500000, 750000, 1000000]

    def __init__(self, g_case, name):
        self.g_case = g_case
        self.name = name
        return
        

    def print_cases(self):
        size = len(deal_or_no.cases_int)
        half_size = int(size/2)
        i = 0
        while i < size:
            if(i == half_size):
                print()
            if(i < half_size):
                print("[",deal_or_no.cases_int[i], "]", end=" ")
            else:
                print("[", deal_or_no.cases_int[i], "]", end=" ")
            i+=1
        print()
        return

    


    def select_open_case(self):
        def open_case(case_selection):
            index = 0
            size = len(deal_or_no.cases_int)
            if case_selection in deal_or_no.cases_int:
                while index < size:
                    if deal_or_no.cases_int[index] == case_selection:
                        print(
                            "Inside case number [", deal_or_no.cases_int[index], "]", end=" ")
                        print(" is [", deal_or_no.values[index], "].", end="\n")
                        del deal_or_no.values[index], deal_or_no.cases_int[index]
                        break
                    index += 1
            return

        sel = int(input("Enter case selection: "))
        open_case(sel)
        print()
        return
