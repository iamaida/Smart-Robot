import os.path

class Environment:

    #Properties
    file_name: str =" "
    world: list = []
    #mode= " "

    #Methods
    def __init__(self, file_name):
        self.file_name = file_name

    #Check if a file exist
    def __file_exist(self) -> bool:
        return os.path.isfile(self.file_name)

    #Read a 2D-array (10x10) of a file and save into property world as a list
    def __read(self,) -> None:

        if self.__file_exist():
            with open(self.file_name, "r") as file:
                self.world = file.readlines()
                print(f"¡lectura exitosa!")
        else:
            print(f"¡el archivo {self.file_name}  no existe!")

    #Return the value of property world
    def getWorld(self) -> list:
        return self.world

    #Conver 2D-Array rows of type str to type list
    def __convertToList(self) -> None:
        i = 0
        for row in self.world:
            self.world[i] = list(row)
            i += 1

    #Remove all the ocurrences of a specific item in a list
    def __removeListItem(self, aList: list ,item: str) -> list:

        ocurrences = aList.count(item)
        for i in range(ocurrences):
            aList.remove(item)

        return aList

    #Remove all the ocurrences of the item ' ' in the rows of the 2D-array
    def __removeBlanksFromRows(self) -> None:
        i = 0
        for row in self.world:
           self.world[i] = self.__removeListItem(row, ' ')
           i += 1

    #Remove all the ocurrences of the item '\n' in each row of the 2D-array
    def __removeEnterFromRows(self) -> None:
        i = 0
        for row in self.world:
            self.world[i] = self.__removeListItem(row, '\n')
            i+= 1

    #Convert all items of  list of str type to int type
    def __convertItemsToInt(self, aList: list) -> list:
        i=0
        for item  in aList:
            aList[i]= int(item)
            i += 1
        return  aList

    #Convert all items of  each row of the 2D-array in integers
    def __convertStrListToIntegerList(self,) -> None:
        i = 0
        for row in self.world:
            self.world[i] = self.__convertItemsToInt(row)
            i += 1

    def upload(self) -> None:
        self.__read()
        #print(self.getWorld())
        self.__convertToList()
        #print(self.getWorld())
        self.__removeBlanksFromRows()
        #print(self.getWorld())
        self.__removeEnterFromRows()
        #print(self.getWorld())
        self.__convertStrListToIntegerList()
        #print(self.getWorld())