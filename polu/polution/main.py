from socio import socio
from trafique import trafique
from météo import météo
from particule import particule
from climat import climat


from variable import METEO

class main:

    def météologie(self):
        météo.recuperation_donnée(self, 'paris', METEO)
        print(METEO)


if __name__ == '__main__':

    main = main()
    main.météologie()
