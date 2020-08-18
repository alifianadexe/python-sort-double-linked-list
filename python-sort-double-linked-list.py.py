#!/usr/bin/python
# Dari anak TryHard Ngoding
import time


class Data(object):
    def __init__(self, name):
        self.name = name

    def __compare(self, name):
        return 1 if self.name > name else -1 if self.name < name else 0

    def compare(self, data):
        if type(data) == str:
            return self.__compare(data)
        else:
            return self.__compare(data.name)

    def print(self):
        print("{0}".format(self.name))


class Rantai(object):
    def __init__(self, data):
        self.data = data
        self.__next = None
        self.__prev = None

    def compare(self, data):
        return self.data.compare(data)

    def print(self):
        self.data.print()

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, node):
        self.__next = node

    @property
    def prev(self):
        return self.__prev

    @prev.setter
    def prev(self, node):
        self.__prev = node


class RantaiTerurut(object):

    def __init__(self):
        self.KEPALA = None
        self.BUNTUT = None
        self.POSISI = None

    def node_print(self):
        current = self.KEPALA
        while current is not None:
            current.print()
            current = current.next

    def node_append(self, str_data):
        data = Data(str_data)
        self.__do_append(data)

    def __do_append(self, data):
        
        new_chain = Rantai(data)
        new_chain.next = None

        # kepalanya ada nggak? klo ngga diisi
        if self.KEPALA == None:
            self.KEPALA = new_chain
            self.BUNTUT = new_chain
            self.KEPALA.prev = None    
            return

        # jika kepala lebih kecil atau sama dengan, maka kepalannya diganti
        if new_chain.compare(self.KEPALA.data) in [-1, 0]:    
            new_chain.prev = None
            self.KEPALA.prev = new_chain
            new_chain.next = self.KEPALA
            self.KEPALA = new_chain
            return  
        
        # jika buntut lebih besar maka buntutnya diganti
        if new_chain.compare(self.BUNTUT.data) in [ 1, 0]:
            new_chain.prev = self.BUNTUT
            self.BUNTUT.next = new_chain
            self.BUNTUT = new_chain
            return

        # itterate dari setelah kepala, buat cari yang mana yang mau diappend
        self.POSISI = self.KEPALA.next
        while self.POSISI.compare(new_chain.data) in [-1,0]:
            self.POSISI = self.POSISI.next
    
        # tuker dengan apa yang uda ada
        (self.POSISI.prev).next = new_chain
        new_chain.prev = self.POSISI.prev
        self.POSISI.prev = new_chain
        new_chain.next = self.POSISI

        # raise NotImplementedError()


def calculate_time(func):
    def function_timer(*args, **kwargs):
        """
        A nested function for timing other functions
        """
        start = time.time()
        value = func(*args, **kwargs)
        end = time.time()
        runtime = end - start
        msg = "The runtime for {func} took {time} seconds to complete"
        print(msg.format(func=func.__name__,
                         time=runtime))
        return value

    return function_timer


@calculate_time
def perform_benchmark(chain_list, list_data):
    for str_data in list_data:
        chain_list.node_append(str_data)

if __name__ == "__main__":

    with open("./data2.txt", encoding="utf8") as text_file:
        lines = text_file.read().splitlines()

    chain_list = RantaiTerurut()
    perform_benchmark(chain_list, lines)
    # chain_list.node_print() 