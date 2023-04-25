import random


class City(object):
    def __init__(self, name):
        self.name = name
        self.paths = []
    def init_path(self,index_paths):
        self.paths.extend(index_paths)
        print(self.paths)
    def get_stat(self,need):
        match need:
            case 'name':
                return self.name
cities = []
class Map(object):
    def __init__(self, number_cities,difficult):
        match difficult:
            case 0:
                for i in range(number_cities):
                    cities.append(City('Joja' + str(i)))
                for i in range(len(cities)-1):
                    path = random.randint(1,len(cities)-1)
                    path_citis = []
                    edit_citis = cities
                    for j in range(path):
                        choice = random.choice(edit_citis)
                        path_citis.append(choice)
                        edit_citis.remove(choice)
                    print(i)
                    cities[i].init_path(path_citis)

Map(3,0)
print([i.name for i in cities])