import hello
import number_game
import farts

def master():
    print("""
    #####################################################################
    ###                          Master.py                            ###
    #####################################################################
    #                                                                   #
    # Hello, and welcome to the Master.py!                              #
    #                                                                   #
    # With this simple file you will be able to navigate to any of the  #
    # other Python projects.                                            #
    #                                                                   #
    # Simply type in the name of the project you would like to visit    #
    # and press Enter.                                                  #
    #                                                                   #
    #####################################################################
    #                                                                   #
    # Select from the following files:                                  #
    #     - hello.py                                                    #
    #     - number_game.py                                              #
    #     - farts.py                                                    #
    #     - list.py                                                     #
    #                                                                   #
    #####################################################################
    """)

    selection = input("Enter the name of a Python script you'd like to run: ")

    if selection == "hello.py":
        print("""
    #####################################################################
    ###                             hello.py                          ###
    #####################################################################
    #                                                                   #
    # hello.py is loading ...                                           #
    #                                                                   #
    #####################################################################
        """)
        hello.hello_world()
    elif selection == "number_game.py":
        print("""
    #####################################################################
    ###                         number_game.py                        ###
    #####################################################################
    #                                                                   #
    # number_game.py is loading ...                                     #
    #                                                                   #
    #####################################################################
        """)
        number_game.game()
    elif selection == "farts.py":
        print("""
    #####################################################################
    ###                             farts.py                          ###
    #####################################################################
    #                                                                   #
    # farts.py is loading ...                                           #
    #                                                                   #
    #####################################################################
        """)
        print("farts.py")
    else:
        print("ERROR! Cannot find: ", selection)
        selection = None
        master()

#For some reason, when I call the scrip to launch initially, it breaks everything.
#More investigation is required.

#master()

#isStart = input("Type start to begin: ")

#if isStart.lower() == "start":
    #start()
