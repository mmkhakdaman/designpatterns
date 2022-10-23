from abc import ABC, ABCMeta, abstractmethod


class AbstractDisplay(ABC):
    @abstractmethod
    def width(self) -> int:
        pass

    @abstractmethod
    def height(self) -> int:
        pass

class AbstractMobileDisplay(AbstractDisplay):
    @abstractmethod
    def z(self) -> int:
        pass

class AppleMobileDisplay(AbstractMobileDisplay):
    def width(self) -> int:
        return 100

    def height(self) -> int:
        return 200

    def z(self) -> int:
        return 300

    def __str__(self):
        return 'AppleMobileDisplay'


class AbstractCPU(ABC):
    @abstractmethod
    def cores(self) -> int:
        pass

    @abstractmethod
    def frequency(self) -> int:
        pass


class AbstractRAM(ABC):
    @abstractmethod
    def size(self) -> int:
        pass

    @abstractmethod
    def frequency(self) -> int:
        pass


class AbstractSystem(ABC):
    @abstractmethod
    def display(self) -> AbstractDisplay:
        pass

    @abstractmethod
    def CPU(self) -> AbstractCPU:
        pass

    @abstractmethod
    def RAM(self) -> AbstractRAM:
        pass


class AppleDisplay(AbstractDisplay):
    def width(self) -> int:
        return 1920

    def height(self) -> int:
        return 1080

    def __str__(self) -> str:
        return 'AppleDisplay'


class AppleCPU(AbstractCPU):
    def cores(self) -> int:
        return 8

    def frequency(self) -> int:
        return 3.8

    def __str__(self) -> str:
        return 'AppleCPU'


class AppleRAM(AbstractRAM):
    def size(self) -> int:
        return 16

    def frequency(self) -> int:
        return 2666

    def __str__(self) -> str:
        return 'AppleRAM'




class GoogleRAM(AbstractRAM):
    def size(self) -> int:
        return 32

    def frequency(self) -> int:
        return 2666

    def __str__(self) -> str:
        return 'GoogleRAM'



class AppleSystem(AbstractSystem):
    def display(self) -> AbstractDisplay:
        return AppleDisplay()

    def CPU(self) -> AbstractCPU:
        return AppleCPU()

    def RAM(self) -> AbstractRAM:
        return AppleRAM()

    def __str__(self) -> str:
        return 'AppleSystem'



class MySystem(AbstractSystem):
    def display(self) -> AbstractDisplay:
        return AppleDisplay()

    def CPU(self) -> AbstractCPU:
        return AppleCPU()

    def RAM(self) -> AbstractRAM:
        return AppleRAM()

    def __str__(self) -> str:
        return 'MySystem'

class SamsungMobileDisplay(AbstractMobileDisplay):
    def width(self) -> int:
        return 100

    def height(self) -> int:
        return 200

    def z(self) -> int:
        return 300

    def __str__(self) -> str:
        return 'SamsungMobileDisplay'



class SamsungCPU(AbstractCPU):
    def cores(self) -> int:
        return 8

    def frequency(self) -> int:
        return 3.8

    def __str__(self) -> str:
        return 'SamsungCPU'



class SamsungRAM(AbstractRAM):
    def size(self) -> int:
        return 16

    def frequency(self) -> int:
        return 2666

    def __str__(self) -> str:
        return 'SamsungRAM'


