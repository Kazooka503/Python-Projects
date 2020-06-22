from abc import ABC, abstractmethod

class Computer(ABC):
    #abstraction 
    @abstractmethod
    def process(self):
        pass
    def compute(self):
        print("Computed!")

class Laptop(Computer):
    #defined implementation of parent's abstraction 
    def process(self):
        print("its running")


x = Laptop()
x.process()
x.compute()
