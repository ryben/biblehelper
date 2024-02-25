from abc import abstractmethod, ABC


class FileParser(ABC):
    @abstractmethod
    def parse(self, filepath):
        pass
