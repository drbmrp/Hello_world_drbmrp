from .Utils import Multiply

class TemplateGitHub(object):
    legs = 4
    def __init__(self,x):
        self.x = x
        self.state = 'calmed'
        print('Built template class')
        pass

    def Bark(self):
        print('guaff')
        self.state = 'barking'
        pass

    def CalmDown(self):
        self.state = 'calmed'
        pass

    def MultiplyBy(self,multiplier):
        out = Multiply(self.x,multiplier)
        return out
    

