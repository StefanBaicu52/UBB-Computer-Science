from domain import Sentence
import random

class UI:

    def game(self):

        s = Sentence()
        s.readfromfile("Scramble.txt")
        string = ""
        liststable = []
        listshuffle = []
        listcuv = []
        liststable.append(0)
        liststable.append(len(s.sentence)-1)
        contor = 0
        i1 = 0
        i2 = 0
        for i in range(len(s.sentence)):
            if s.sentence[i] == " ":
                i1 = i2
                i2 = i
                cuv = s.sentence[i1:i2]
                cuv = cuv.strip()
                listcuv.append(cuv)
                liststable.append(i)
                liststable.append(i-1)
                liststable.append(i+1)

            else:
                contor += 1
        i1 = i2
        i2 = len(s.sentence)
        cuv = s.sentence[i1:i2]
        cuv = cuv.strip()
        listcuv.append(cuv)

        for i in range(len(s.sentence)):
            if i not in liststable:
                listshuffle.append(i)

        for i in range(len(s.sentence)):
            if i in liststable:
                string = string + s.sentence[i]
            else:
                a = random.choice(listshuffle)
                string = string + s.sentence[a]
                listshuffle.remove(a)

        print("Game begins! \n")
        print("This is your sentence: ")
        print(string + " [Your score is: " + str(contor) + "]")
        maxx = contor
        oldstring = string

        #print(listcuv)
        while string != s.sentence and contor != 0:
            ok = False
            while ok == False:
                cmd = input()
                if cmd == "undo":
                    string = oldstring
                    if contor + 1 < maxx:
                        contor += 1
                    print(string + " [Your score is: " + str(contor) + "]")
                else:
                    cmd = cmd.split(" ")
                    if len(cmd) != 5:
                        print("The command does not respect the format!")
                    else:
                        if cmd[0] != "swap":
                            print("The command " + cmd[0] + "does not exist!")
                        else:
                            if cmd[1].isdigit() == False or cmd[2].isdigit() == False or cmd[3].isdigit() == False or cmd[4].isdigit() == False:
                                print("One of the indices is not a number!")
                            else:
                                c1 = int(cmd[1])
                                c2 = int(cmd[2])
                                c3 = int(cmd[3])
                                c4 = int(cmd[4])
                                if c1 > len(listcuv) - 1 or c3 > len(listcuv) - 1:
                                    print("The indices of the words are out of range!")
                                else:
                                    if c2 > len(listcuv[c1]) - 2 or c4 > len(listcuv[c3]) - 2 or c2 == 0 or c4 == 0:
                                        print("The indices of the letters are out of range!")
                                    else:
                                        a = 0
                                        b = 0
                                        for j in range(c1):
                                            a = a + len(listcuv[j]) + 1
                                        a += c2
                                        for j in range(c3):
                                            b = b + len(listcuv[j]) + 1
                                        b += c4
                                        newstring = ""
                                        for i in range(len(string)):
                                            if i == a:
                                                newstring = newstring + string[b]
                                            elif i == b:
                                                newstring = newstring + string[a]
                                            else:
                                                newstring = newstring + string[i]
                                        oldstring = string
                                        string = newstring
                                        contor -= 1
                                        print(string + " [Your score is: " + str(contor) + "]")
                                        ok = True
        if string == s.sentence:
            print("You win! Your score is: " + str(contor))
        else:
            print("You lost!")


ui = UI()
ui.game()
