class Logger:
    filename = None
    logFile = None

    def __init__(self, filename = ""):
        self.filename = filename

    def OpenLogFile(self):
        self.logFile = open(self.filename, "w")
    def WriteToLogFile(self, string):
        self.logFile.write(string)
    def CloseLogFile(self):
        self.logFile.close()