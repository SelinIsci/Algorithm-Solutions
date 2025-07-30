class Dinglemouse(object):

    def __init__(self):
        self.name = None
        self.age = None
        self.sex = None
        self.order = []

    def setName(self, name):
        if "name" not in self.order:
            self.order.append("name")
        self.name = name
        return self

    def setAge(self, age):
        if "age" not in self.order:
            self.order.append("age")
        self.age = age
        return self

    def setSex(self, sex):
        if "sex" not in self.order:
            self.order.append("sex")
        self.sex = sex
        return self

    def hello(self):
        parts = []
        for attr in self.order:
            if attr == "name":
                parts.append(f"My name is {self.name}.")
            elif attr == "age":
                parts.append(f"I am {self.age}.")
            elif attr == "sex":
                gender = "male" if self.sex == "M" else "female"
                parts.append(f"I am {gender}.")
        return "Hello." + (" " + " ".join(parts) if parts else "")
