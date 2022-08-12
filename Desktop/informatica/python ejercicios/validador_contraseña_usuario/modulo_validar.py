class Usuario:
    def __init__(self,nomb_usuario,contraseña):
        self.nomb_usuario = nomb_usuario
        self.__contraseña = contraseña

    @property
    def contraseña(self):
        return self.__contraseña

    @contraseña.setter
    def contraseña(self,contrseña):
        self.__contraseña = contrseña

    def ValNomb(self):
        cant_caract = len(self.nomb_usuario)
        if cant_caract >= 6 and cant_caract <= 12:
            cont_let = 0
            cont_num = 0
            cont_otro = 0

            for i in self.nomb_usuario:
                if i.lower() in "abcdefghijklmnñopqrstuvwxyz":
                    cont_let += 1
                elif i in "0123456789":
                    cont_num += 1
                else:
                    cont_otro += 1
                
            if cont_let > 0 and cont_num > 0 and cont_otro == 0:
                return True
            else:
                print("El nombre de usuario debe contener solo letras y numeros")

        elif cant_caract < 6:
            print("El nombre de usuario debe contener al menos 6 caracteres")
        
        elif cant_caract > 12:
            print("El nombre de usuario no puede contener más de 12 caracteres")
        
    def ValContraseña(self):
        cant_caract = len(self.__contraseña)
        if cant_caract == 8:
            letras_min = "abcdefghijklmnñopqrstuvwxyz"
            letras_may = letras_min.upper()
            cont_let_Min = 0
            cont_let_May = 0
            cont_num = 0
            cont_otro = 0
            for c in self.__contraseña:
                if c in letras_min:
                    cont_let_Min += 1
                elif c in letras_may:
                    cont_let_May += 1
                elif c in "0123456789":
                    cont_num += 1
                elif c in " ":
                    espacio = True
                else:
                    cont_otro += 1
            
            if cont_let_Min >= 1 and cont_let_May >= 1 and cont_num >= 1 and cont_otro >= 1:
                return True

            elif espacio:
                print("La contraseña no debe contener espacios en blanco")
            
            else:
                print("(CONTASEÑA INVALIDA): la contraseña debe contener letras minúsculas, mayúsculas, números y al menos 1 carácter no alfanumérico")


class Registros:
    Nomb_Users = []
    password_users = []
    def __init__(self,usuario = None):
        self.usuario = usuario
    
    def registrar(self):
        if isinstance(self.usuario,Usuario):
            if self.usuario.ValNomb() and self.usuario.ValContraseña():
                self.Nomb_Users.append(self.usuario.nomb_usuario)
                self.password_users.append(self.usuario.contraseña)
            else:
                print("La contraseña o nombre del usuario es invalido")
        else:
            print("El usuario debe ser instancia de la clase Usuario")


def menu():
    val = True
    while val:
        try:
            op = int(input("QUE DESEA HACER?\n(1) INICIAR SESSION\n(2) REGISTRARSE\n(3) SALIR\nINGRESE AQUI --> "))
            if op >= 1 and op <= 3:
                val = False
                return op
            else:
                raise Exception("(OPCION INVALIDA): La opcion debe estar dentro de la opciones que se presentan en el menu, y este debe estar representado en un numero entero. reintente...")
        except Exception as e:
            print(e)


