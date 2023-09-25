import sys

class MenuConsole:

    def menu_option(self):
        print("""
Menu
1. Iniciar")
2. Salir
                    """)
    
    def election_option(self):
        self.menu_option()
        eleccion = int(input("Opcion: "))

        if eleccion == 1:
            pass

        if eleccion == 2:
            sys.exit()