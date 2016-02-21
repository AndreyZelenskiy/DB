# coding=utf-8
from model.producer import Producer
from model.film import Film
import cPickle as pickle

#TODO: подключение библиотеки pickle

class Application:
    def __init__(self):
        self.__list_of_producers = pickle.load(open("producers.txt", "rb"))
        self.__list_of_films = pickle.load(open("films.txt", "rb"))
        self.__dictionary = pickle.load(open("dictionary.txt", "rb"))
        self.__menu = ["1. Add producer",
                       "2. Add film",
                       "3. Display producers",
                       "4. Display films",
                       "5. Delete producer",
                       "6. Delete film",
                       "7. Edit producer",
                       "8. Edit film",
                       "9. Display filmed in Ukraine",
                       "Type 'exit' to exit))"
                       ]
        #TODO: инициализация из файла (Конфигурироваие его каким то образом

    def display_menu(self):
        for item in self.__menu:
            print item

    def action(self, menu_item):
        if menu_item == 1:
            name = str(raw_input("Enter name of new producer: "))
            surname = str(raw_input("Enter surname: "))
            self.__add_producer(name, surname)
        elif menu_item == 2:
            name = raw_input("Enter name of film: ")
            country = raw_input("Enter country: ")
            self.__display_producers()
            producer = int(raw_input("Enter producer index: ")) - 1
            if 0 <= producer < len(self.__list_of_producers):
                self.__add_film(Film(name, country), self.__list_of_producers[producer])
            else:
                print "Incorrect index"
        elif menu_item == 3:
            self.__display_producers()
        elif menu_item == 4:
            self.__display_films()
        elif menu_item == 5:
            self.__display_producers()
            index = int(input("Enter producer index: ") - 1)
            if 0 <= index < len(self.__list_of_producers):
                self.__delete_producer(self.__list_of_producers[index])
            else:
                print "Failed index!"
        elif menu_item == 6:
            self.__display_films()
            index = int(input("Enter film index: ")) - 1
            if 0 <= index < len(self.__list_of_films):
                self.__delete_film(self.__list_of_films[index])
            else:
                print "Failed index!"
        elif menu_item == 7:
            self.__display_producers()
            index = int(input("Enter producer index: ")) - 1

            if index < 0 or index >= len(self.__list_of_producers):
                print "Failed index!"
            else:
                producer = self.__list_of_producers[index]
                name = raw_input("Enter new name: ")
                if name == "":
                    name = producer.name

                surname = raw_input("Enter new surname: ")
                if surname == "":
                    surname = producer.surname
                self.__edit_producer(producer, name, surname)
        elif menu_item == 8:
            self.__display_films()
            index = int(input("Enter film index: ")) - 1
            if 0 <= index < len(self.__list_of_films):
                film = self.__list_of_films[index]
                name = raw_input("Enter new name of film: ")
                country = raw_input("Enter new country of filmed: ")
                self.__display_producers()
                producer_index = int(input("Enter producer index: ")) - 1
                if not 0 <= index <len(self.__list_of_producers):
                    print "Incorrect producer!"
                    return
                if name == "":
                    name = film.name
                if country == "":
                    country = film.country
                self.__edit_film(film, name, country, self.__list_of_producers[producer_index])
        elif menu_item == 9:
            self.__display_filmed_in_ukraine()

    def __add_producer(self, name, surname):
        producer = Producer(name, surname)
        if producer not in self.__list_of_producers:
            self.__list_of_producers.append(Producer(name, surname))
        else:
            print "Duplicate producers"

    def __add_film(self, film, producer):
        if film in self.__list_of_films:
            print "Duplicate film!"
            return
        self.__list_of_films.append(film)
        self.__dictionary[film] = producer

    def __display_producers(self):
        for producer in self.__list_of_producers:
            print str(self.__list_of_producers.index(producer) + 1) + ". " + str(producer)
        #TODO: вывод списка фильмов

    def __display_films(self):
        for film in self.__list_of_films:
            print str(self.__list_of_films.index(film) + 1) + ". " + str(film)

    def __delete_producer(self, producer):
        dictionary = self.__dictionary.copy()
        for key in dictionary:
            if dictionary[key] == producer:
                self.__list_of_films.remove(key)
                del self.__dictionary[key]
        self.__list_of_producers.remove(producer)

    def __delete_film(self, film):
        del self.__dictionary[film]
        self.__list_of_films.remove(film)

    def __edit_producer(self, producer, name, surname):
        index = self.__list_of_producers.index(producer)
        if index == -1:
            print "index -1!"
            return
        self.__list_of_producers[index].name = name
        self.__list_of_producers[index].surname = surname
        for key in self.__dictionary:
            if self.__dictionary[key] == producer:
                self.__dictionary[key] = self.__list_of_producers[index]

    def __edit_film(self, film, name, country, producer):
        index = self.__list_of_films.index(film)
        if index == -1:
            print "Index -1!"
            return
        self.__dictionary.pop(self.__list_of_films[index])
        self.__list_of_films[index].name = name
        self.__list_of_films[index].country = country
        self.__dictionary[self.__list_of_films[index]] = producer

    def __display_filmed_in_ukraine(self):
        list = []
        for key in self.__dictionary:
            if key.country == "Ukraine" and self.__dictionary[key] not in list:
                list.append(self.__dictionary[key])
        for producer in list:
            print producer

    def __have_films(self, producer):
        for key in self.__dictionary:
            if self.__dictionary[key] == producer:
                return 1
        return 0

    def __del__(self):
        pickle.dump(self.__list_of_films, open("films.txt", "wb"))
        pickle.dump(self.__list_of_producers, open("producers.txt", "wb"))
        pickle.dump(self.__dictionary, open("dictionary.txt", "wb"))
