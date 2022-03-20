def main():

    x = "X"
    o = "O"
    spc = " "
    vDivider = " | "
    hDivider = "----------"

    matrix = [[spc for _ in range(0, 3)] for _ in range(0,3)]

    player1 = "Player 1"
    player2 = "Player 2"

    def printMat():
        print(f" 1   2   3\n")
        print(f" {matrix[0][0]}{vDivider}{matrix[0][1]}{vDivider}{matrix[0][2]}   1")
        print(hDivider)
        print(f" {matrix[1][0]}{vDivider}{matrix[1][1]}{vDivider}{matrix[1][2]}   2")
        print(hDivider)
        print(f" {matrix[2][0]}{vDivider}{matrix[2][1]}{vDivider}{matrix[2][2]}   3")
        print("\n")

    def changePos(player):
        move = input(f"{player} enter your move: ").split(" ")
        if player == player1:
            matrix[int(move[0]) - 1][int(move[1]) - 1] = x

        elif player == player2:
            matrix[int(move[0]) - 1][int(move[1]) - 1] = o

    def checkwin(player):
        if matrix[0][0] == matrix[0][1] and matrix[0][0] == matrix[0][2] and matrix[0][0] != spc and matrix[0][1] != spc and matrix[0][2] != spc:
            print(f"\n{player} wins!")
            return False

        elif matrix[1][0] == matrix[1][1] and matrix[1][0] == matrix[1][2] and matrix[1][0] != spc and matrix[1][1] != spc and matrix[1][2] != spc:
            print(f"\n{player} wins!")
            return False

        elif matrix[2][0] == matrix[2][1] and matrix[2][0] == matrix[2][2] and matrix[2][0] != spc and matrix[2][1] != spc and matrix[2][2] != spc:
            print(f"\n{player} wins!")
            return False

        elif matrix[0][0] == matrix[1][0] and matrix[0][0] == matrix[2][0] and matrix[0][0] != spc and matrix[1][0] != spc and matrix[2][0] != spc:
            print(f"\n{player} wins!")
            return False

        elif matrix[0][1] == matrix[1][1] and matrix[0][1] == matrix[2][1] and matrix[0][1] != spc and matrix[1][1] != spc and matrix[2][1] != spc:
            print(f"\n{player} wins!")
            return False

        elif matrix[0][2] == matrix[1][2] and matrix[0][2] == matrix[2][2] and matrix[0][2] != spc and matrix[1][2] != spc and matrix[2][2] != spc:
            print(f"\n{player} wins!")
            return False

        elif matrix[0][0] == matrix[1][1] and matrix[0][0] == matrix[2][2] and matrix[0][0] != spc and matrix[1][1] != spc and matrix[2][2] != spc:
            print(f"\n{player} wins!")
            return False

        elif matrix[2][0] == matrix[1][1] and matrix[2][0] == matrix[0][2] and matrix[2][0] != spc and matrix[1][1] != spc and matrix[0][2] != spc:
            print(f"\n{player} wins!")
            return False

        else:
            return True


    def gameStart():

        print("Welcome to the Game!")
        print("Enter your move by position seperated by a space\n")
        turn = 1

        running = True

        printMat()

        try:
            while running:
                if turn == 1:
                    changePos(player1)
                    printMat()
                    turn = 2
                    running = checkwin(player1)

                elif turn == 2:
                    changePos(player2)
                    printMat()
                    turn = 1
                    running = checkwin(player2)

        except KeyboardInterrupt:
            print("\nStopped by User")

    gameStart()

if __name__ == "__main__":
    main()
