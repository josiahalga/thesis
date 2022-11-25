class lane:
    def __init__(self):
        self.state = 1
    
    def switch_red(self):
        self.state = 1
     
    def switch_yellow(self):
        self.state = 2
        
    def switch_green(self):
        self.state = 3