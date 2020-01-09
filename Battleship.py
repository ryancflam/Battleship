import random
class Battleship:
    def __init__(self):
        self.__shipsize=[4,3,3,2]
        self.__shipcode=["B","C","S","D"]
        self.__board=[[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "],[" "," "," "," "," "," "," "," "," "," "]]
        self.__battleship=4
        self.__cruiser=3
        self.__submarine=3
        self.__destroyer=2
        self.__totalx=12
        self.__turns=0
    def displayboard(self,showships):
        st=""
        st+="\n  0123456789\n ┌----------┐\n"
        for x in range(10):
            st+=f"{x}|"
            for y in range(10):
                if showships==True:
                    st+=f"{self.__board[x][y]}"
                else:
                    if self.__board[x][y]=="M":
                        st+="M"
                    elif self.__board[x][y]=="X":
                        st+="X"
                    else:
                        st+=" "
            st+="|\n"
        st+=" └----------┘"
        return st
    def placeships(self):
        for z in range(len(self.__shipcode)):
            done=False
            while done==False:
                rand1=random.randint(0,9)
                rand2=random.randint(0,9)
                direction=random.randint(0,2)
                piece=0
                problem=False
                while piece<self.__shipsize[z]and problem==False:
                    if self.__board[rand1][rand2]==" ":
                        self.__board[rand1][rand2]=self.__shipcode[z]
                    else:
                        problem=True
                    if direction==0:
                        rand1+=1
                    else:
                        rand2+=1
                    if rand1>9or rand2>9:
                        problem=True
                    else:
                        piece+=1
                    if problem==True:
                        for row in range(10):
                            for column in range(10):
                                if self.__board[row][column]==self.__shipcode[z]:
                                    self.__board[row][column]=" "
                if piece==self.__shipsize[z]and problem==False:
                    done=True
    def taketurn(self,ships):
        try:
            row=int(input("\nEnter row number (0-9): "))
            if row is None:
                return None
            while row<0 or row>9:
                row=int(input("\n[ERROR] Row number must be 0-9 inclusive.\n\nEnter row number (0-9): "))
                if row is None:
                    return None
            col=int(input("\nEnter column number (0-9): "))
            if col is None:
                return None
            while col<0 or col>9:
                col=int(input("\n[ERROR] Column number must be 0-9 inclusive.\n\nEnter column number (0-9): "))
                if col is None:
                    return None
            if self.__board[row][col]=="M"or self.__board[row][col]=="X":
                print("\nYou have wasted a turn.")
                self.__turns+=1
            if self.__board[row][col]==" ":
                self.__turns+=1
                print("\nMiss.")
                self.__board[row][col]="M"
            if self.__board[row][col]=="B":
                print("\nHit.")
                self.__board[row][col]="X"
                self.__battleship-=1
                self.__totalx-=1
                self.__turns+=1
                if self.__battleship==0:
                    print("\nYou have sunk the battleship.")
                    ships-=1
                if self.__totalx==0:
                    print(f"\nGame required {self.__turns} turns.")
            if self.__board[row][col]=="S":
                print("\nHit.")
                self.__board[row][col]="X"
                self.__submarine-=1
                self.__totalx-=1
                self.__turns+=1
                if self.__submarine==0:
                    print("\nYou have sunk the submarine.")
                    ships-=1
                if self.__totalx==0:
                    print(f"\nGame required {self.__turns} turns.")
            if self.__board[row][col]=="C":
                print("\nHit.")
                self.__board[row][col]="X"
                self.__cruiser-=1
                self.__totalx-=1
                self.__turns+=1
                if self.__cruiser==0:
                    print("\nYou have sunk the cruiser.")
                    ships-=1
                if self.__totalx==0:
                    print(f"\nGame required {self.__turns} turns.")
            if self.__board[row][col]=="D":
                print("\nHit.")
                self.__board[row][col]="X"
                self.__destroyer-=1
                self.__totalx-=1
                self.__turns+=1
                if self.__destroyer==0:
                    print("\nYou have sunk the destroyer.")
                    ships-=1
                if self.__totalx==0:
                    print(f"\nGame required {self.__turns} turns.")
            return ships
        except ValueError:
            print("\nYou have left Battleship.")
            return None
        except KeyboardInterrupt:
            return None
    def turn(self):
        ships=4
        while ships>0:
            print(self.displayboard(False))
            ships=self.taketurn(ships)
            if ships is None:
                return
    def game(self):
        print("\nWelcome to Battleship. Enter any value other than the digits 0-9 to quit.")
        self.placeships()
        self.turn()
Battleship().game()
