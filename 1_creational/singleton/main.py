_db_instance = None


class Database:
    def __init__(self):
        pass


def get_db_instance():
    global _db_instance

    if not _db_instance:
        _db_instance = Database()

    return _db_instance


def client_code():
    foo = get_db_instance()
    bar = get_db_instance()

    print(id(foo))
    print(id(bar))
    if id(foo) == id(bar):
        print("Singleton works, both variables contain the same instance.")


if __name__ == '__main__':
    client_code()
