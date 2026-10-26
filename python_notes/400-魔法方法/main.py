class Logbook(object):

    def __new__(cls, *args, **kwargs):
        print("__new__ invoke")
        return super(Logbook, cls).__new__(cls)

    def __init__(self, records=None):
        if records is None:
            records = []
        print("__init__ invoke")
        self.records = records

    def __len__(self):
        return len(self.records)


if __name__ == '__main__':
    logbook = Logbook(['a', 'b', 'c'])
