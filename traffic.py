class lane:
    def __init__(self):
        self.red = False
        self.yellow = False
        self.green = False
    
    def red(self):
        self.red = True
        self.yellow = False
        self.green = False
     
    def yellow(self):
        self.yellow = True
        self.red = False
        self.green = False
        
    def green(self):
        self.green = True
        self.red = False
        self.yellow = False