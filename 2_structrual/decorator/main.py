from abc import ABC, abstractmethod


class DataSource(ABC):
    @abstractmethod
    def write_data(self, data):
        pass

    @abstractmethod
    def read_data(self):
        pass


class FileDataSource(DataSource):
    def __init__(self, filename):
        self.filename = filename
        self.data = ""

    def write_data(self, data):
        print(f'Writing data {data} to file {self.filename}')
        self.data = data

    def read_data(self):
        print(f'Reading data from file {self.filename}')
        return self.data


class DataSourceDecorator(DataSource):
    def __init__(self, source: DataSource):
        self.wrapper = source

    def write_data(self, data):
        self.wrapper.write_data(data)

    def read_data(self):
        return self.wrapper.read_data()


class EncryptionDecorator(DataSourceDecorator):
    def write_data(self, data):
        print(f'Encrypting data {data}...')
        self.wrapper.write_data('Encrypted'+data)

    def read_data(self):
        data = self.wrapper.read_data()
        print(f'Decrypting data...')
        return data.lstrip('Encrypted')


class CompressionDecorator(DataSourceDecorator):
    def write_data(self, data):
        print(f'Compressing data {data}...')
        data = data[:len(data)//2]
        self.wrapper.write_data(data)

    def read_data(self):
        data = self.wrapper.read_data()
        print(f'Decompressing data...')
        return data*2


def client_code():
    source = FileDataSource("somefile.dat")

    source.write_data("aaa")
    data = source.read_data()
    print(f'Reading the data just written: {data}')
    print()

    source = EncryptionDecorator(source)
    source.write_data("bbb")
    data = source.read_data()
    print(f'Reading the data just written: {data}')
    print()

    source = CompressionDecorator(source)
    source.write_data("abcabc")
    data = source.read_data()
    print(f'Reading the data just written: {data}')
    print()


if __name__ == "__main__":
    client_code()
