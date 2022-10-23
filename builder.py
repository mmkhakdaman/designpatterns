from abc import ABC
import abstract_facotry


class BuilderAbstract(ABC):
    def build_display(self):
        pass

    def build_cpu(self):
        pass

    def build_ram(self):
        pass


class AppleIphone7Builder(BuilderAbstract):
    def build_display(self):
        return abstract_facotry.AppleMobileDisplay()

    def build_cpu(self):
        return abstract_facotry.AppleCPU()

    def build_ram(self):
        return abstract_facotry.AppleRAM()


class SamsungGalaxyS7Builder(BuilderAbstract):
    def build_display(self):
        return abstract_facotry.SamsungMobileDisplay()

    def build_cpu(self):
        return abstract_facotry.SamsungCPU()

    def build_ram(self):
        return abstract_facotry.SamsungRAM()

class myPhone:
    def __init__(self, builder: BuilderAbstract):
        self.display = builder.build_display()
        self.cpu = builder.build_cpu()
        self.ram = builder.build_ram()

    def __str__(self):
        return f'{self.display}, {self.cpu}, {self.ram}'


class Director:
    def __init__(self, builder):
        self.builder = builder

    def build(self):
        self.builder.build_display()
        self.builder.build_cpu()
        self.builder.build_ram()


if __name__ == '__main__':
    iphone7_builder = AppleIphone7Builder()
    iphone7_director = Director(iphone7_builder)
    iphone7_director.build()
    print(iphone7_builder.build_display())

    myPhone = myPhone(iphone7_builder)

    print(myPhone)

    galaxy_s7_builder = SamsungGalaxyS7Builder()
    galaxy_s7_director = Director(galaxy_s7_builder)
    galaxy_s7_director.build()