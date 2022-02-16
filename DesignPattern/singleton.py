class SingleTonNew:
    _instance = None

    @staticmethod
    def get_instance():
        if SingleTonNew._instance is None:
            SingleTonNew()
        return SingleTonNew._instance

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, a=0):
        self.a = a


s1 = SingleTonNew(a=11)
s2 = SingleTonNew(a=10)
print(id(s1), s1.a)
print(id(s2), s2.a)
print(SingleTonNew.get_instance().a)
