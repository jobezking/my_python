class Dog:
    def __init__(self, name, month, day, year, speakText):
        self.name = name
        self.month = month
        self.day = day
        self.year = year
        self.speakText = speakText
    #####
    def speak(self):
        return self.speakText
    def getName(self):
        return self.name
    def  birthDate(self):
        return str(self.month) + "/" + str(self.day) + "/" + str(self.year)
    def changeBark(self,bark):
        self.speakText = bark