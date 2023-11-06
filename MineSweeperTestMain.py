import MineSweeperLibrary as MineSweeperBackEnd

print("main")

def main():
    print("main")
    dude = MineSweeperBackEnd.MineSweeperBoard()
    #test = dude.board_Array[4][4]
    #print(test)

    MineSweeperBackEnd.MineSweeperBoard.debug_board_console_print(dude)

    print(MineSweeperBackEnd.MineSweeperBoard.Player_Reveal_Guess(dude, 1, 5))

    MineSweeperBackEnd.MineSweeperBoard.debug_board_console_print(dude)



#have this at the bottom of the page as thsi runs main 
if __name__ == "__main__":
    main()