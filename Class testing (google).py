class Classy(object):
    def __init__(self):
        self.items = []

#Test classes
me = Classy()
#Should be 0
print me.getClassiness()

me.addItem("tophat")
print me.getClassiness()

me.addItem("bowtie")
me.addItem("jacket")
me.addItem("monocle")

print me.getClassiness()

me.addItem("bowtie")
#Should be 15
print me.getClassiness()



        
