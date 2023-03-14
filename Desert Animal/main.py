# 9608_w17_qp_41
from time import sleep
import random, os

animal = 'A'
food = 'F'
sand = '.'

class Animal:

    def __init__(self) -> None:
        self.__across = random.randint(0, 19)
        self.__down = random.randint(0, 19)
        self.__score = 0

    def setAcross(self, value) -> None:
        self.__across = value

    def getAcross(self) -> int:
        return self.__across
    
    def setDown(self, value) -> None:
        self.__down = value

    def getDown(self) -> int:
        return self.__down
    
    def getScore(self) -> int:
        return self.__score
    
    def IncrementScore(self) -> None:
        self.__score += 1
    
    def GenerateChangeInCoordinate(self, coordinate) -> int:
        if coordinate == 0:
            change = random.randint(0, 1)
        elif coordinate == 19:
            change = random.randint(-1, 0)
        else:
            change = random.randint(-1, 1)

        return change
    
    def collisionDetection(self, across, down, entity):
        """Entity should be either 'Food' or 'Animal'"""
        if entity == desert.getGrid(across, down):
            return True
        return False
        
    def Move(self) -> None:
        desert.setGrid(self.getAcross(), self.getDown(), sand)

        newacross = self.__across + self.GenerateChangeInCoordinate(self.getAcross())
        newdown = self.__down + self.GenerateChangeInCoordinate(self.getDown())
 
        if not self.collisionDetection(newacross, newdown, animal):
            self.__across = newacross
            self.__down = newdown

            if desert.getGrid(self.getAcross(), self.getDown()) == food:
                self.EatFood()

            desert.setGrid(self.getAcross(), self.getDown(), animal)

    def EatFood(self): 
        self.IncrementScore()
        desert.GenerateFood()
        desert.GenerateAnimal()
    
class Desert:

    def __init__(self) -> None:
        self.__grid = [[sand for across in range(20)] for down in range(20)]
        self.__AnimalList = []
        self.__StepCounter = 0
        self.__NumberOfAnimals = 0

        for i in range(5):
            self.GenerateAnimal()

        self.GenerateFood()
        # for i in range(5):
            # self.GenerateFood()

    def GenerateAnimal(self) -> None:
        if self.getNumberOfAnimals() < 20:
            entity = Animal()
            self.setGrid(entity.getAcross(), entity.getDown(), animal)
            self.__AnimalList.append(entity)
            self.__NumberOfAnimals += 1

    def getNumberOfAnimals(self) -> int:
        return self.__NumberOfAnimals
    
    def setGrid(self, across, down, value) -> None:
        self.__grid[down][across] = value

    def getGrid(self, across, down) -> str:
        return self.__grid[down][across]

    def IncrementStepCounter(self) -> None:
        self.__StepCounter += 1

    def GenerateFood(self) -> None:
        across = random.randint(0, 19)
        down = random.randint(0, 19)
        self.__grid[down][across] = food

    def DisplayGrid(self) -> None:
        os.system('cls')
        for down in range(20):
            for across in range(20):
                print(self.__grid[down][across], end='')
            print()

    def start(self) -> None:
        for tick in range(50):
            for i in range(self.getNumberOfAnimals()):
                self.__AnimalList[i].Move()
            sleep(1)
            self.DisplayGrid()
        for count in range(self.getNumberOfAnimals()):
            print(f"Animal No. = {count} || Score = {self.__AnimalList[count].getScore()}")

desert = Desert()
desert.start()