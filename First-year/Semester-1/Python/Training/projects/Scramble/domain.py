from random import randint

class Sentence:

    def readfromfile(self, fname):

        with open(fname, 'r') as f:
            lines = f.readlines()
            a = randint(0, len(lines)-1)
            self.sentence = lines[a]
            self.sentence = self.sentence.strip("\n")

a = "rwtetrytu"
print(a[len(a)-2])