def assignCashPrizes(runners):
    ''' 1st place gets $100
        2nd place gets $50
        3rd place gets $33

        Each title is worth $20 only if they have the title "Pass"
        the "Pass" title is not worth any money
    '''
    cashPrizes = {}
    names = ["Bruce", "Hugo", "Tony", "Jay", "Donovan"]

    # assign cash for titles
    for i in range(1,6):
        runnerTitles = runners[i][2]
        name = names[i - 1]
        if ("Pass" in runnerTitles and len(runnerTitles) > 1):
            cashPrizes[name] = (len(runnerTitles) - 1) * 20

    # assign cash for rank
    for i in range(1, 4):
        name = names[i - 1]
        cashPrizes[name] += 100 / i

    # print results
    for name, cash in cashPrizes.items():
        print(name + " won $" + "{:.2f}".format(cash))
    
def assignTitles(runners):
    ''' Assigns titles for meeting certain requirements
        "Golden" == Time is the fastest among contestants
        "Pass" == Time is less than minute
        "On the dot" == Time is exactly on a second like 54.00

        Runners who've received a title last time may not receive it again
    '''

    runners[1][2].append("Golden Leg")
    
    for num, runnerData in runners.items():
        name, time = runnerData[0:2]

        # "Pass" title
        title = "Pass"
        if (time < 60 and title not in runnerData[2]):
            runnerData[2].append(title)

        # "On the dot" title
        title = "On the dot"
        if (int(time) == time):
            runnerData[2].append(title)


def main():
    runners = {
        1 : ["Bruce", 27.24, ["Pass"]],
        2 : ["Hugo", 32.00, ["Pass"]],
        3 : ["Tony", 44.00, []],
        4 : ["Jay", 57.73, []],
        5 : ["Donovan", 75.75, []],
    }

    assignTitles(runners)
    assignCashPrizes(runners)
