from components import variables
choice = ["y", "n"]

def newgame(status):

    choice = input("Do you want to play again? y/n: ")

    if choice == "n":
        print("====== see ya! =======")
        exit()
    elif choice == "y":
        variables.Hulk = 0
        variables.IronMan = 0
        variables.CaptainAmerica = 0
        variables.AntMan = 0
        variables.DocStrange = 0
        variables.quiz = False
