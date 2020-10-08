class A:
    def __init__(self, *args, **kwargs):
        # has a generator
        self.generator = kwargs.get("generator", None)
    def generate(self):
        if self.generator:
            self.generator().generate(self)
    def py_gen(self):
        print("python code gen")
    def cpp_gen(self):
        print("c++ code gen")

class PyGenerator:
    def generate(self, owner):
        owner.py_gen()

class CPPGenerator:
    def generate(self, owner):
        owner.cpp_gen()

a = A(generator=PyGenerator)
b = A(generator=CPPGenerator)

for x in [a, b]:
    x.generate()
