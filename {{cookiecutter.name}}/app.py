class Application:
    def __init__(self, element="app"):
        self.element = element
        self.counter = 0

    def greet(self):
        self.counter += 1
        element = document.getElementById(self.element)
        element.innerHTML = f"Hello App {self.counter}!"
