def assignCashPrizes(runners):
    ''' 1st place gets $100
        2nd place gets $50
        3rd place gets $33

        Each title is worth $20 only if they have the title "Pass"
        the "Pass" title is not worth any money
    '''


def assignTitles(runners):
    ''' Assigns titles for meeting certain requirements
        "Golden" == Time is the fastest among contestants
        "Pass" == Time is less than minute
        "On the dot" == Time is exactly on a second like 54.00

        Runners who've received a title last time may not receive it again
    '''


def main():
    runners = {
        1 : ["Bruce", 27.24, ["Pass"]],
        2 : ["Hugo", 32.00, ["Pass"]],
        3 : ["Tony", 44.00, []],
        4 : ["Jay", 57.73, []],
        5 : ["Donovan", 75.75, []],
    }
