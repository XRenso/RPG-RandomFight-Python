import random


class City(object):
    def __init__(self, name):
        self.name = name
        self.paths = []
    def init_path(self,paths):
        self.paths.extend(paths)

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
                for i in range(number_cities):
                    path = random.randint(1,len(cities)-1)
                    path_citis = []
                    edit_citis = []
                    edit_citis.extend(cities)
                    edit_citis.remove(cities[i])
                    for j in range(path):
                        choice = random.choice(edit_citis)
                        path_citis.append(choice)
                        edit_citis.remove(choice)

                    cities[i].init_path(path_citis)

if __name__ == '__main__':
    Map(20,0)
    for i in cities:
        paths = []
        for j in i.paths:
            paths.append(j.name)
        print(f'city - {i.name} \npaths - {paths}')