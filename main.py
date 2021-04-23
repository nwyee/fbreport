# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from report import Report
from getpass import getpass


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'**** Welcome From Report App, {name} **** \n')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Entry Log In name / email : ")
    name = input()
    print_hi(name)
    password = getpass(prompt="Password: ")
    print("Target Account : ")
    target = input()
    print("How many Times (integer) ? : ")
    times = int(input())
    me = Report(name, password, target, times)
    me.start()

