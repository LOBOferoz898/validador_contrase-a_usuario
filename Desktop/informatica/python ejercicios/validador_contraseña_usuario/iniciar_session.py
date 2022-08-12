import modulo_validar as m_v

op = 0
registros = m_v.Registros()
while op != 3:

    op = m_v.menu()

    if op == 1:
        name_user = input("Ingrese nombre de usuario: ")
        pass_user = input("Ingrese contraseña: ")

        iniciar = False
        for (name,password) in zip(registros.Nomb_Users,registros.password_users):
            if name == name_user and password == pass_user:
                iniciar = True
            
        if iniciar:
            print("\nSe inicio session correctamente\n")
        else:
            print("\nUsuario no registrado\n")
    
    elif op == 2:
        name_user = input("Ingrese nombre de usuario: ")

        val = True
        while val:
            pass_user = input("Ingrese contraseña: ")
            pass_user2 = input("Confirme la contraseña: ")

            if pass_user == pass_user2:
                val = False
            else:
                print("\n(Confirmacion invalida): Ambas contraseñas deben ser iguales. Reintente...\n")
        
        usuario = m_v.Usuario(name_user,pass_user)

        registros = m_v.Registros(usuario)
        registros.registrar()
    else:
        print("\nADIOS\n")







            


