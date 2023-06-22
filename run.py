from vb2py.vbfunctions import *
from vb2py.vbdebug import *

class Program:
    """Hauted House Program
    By: Lucas Bates
    Version: 2.2.1
    FUNCTIONS
    """


    def Red(self):
        Console.ForegroundColor = ConsoleColor.Red
        return fn_return_value

    def DarkRed(self):
        Console.ForegroundColor = ConsoleColor.DarkRed
        return fn_return_value

    def DarkGray(self):
        Console.ForegroundColor = ConsoleColor.DarkGray
        return fn_return_value

    def White(self):
        Console.ForegroundColor = ConsoleColor.White
        return fn_return_value

    def Green(self):
        Console.ForegroundColor = ConsoleColor.Green
        return fn_return_value

    def Gray(self):
        Console.ForegroundColor = ConsoleColor.Gray
        return fn_return_value

    def Yellow(self):
        Console.ForegroundColor = ConsoleColor.Yellow
        return fn_return_value

    def Gold(self):
        Console.ForegroundColor = ConsoleColor.DarkYellow
        return fn_return_value

    def Blue(self):
        Console.ForegroundColor = ConsoleColor.Blue
        return fn_return_value

    def Purple(self):
        Console.ForegroundColor = ConsoleColor.DarkMagenta
        return fn_return_value

    def Pink(self):
        Console.ForegroundColor = ConsoleColor.Magenta
        return fn_return_value

    def Cyan(self):
        Console.ForegroundColor = ConsoleColor.Cyan
        return fn_return_value

    def Blank(self):
        Console.Writeline()
        return fn_return_value

    def Main(self):
        roomName = vbObjectInitialize((Integer(18),), String)

        SroomName = vbObjectInitialize((Integer(18),), String)

        roomDesc = vbObjectInitialize((Integer(18),), String)

        roomLocked = vbObjectInitialize((Integer(18),), Integer)

        roomLit = vbObjectInitialize((Integer(18),), Integer)

        itemName = vbObjectInitialize((Integer(15),), String)

        itemDesc = vbObjectInitialize((Integer(15),), String)

        itemLocation = vbObjectInitialize((Integer(15),), Integer)

        itemValue = vbObjectInitialize((Integer(15),), Integer)

        pronoun = vbObjectInitialize((Integer(1),), String)

        diffProb = vbObjectInitialize((Integer(6),), Integer)

        playerRoomNum = Integer(0)

        playerInput = Integer()

        playerName = String()

        playerAge = Integer()

        playerGender = Integer()

        playerScore = Integer()

        playerLives = Integer(5)

        programEnd = Integer()

        enterCorrect = Integer()

        itemPickup = Integer()

        difficulty = Integer()

        playerOK = Integer()

        inventory = - Integer(1)
        #STEP 1: SET UP ARRAYS
        roomName[Integer(0)] = String(value='at the Front Door')
        roomName[Integer(1)] = String(value='in the Underground Cabin')
        roomName[Integer(2)] = String(value='in the Underground Tunnel')
        roomName[Integer(3)] = String(value='in the North Garden')
        roomName[Integer(4)] = String(value='in the Ground Floor Landing')
        roomName[Integer(5)] = String(value='in the Dining Room')
        roomName[Integer(6)] = String(value='in the Dungeon')
        roomName[Integer(7)] = String(value='in the Lounge')
        roomName[Integer(8)] = String(value='in the Clothing Room')
        roomName[Integer(9)] = String(value='in the First Floor Landing')
        roomName[Integer(10)] = String(value='in the South Garden')
        roomName[Integer(11)] = String(value='on the Second Floor Balcony')
        roomName[Integer(12)] = String(value='in the Second Floor Landing')
        roomName[Integer(13)] = String(value='in the Bedroom')
        roomName[Integer(14)] = String(value='in the Bathroom ')
        roomName[Integer(15)] = String(value='in the Treasury')
        roomName[Integer(16)] = String(value='on the Third Floor Balcony')
        roomName[Integer(17)] = String(value='in the Attic')
        roomName[Integer(18)] = String(value='on the Roof')
        SroomName[Integer(0)] = String(value='Front Door')
        SroomName[Integer(1)] = String(value='Underground Cabin')
        SroomName[Integer(2)] = String(value='Underground Tunnel')
        SroomName[Integer(3)] = String(value='North Garden')
        SroomName[Integer(4)] = String(value='Ground Floor Landing')
        SroomName[Integer(5)] = String(value='Dining Room')
        SroomName[Integer(6)] = String(value='Dungeon')
        SroomName[Integer(7)] = String(value='Lounge')
        SroomName[Integer(8)] = String(value='Clothing Room')
        SroomName[Integer(9)] = String(value='First Floor Landing')
        SroomName[Integer(10)] = String(value='South Garden')
        SroomName[Integer(11)] = String(value='Second Floor Balcony')
        SroomName[Integer(12)] = String(value='Second Floor Landing')
        SroomName[Integer(13)] = String(value='Bedroom')
        SroomName[Integer(14)] = String(value='Bathroom ')
        SroomName[Integer(15)] = String(value='Treasury')
        SroomName[Integer(16)] = String(value='Third Floor Balcony')
        SroomName[Integer(17)] = String(value='Attic')
        SroomName[Integer(18)] = String(value='Roof')
        roomDesc[Integer(0)] = String(value='a heavy wooden door, slightly ajar.')
        roomDesc[Integer(1)] = String(value='a dark, dirty underground room.')
        roomDesc[Integer(2)] = String(value='a dark, dirty underground tunnel.')
        roomDesc[Integer(3)] = String(value='a small garden with a gravestone.')
        roomDesc[Integer(4)] = String(value='a small room with a coat hanger.')
        roomDesc[Integer(5)] = String(value='a small room with a wooden table that has rotten food atop it.')
        roomDesc[Integer(6)] = String(value='a dark, murky room. You can make out a dead skeleton.')
        roomDesc[Integer(7)] = String(value='a room with 2 armchairs and a log fire that went out long ago.')
        roomDesc[Integer(8)] = String(value='a small storage room with clothes hung on the walls. You see a poster: A RUSTY dungeon, A STEEL bedroom, A BRASS clothing room, A SILVER chest')
        roomDesc[Integer(9)] = String(value='a small, dark room. a cat scurries away as you enter.')
        roomDesc[Integer(10)] = String(value='a garden with many trees and many gravestones.')
        roomDesc[Integer(11)] = String(value='a small balcony, looking out the front side of the house.')
        roomDesc[Integer(12)] = String(value='a cobweb-filled room with a broken chandelier.')
        roomDesc[Integer(13)] = String(value='The master bedroom. a rotting woman is in the four-poster bed.')
        roomDesc[Integer(14)] = String(value='a small bathroom with a dripping tap.')
        roomDesc[Integer(15)] = String(value='a small room with a small, locked chest.')
        roomDesc[Integer(16)] = String(value='a small balcony, looking out the south side of the house.')
        roomDesc[Integer(17)] = String(value='an old attic with a skeleton lying on a small table. a spider drops form the ceiling.')
        roomDesc[Integer(18)] = String(value='a flat area on the roof of the house.')
        roomLocked[Integer(0)] = Integer(0)
        roomLocked[Integer(1)] = Integer(0)
        roomLocked[Integer(2)] = Integer(0)
        roomLocked[Integer(3)] = Integer(0)
        roomLocked[Integer(4)] = Integer(0)
        roomLocked[Integer(5)] = Integer(0)
        roomLocked[Integer(6)] = Integer(1)
        roomLocked[Integer(7)] = Integer(0)
        roomLocked[Integer(8)] = Integer(1)
        roomLocked[Integer(9)] = Integer(0)
        roomLocked[Integer(10)] = Integer(0)
        roomLocked[Integer(11)] = Integer(0)
        roomLocked[Integer(12)] = Integer(0)
        roomLocked[Integer(13)] = Integer(1)
        roomLocked[Integer(14)] = Integer(0)
        roomLocked[Integer(15)] = Integer(0)
        roomLocked[Integer(16)] = Integer(0)
        roomLocked[Integer(17)] = Integer(0)
        roomLocked[Integer(18)] = Integer(0)
        roomLit[Integer(0)] = Integer(1)
        roomLit[Integer(1)] = Integer(0)
        roomLit[Integer(2)] = Integer(0)
        roomLit[Integer(3)] = Integer(1)
        roomLit[Integer(4)] = Integer(1)
        roomLit[Integer(5)] = Integer(1)
        roomLit[Integer(6)] = Integer(0)
        roomLit[Integer(7)] = Integer(1)
        roomLit[Integer(8)] = Integer(1)
        roomLit[Integer(9)] = Integer(0)
        roomLit[Integer(10)] = Integer(1)
        roomLit[Integer(11)] = Integer(1)
        roomLit[Integer(12)] = Integer(1)
        roomLit[Integer(13)] = Integer(1)
        roomLit[Integer(14)] = Integer(1)
        roomLit[Integer(15)] = Integer(1)
        roomLit[Integer(16)] = Integer(1)
        roomLit[Integer(17)] = Integer(0)
        roomLit[Integer(18)] = Integer(1)
        itemName[Integer(0)] = String(value='Candle')
        itemName[Integer(1)] = String(value='Bone')
        itemName[Integer(2)] = String(value='Chest Key')
        itemName[Integer(3)] = String(value='Dungeon Key')
        itemName[Integer(4)] = String(value='Closet Key')
        itemName[Integer(5)] = String(value='Bedroom Key')
        itemName[Integer(6)] = String(value='Torch')
        itemName[Integer(7)] = String(value='Ruby')
        itemName[Integer(8)] = String(value='Amulet')
        itemName[Integer(9)] = String(value='Artifact')
        itemName[Integer(10)] = String(value='Red Herring')
        itemName[Integer(11)] = String(value='Stone')
        itemName[Integer(12)] = String(value='Glass Shard')
        itemName[Integer(13)] = String(value='Soap Bar')
        itemName[Integer(14)] = String(value='Tile')
        itemName[Integer(15)] = String(value='Painting')
        itemDesc[Integer(0)] = String(value='a wax candle, glowing dimly')
        itemDesc[Integer(1)] = String(value='an old bone')
        itemDesc[Integer(2)] = String(value='a small silver key')
        itemDesc[Integer(3)] = String(value='a large rusty key')
        itemDesc[Integer(4)] = String(value='a brass key with \'Sixty Four\'s Root and Two\'s Cube\' enscribed on it')
        itemDesc[Integer(5)] = String(value='a steel key')
        itemDesc[Integer(6)] = String(value='a bright electric torch')
        itemDesc[Integer(7)] = String(value='a large blood-red ruby')
        itemDesc[Integer(8)] = String(value='a gold amulet')
        itemDesc[Integer(9)] = String(value='a soul-green jade, shaped into a skull')
        itemDesc[Integer(10)] = String(value='a red herring')
        itemDesc[Integer(11)] = String(value='a shiny blue stone')
        itemDesc[Integer(12)] = String(value='a shard of glass')
        itemDesc[Integer(13)] = String(value='a pink bar of soap')
        itemDesc[Integer(14)] = String(value='a loose rooftile')
        itemDesc[Integer(15)] = String(value='a painting of an old man')
        itemLocation[Integer(0)] = Integer(5)
        itemLocation[Integer(1)] = Integer(6)
        itemLocation[Integer(2)] = Integer(13)
        itemLocation[Integer(3)] = Integer(17)
        itemLocation[Integer(4)] = Integer(18)
        itemLocation[Integer(5)] = Integer(6)
        itemLocation[Integer(6)] = Integer(9)
        itemLocation[Integer(7)] = Integer(15)
        itemLocation[Integer(8)] = Integer(15)
        itemLocation[Integer(9)] = Integer(15)
        itemLocation[Integer(10)] = Integer(5)
        itemLocation[Integer(11)] = Integer(1)
        itemLocation[Integer(12)] = Integer(12)
        itemLocation[Integer(13)] = Integer(14)
        itemLocation[Integer(14)] = Integer(18)
        itemLocation[Integer(15)] = Integer(4)
        itemValue[Integer(0)] = Integer(1)
        itemValue[Integer(1)] = Integer(0)
        itemValue[Integer(2)] = Integer(20)
        itemValue[Integer(3)] = Integer(0)
        itemValue[Integer(4)] = Integer(5)
        itemValue[Integer(5)] = Integer(0)
        itemValue[Integer(6)] = Integer(3)
        itemValue[Integer(7)] = Integer(25000)
        itemValue[Integer(8)] = Integer(15000)
        itemValue[Integer(9)] = Integer(75000)
        itemValue[Integer(10)] = Integer(0)
        itemValue[Integer(11)] = Integer(5)
        itemValue[Integer(12)] = Integer(0)
        itemValue[Integer(13)] = Integer(0)
        itemValue[Integer(14)] = Integer(7)
        itemValue[Integer(15)] = Integer(100)
        pronoun[Integer(0)] = String(value='He')
        pronoun[Integer(1)] = String(value='She')
        diffProb[Integer(0)] = Integer(0)
        diffProb[Integer(1)] = Integer(10)
        diffProb[Integer(2)] = Integer(21)
        diffProb[Integer(3)] = Integer(33)
        diffProb[Integer(4)] = Integer(46)
        diffProb[Integer(5)] = Integer(60)
        diffProb[Integer(6)] = Integer(90)
        #STEP 2: SET UP VARIABLES
        #ENTER NAME, AGE, GENDER, DIFFICULTY
        self.DarkGray()
        while enterCorrect == Integer(0) and not programEnd == Integer(1):
            #name
            Console.WriteLine(String(value='What is your Name?'))
            playerName = Console.ReadLine
            #age
            Console.WriteLine(String(value='What is your Age (in years)?'))
            playerAge = Val(Console.ReadLine)
            #gender
            Console.WriteLine(String(value='What is your Gender? 0:Male 1:Female'))
            playerGender = Val(Console.ReadLine)
            #difficulty
            Console.WriteLine(String(value='What difficulty level do you want to play at? 0:Really Easy 1:Easy 2:Medium 3:Hard 4:Very Hard 5:Deathly'))
            difficulty = Val(Console.ReadLine)
            #age check
            if playerAge < Integer(13):
                Console.Clear(self.DarkRed())
                Console.WriteLine(String(value='You are too young to play this game! Please return in ') + Integer(13) - playerAge + String(value=' year(s).'))
                Console.ForegroundColor = ConsoleColor.Gray
                programEnd = Integer(1)
            #full check
            if playerGender >= Integer(0) and playerGender <= Integer(3) and playerGender <= Integer(1) and not playerName == String(value='') and difficulty >= Integer(0) and difficulty <= Integer(6):
                enterCorrect = Integer(1)
            if programEnd == Integer(0):
                Console.Clear()
            if enterCorrect == Integer(1) and programEnd == Integer(0):
                Console.WriteLine(String(value='Name: ') + playerName)
                Console.WriteLine(String(value='Age: ') + playerAge)
                Console.WriteLine(String(value='Gender: ') + playerGender + String(value=' (0:Male 1:Female)'))
                Console.WriteLine(String(value='Difficulty: ') + difficulty + String(value=' (0:Really Easy 1:Easy 2:Medium 3:Hard 4:Very Hard 5:Deathly)'))
                self.Blank()
                Console.WriteLine(String(value='Are the above details correct? 0:No 1:Yes'))
                enterCorrect = Val(Console.ReadLine())
            if programEnd == Integer(0):
                Console.Clear()
            if difficulty == Integer(6):
                self.DarkRed()
                Console.WriteLine(String(value='Difficulty: ErrO4'))
                Console.ReadKey(True)
                Console.Clear()
        if difficulty >= Integer(4):
            roomDesc[Integer(8)] = String(value='a small storage room with clothes hung on the walls.')
            #Removes clue when difficulty is Very Hard Or Higher
        #INTRO
        if programEnd == Integer(0):
            Console.Clear(self.Blank())
            self.Red()
            Console.WriteLine(String(value=' ██░ ██  ▄▄▄       █    ██  ███▄    █ ▄▄▄█████▓▓█████ ▓█████▄     ██░ ██  ▒█████   █    ██   ██████ ▓█████ '))
            Console.WriteLine(String(value='▓██░ ██▒▒████▄     ██  ▓██▒ ██ ▀█   █ ▓  ██▒ ▓▒▓█   ▀ ▒██▀ ██▌   ▓██░ ██▒▒██▒  ██▒ ██  ▓██▒▒██    ▒ ▓█   ▀ '))
            Console.WriteLine(String(value='▒██▀▀██░▒██  ▀█▄  ▓██  ▒██░▓██  ▀█ ██▒▒ ▓██░ ▒░▒███   ░██   █▌   ▒██▀▀██░▒██░  ██▒▓██  ▒██░░ ▓██▄   ▒███   '))
            Console.WriteLine(String(value='░▓█ ░██ ░██▄▄▄▄██ ▓▓█  ░██░▓██▒  ▐▌██▒░ ▓██▓ ░ ▒▓█  ▄ ░▓█▄   ▌   ░▓█ ░██ ▒██   ██░▓▓█  ░██░  ▒   ██▒▒▓█  ▄ '))
            Console.WriteLine(String(value='░▓█▒░██▓ ▓█   ▓██▒▒▒█████▓ ▒██░   ▓██░  ▒██▒ ░ ░▒████▒░▒████▓    ░▓█▒░██▓░ ████▓▒░▒▒█████▓ ▒██████▒▒░▒████▒'))
            Console.WriteLine(String(value='▒ ░░▒░▒ ▒▒   ▓▒█░░▒▓▒ ▒ ▒ ░ ▒░   ▒ ▒   ▒ ░░   ░░ ▒░ ░ ▒▒▓  ▒     ▒ ░░▒░▒░ ▒░▒░▒░ ░▒▓▒ ▒ ▒ ▒ ▒▓▒ ▒ ░░░ ▒░ ░'))
            Console.WriteLine(String(value=' ▒ ░▒░ ░  ▒   ▒▒ ░░░▒░ ░ ░ ░ ░░   ░ ▒░    ░     ░ ░  ░ ░ ▒  ▒     ▒ ░▒░ ░  ░ ▒ ▒░ ░░▒░ ░ ░ ░ ░▒  ░ ░ ░ ░  ░'))
            Console.WriteLine(String(value=' ░  ░░ ░  ░   ▒    ░░░ ░ ░    ░   ░ ░   ░         ░    ░ ░  ░     ░  ░░ ░░ ░ ░ ▒   ░░░ ░ ░ ░  ░  ░     ░   '))
            Console.WriteLine(String(value=' ░  ░  ░      ░  ░   ░              ░             ░  ░   ░        ░  ░  ░    ░ ░     ░           ░     ░  ░'))
            self.Blank()
            self.Blank()
            self.DarkRed()
            Console.WriteLine(String(value='A haunted house looms in front of you. You walk up slowly to a heavy wooden door, slightly ajar.'))
            Console.WriteLine(String(value='You reach to push it open but it creaks open before you can touch it. You decide to walk inside.'))
            self.Blank()
            self.Blank()
        #GAME LOOP START
        while programEnd == Integer(0):
            #enter room
            self.DarkGray()
            self.Blank()
            if inventory >= Integer(0):
                Console.WriteLine(String(value='----------------------------------------------------------------------------------------------------------------------------------------'))
                Console.WriteLine(String(value='Please enter a room number (0-18). Enter 20 to see or drop your held item. Enter 21 to see a list of all the rooms in the haunted house.'))
            if inventory == - Integer(1):
                Console.WriteLine(String(value='------------------------------------------------------------------------------------------------'))
                Console.WriteLine(String(value='Please enter a room number (0-18). Enter 21 to see a list of all the rooms in the haunted house.'))
            playerInput = Val(Console.ReadLine)
            self.Blank()
            #check if room is 0
            if playerInput == Integer(0):
                self.Green()
                Console.WriteLine(String(value='You are at the front door. Would you like to exit the haunted house? 0:No 1:Yes'))
                #check if player wants to leave
                programEnd = Val(Console.ReadLine)
                if programEnd > Integer(1) or programEnd < Integer(0):
                    programEnd = Integer(0)
                #if player chose to leave, program goes to end
                if programEnd == Integer(0):
                    self.DarkRed()
                    Console.WriteLine(String(value='You hear a gloomy voice call \'') + pronoun(playerGender) + String(value=' will stay here forever...\''))
                self.DarkGray()
            #check if the player has the required key to unlock the room
            assert False, '# UNTRANSLATED VB LINE #358 [Select inventory]'
            assert False, '# UNTRANSLATED VB LINE #359 [Case 3 'Dungeon Key]'
            if playerInput == Integer(6) and programEnd == Integer(0) and roomLocked(Integer(6)) == Integer(1):
                Console.ForegroundColor = ConsoleColor.DarkGreen
                Console.WriteLine(String(value='Your key fits into the door lock. You turn it and hear a click.'))
                roomLocked[Integer(6)] = Integer(0)
                self.Blank()
                self.DarkGray()
            assert False, '# UNTRANSLATED VB LINE #368 [Case 4 'Closet Key]'
            if playerInput == Integer(8) and programEnd == Integer(0) and roomLocked(Integer(8)) == Integer(1):
                Console.ForegroundColor = ConsoleColor.DarkGreen
                Console.WriteLine(String(value='Your key fits into the door lock. You turn it and hear a click.'))
                roomLocked[Integer(8)] = Integer(0)
                self.Blank()
                self.DarkGray()
            assert False, '# UNTRANSLATED VB LINE #377 [Case 5 'Bedroom Key]'
            if playerInput == Integer(13) and programEnd == Integer(0) and roomLocked(Integer(13)) == Integer(1):
                Console.ForegroundColor = ConsoleColor.DarkGreen
                Console.WriteLine(String(value='Your key fits into the door lock. You turn it and hear a click.'))
                roomLocked[Integer(13)] = Integer(0)
                self.Blank()
                self.DarkGray()
            assert False, '# UNTRANSLATED VB LINE #385 [End Select]'
            #If player entered 0-18
            assert False, '# UNTRANSLATED VB LINE #388 [If playerInput>=0 And programEnd=0 And playerInput<=18 Then]'
            #check if room locked
            assert False, '# UNTRANSLATED VB LINE #390 [If roomLocked(playerInput)=0 And programEnd=0 Then]'
            #when room is unlocked
            playerRoomNum = playerInput
            assert False, '# UNTRANSLATED VB LINE #393 [Else If programEnd=0]'
            #say room is locked
            self.Red()
            Console.WriteLine(String(value='This room is locked!'))
            self.Blank()
            self.DarkGray()
            assert False, '# UNTRANSLATED VB LINE #399 [End If]'
            #check if the player has a candle or torch
            if inventory == Integer(0) and programEnd == Integer(0):
                self.Yellow()
                Console.WriteLine(String(value='Your candle illuminates the area'))
                self.DarkGray()
            if inventory == Integer(6) and programEnd == Integer(0):
                self.Yellow()
                Console.WriteLine(String(value='Your torch illuminates the area'))
                self.DarkGray()
            #check if a candle or torch is in that room
            if not inventory == Integer(0) and not inventory == Integer(6) and itemLocation(Integer(0)) == playerRoomNum and not itemLocation(Integer(6)) == playerRoomNum and programEnd == Integer(0):
                self.Yellow()
                Console.WriteLine(String(value='A candle illuminates the room'))
                self.DarkGray()
            if not inventory == Integer(6) and not inventory == Integer(0) and itemLocation(Integer(6)) == playerRoomNum and programEnd == Integer(0):
                self.Yellow()
                Console.WriteLine(String(value='A torch illuminates the room'))
                self.DarkGray()
            #check if room lit
            assert False, '# UNTRANSLATED VB LINE #426 [If roomLit(playerRoomNum)=1 And programEnd=0 Or inventory=0 And programEnd=0 Or inventory=6 And programEnd=0 Or itemLocation(0)=playerRoomNum And programEnd=0 Or itemLocation(6)=playerRoomNum And programEnd=0 Then]'
            #display room name and desc (when room is lit)
            Console.ForegroundColor = ConsoleColor.White
            Console.WriteLine(String(value='You are ') + roomName(playerRoomNum) + String(value=', ') + roomDesc(playerRoomNum))
            self.DarkGray()
            assert False, '# UNTRANSLATED VB LINE #431 [Else If programEnd=0]'
            #say it is too dark
            Console.ForegroundColor = ConsoleColor.White
            Console.WriteLine(String(value='You are in the ') + roomName(playerRoomNum))
            self.Red()
            Console.WriteLine(String(value='It is too dark to see a thing'))
            self.DarkGray()
            assert False, '# UNTRANSLATED VB LINE #438 [End If]'
            #player travels with items
            if inventory >= Integer(0):
                itemLocation[inventory] = playerRoomNum
            #check for hostile creatures (if you have no torch)
            if diffProb(difficulty) > Fix(Integer(100) * Rnd()) and programEnd == Integer(0) and not inventory == Integer(0) and not inventory == Integer(6):
                playerLives = playerLives - Integer(1)
                self.DarkRed()
                self.Blank()
                Console.WriteLine(String(value='---------------------------------------------------'))
                Console.WriteLine(String(value=' You feel an eerie pain...'))
                Console.WriteLine(String(value=' Blood stains begin to appear on your clothes...'))
                if playerLives == Integer(1):
                    Console.Write(String(value=' You have '))
                    self.Red()
                    Console.Write(String(value='1 life '))
                    self.DarkRed()(Console.WriteLine(String(value='remaining...')))
                else:
                    Console.Write(String(value=' You have '))
                    self.Red()
                    Console.Write(playerLives + String(value=' lives '))
                    self.DarkRed()(Console.WriteLine(String(value='remaining...')))
                Console.WriteLine(String(value='---------------------------------------------------'))
                self.Blank()
                self.DarkGray()
            #end game if player runs out of lives
            if playerLives <= Integer(0):
                programEnd = Integer(1)
            #give the player a clue to where the brass key is
            if playerRoomNum == Integer(3) or playerRoomNum == Integer(10) or playerRoomNum == Integer(11) or playerRoomNum == Integer(16):
                if programEnd == Integer(0) and itemLocation(Integer(4)) == Integer(18) and not difficulty >= Integer(4):
                    self.Blank()
                    self.Yellow()
                    Console.WriteLine(String(value='You see a glint coming from the roof of the house'))
                    self.DarkGray()
                    self.Yellow()
            #check room items
            for x in vbForRange(Integer(0), Integer(15)):
                #check if the item is in the player's room
                #IF PLAYER IS NOT IN TREASURY
                if itemLocation(x) == playerRoomNum and not inventory == x and not playerRoomNum == Integer(15):
                    #check if the room is lit
                    if roomLit(playerRoomNum) == Integer(1) and programEnd == Integer(0) or inventory == Integer(0) and programEnd == Integer(0) or inventory == Integer(6) and programEnd == Integer(0) or itemLocation(Integer(0)) == playerRoomNum and programEnd == Integer(0) or itemLocation(Integer(6)) == playerRoomNum and programEnd == Integer(0):
                        self.Blank()
                        #say item decription
                        self.Blue()
                        Console.WriteLine(String(value='You can see ') + itemDesc(x))
                        #ask if player wishes to pick up the item
                        Console.ForegroundColor = ConsoleColor.Gray
                        if inventory == - Integer(1):
                            Console.WriteLine(String(value='Would you like to pick up this item? 0:No 1:Yes'))()
                            #If player has no held item
                        if inventory >= Integer(0):
                            Console.WriteLine(String(value='Would you like to pick up this item (and drop your current item)? 0:No 1:Yes'))()
                            #If player has a held item
                        itemPickup = Val(Console.ReadLine)
                        #if player picks item up
                        if itemPickup == Integer(1):
                            self.Blue()
                            Console.WriteLine(String(value='You have picked up this item.'))
                            self.DarkGray()
                            #put the item in their inventory
                            inventory = x
                #IF PLAYER IS IN TREASURY
                if itemLocation(x) == playerRoomNum and not inventory == x and playerRoomNum == Integer(15) and inventory == Integer(2):
                    #check if the room is lit
                    if roomLit(playerRoomNum) == Integer(1) and programEnd == Integer(0) or inventory == Integer(0) and programEnd == Integer(0) or inventory == Integer(6) and programEnd == Integer(0) or itemLocation(Integer(0)) == playerRoomNum and programEnd == Integer(0) or itemLocation(Integer(6)) == playerRoomNum and programEnd == Integer(0):
                        self.Blank()
                        #say item decription
                        self.Blue()
                        Console.WriteLine(String(value='You can see ') + itemDesc(x))
                        #ask if player wishes to pick up the item
                        Console.ForegroundColor = ConsoleColor.Gray
                        if inventory == - Integer(1):
                            Console.WriteLine(String(value='Would you like to pick up this item? 0:No 1:Yes'))()
                            #If player has no held item
                        if inventory >= Integer(0):
                            Console.WriteLine(String(value='Would you like to pick up this item (and drop your current item)? 0:No 1:Yes'))()
                            #If player has a held item
                        itemPickup = Val(Console.ReadLine)
                        #if player picks item up
                        if itemPickup == Integer(1):
                            self.Blue()
                            Console.WriteLine(String(value='You have picked up this item.'))
                            self.DarkGray()
                            #put the item in their inventory
                            inventory = x
            assert False, '# UNTRANSLATED VB LINE #541 [End If]'
            #ask if player wants to drop item
            if playerInput == Integer(20):
                if not inventory == - Integer(1) and programEnd == Integer(0):
                    self.Gold()
                    self.Blank()
                    Console.Writeline(String(value='You are holding ') + itemDesc(inventory) + String(value='. Would you like to drop it? 0:No 1:Yes'))
                    if Console.ReadLine() == Integer(1):
                        inventory = - Integer(1)
            self.DarkGray()
            #display all room numbers and names
            if playerInput == Integer(21):
                for x in vbForRange(Integer(0), Integer(18)):
                    self.White()
                    Console.WriteLine(String(value='Room ') + x + String(value=': ') + SroomName(x))
                    self.DarkGray()
            #cheat code: The Special Shed (Code 1234)- This was used for testing items. It is no longer in use.
            #            If playerInput=1234 Then
            #                Cyan()
            #                Blank()
            #                Console.WriteLine("--------------------------------------------------------------------------------------------------------")
            #                Console.WriteLine("You are in the Special Shed, an interdimensional shed that has access to every item in the haunted house.")
            #                Console.WriteLine("--------------------------------------------------------------------------------------------------------")
            #                For x=0 To 15
            #                    Blank()
            #                    'say item decription
            #                    Blue()
            #                    Console.WriteLine("You can see " & itemDesc(x))
            #
            #                    'ask if player wishes to pick up the item
            #                    Console.ForegroundColor=ConsoleColor.Gray
            #                    Console.WriteLine("Would you like to pick up this item? 0:No 1:Yes")
            #                    itemPickup=Val(Console.ReadLine)
            #
            #                    'if player picks item up
            #                    If itemPickup=1 Then
            #                        Console.WriteLine("You have picked up this item.")
            #                        DarkGray()
            #                        'put the item in their inventory
            #                        inventory=x
            #                    End If
            #                Next
            #
            #            End If
            #end of game loop
        #game end
        #If player left alive
        if playerLives >= Integer(1) and playerAge >= Integer(13):
            self.Blank()
            self.Green()
            Console.WriteLine(String(value='Well done ') + playerName + String(value='! You have left the haunted house alive!'))
            if playerLives > Integer(1):
                Console.WriteLine(String(value='You had ') + playerLives + String(value=' lives left.'))()
                if playerLives == Integer(1):
                    Console.WriteLine(String(value='You had 1 life left.'))()
            if not inventory == - Integer(1):
                self.Gold()
                Console.WriteLine(String(value='You are holding ') + itemDesc(inventory) + String(value='. It is worth £') + itemValue(inventory) + String(value='.'))
                playerScore = ( itemValue(inventory) *  ( difficulty + Integer(1) ) )  +  ( playerLives * Integer(1000) *  ( difficulty + Integer(1) ) )
            else:
                playerScore = playerLives * Integer(1000) *  ( difficulty + Integer(1) )
            Console.WriteLine(String(value='Score: ') + playerScore)
            self.Blank()
            self.Gold()
            Console.WriteLine(String(value=' ▓██   ██▓ ▒█████   █    ██    ▓█████   ██████  ▄████▄   ▄▄▄       ██▓███  ▓█████ ▓█████▄ '))
            Console.WriteLine(String(value=' ▒██  ██▒▒██▒  ██▒ ██  ▓██▒   ▓█   ▀ ▒██    ▒ ▒██▀ ▀█  ▒████▄    ▓██░  ██▒▓█   ▀ ▒██▀ ██▌'))
            Console.WriteLine(String(value='  ▒██ ██░▒██░  ██▒▓██  ▒██░   ▒███   ░ ▓██▄   ▒▓█    ▄ ▒██  ▀█▄  ▓██░ ██▓▒▒███   ░██   █▌'))
            Console.WriteLine(String(value='  ░ ▐██▓░▒██   ██░▓▓█  ░██░   ▒▓█  ▄   ▒   ██▒▒▓▓▄ ▄██▒░██▄▄▄▄██ ▒██▄█▓▒ ▒▒▓█  ▄ ░▓█▄   ▌'))
            Console.WriteLine(String(value='  ░ ██▒▓░░ ████▓▒░▒▒█████▓    ░▒████▒▒██████▒▒▒ ▓███▀ ░ ▓█   ▓██▒▒██▒ ░  ░░▒████▒░▒████▓ '))
            Console.WriteLine(String(value='   ██▒▒▒ ░ ▒░▒░▒░ ░▒▓▒ ▒ ▒    ░░ ▒░ ░▒ ▒▓▒ ▒ ░░ ░▒ ▒  ░ ▒▒   ▓▒█░▒▓▒░ ░  ░░░ ▒░ ░ ▒▒▓  ▒ '))
            Console.WriteLine(String(value=' ▓██ ░▒░   ░ ▒ ▒░ ░░▒░ ░ ░     ░ ░  ░░ ░▒  ░ ░  ░  ▒     ▒   ▒▒ ░░▒ ░      ░ ░  ░ ░ ▒  ▒ '))
            Console.WriteLine(String(value=' ▒ ▒ ░░  ░ ░ ░ ▒   ░░░ ░ ░       ░   ░  ░  ░  ░          ░   ▒   ░░          ░    ░ ░  ░ '))
            Console.WriteLine(String(value=' ░ ░         ░ ░     ░           ░  ░      ░  ░ ░            ░  ░            ░  ░   ░    '))
        #If player died
        if playerLives <= Integer(0) and playerAge >= Integer(13):
            self.DarkRed()
            Console.WriteLine(String(value='Your vision starts to go black as all life leaves you. You hear a voice call: \'') + pronoun(playerGender) + String(value=' will stay here for eternity...\''))
            self.Blank()
            Console.WriteLine(String(value=' ▄████  ▄▄▄       ███▄ ▄███▓▓█████     ▒█████   ██▒   █▓▓█████  ██▀███  '))
            Console.WriteLine(String(value=' ██▒ ▀█▒▒████▄    ▓██▒▀█▀ ██▒▓█   ▀    ▒██▒  ██▒▓██░   █▒▓█   ▀ ▓██ ▒ ██▒'))
            Console.WriteLine(String(value='▒██░▄▄▄░▒██  ▀█▄  ▓██    ▓██░▒███      ▒██░  ██▒ ▓██  █▒░▒███   ▓██ ░▄█ ▒'))
            Console.WriteLine(String(value='░▓█  ██▓░██▄▄▄▄██ ▒██    ▒██ ▒▓█  ▄    ▒██   ██░  ▒██ █░░▒▓█  ▄ ▒██▀▀█▄  '))
            Console.WriteLine(String(value='░▒▓███▀▒ ▓█   ▓██▒▒██▒   ░██▒░▒████▒   ░ ████▓▒░   ▒▀█░  ░▒████▒░██▓ ▒██▒'))
            Console.WriteLine(String(value=' ░▒   ▒  ▒▒   ▓▒█░░ ▒░   ░  ░░░ ▒░ ░   ░ ▒░▒░▒░    ░ ▐░  ░░ ▒░ ░░ ▒▓ ░▒▓░'))
            Console.WriteLine(String(value='  ░   ░   ▒   ▒▒ ░░  ░      ░ ░ ░  ░     ░ ▒ ▒░    ░ ░░   ░ ░  ░  ░▒ ░ ▒░'))
            Console.WriteLine(String(value='░ ░   ░   ░   ▒   ░      ░      ░      ░ ░ ░ ▒       ░░     ░     ░░   ░ '))
            Console.WriteLine(String(value='     ░       ░  ░       ░      ░  ░       ░ ░        ░     ░  ░   ░      '))
        self.Blank()
        self.DarkGray()
        Console.WriteLine(String(value='Press any key to exit'))
        Console.ReadKey(True)

