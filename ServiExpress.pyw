from tkinter import *
from tkinter import messagebox

raiz=Tk()

varOpcion=IntVar()

def agendar():
        raiz.geometry("623x277")
        ventana = Toplevel(raiz)
        ventana.title("Agenda")
        etiqueta = Label(ventana,text="Detalles de la cita: ", bg="black", fg="white").pack()
        
        diaLabel = Label(ventana, text="Dia: ").pack()
        cuadroDia = Entry(ventana).pack()
        
        mesLabel = Label(ventana, text="Mes: ").pack()
        cuadroMes = Entry(ventana).pack()
        
        nombreLabel = Label(ventana, text="Nombre del evento: ").pack()
        cuadroNombre = Entry(ventana).pack()

        servicio_solicitadoLabel = Label(ventana, text="Servicio Solicitado: ").pack()
        cuadroServicio_Solicitado = Entry(ventana).pack()

        informacionLabel = Label(ventana, text="Información del evento: ").pack()
        cuadroInformacion = Entry(ventana).pack()

        def cita_agendada():
            valor=messagebox.askokcancel("ServiExpress","¿Está seguro de agendar esta cita?")
            if valor==True:
                messagebox.showinfo("ServiExpress","¡Su cita fue programada con exito!")
                raiz.destroy()
    
        Button(ventana, text="Listo", bg="black", fg="white", command=cita_agendada).pack()

        ventana.resizable(0,0)
        ventana.geometry("300x300")
        ventana.transient(raiz)
        
def enviar_mensaje():

        raiz.geometry("623x277")
        ventana = Toplevel(raiz)
        ventana.title("Mensajeria")
        etiqueta = Label(ventana,text="Ingrese un mensaje: ", bg="black", fg="white").pack()
       
        remitenteLabel = Label(ventana, text="Remitente: ").pack()
        cuadroRemitente = Entry(ventana).pack()
        
        destinarioLabel = Label(ventana, text="Destinario: ").pack()
        cuadroDestinario = Entry(ventana).pack()

        mensajeLabel = Label(ventana, text="Mensaje: ").pack()
        cuadroMensaje = Entry(ventana).pack()

        def mensaje_enviado():
            valor=messagebox.askokcancel("ServiExpress","¿Está seguro que desea enviar el mensaje?")
            if valor==True:
                messagebox.showinfo("ServiExpress","¡Su mensaje fue enviado!")
                raiz.destroy()
                
        Button(ventana, text="Listo", bg="black", fg="white", command=mensaje_enviado).pack()

        ventana.resizable(0,0)
        ventana.geometry("300x200")
        ventana.transient(raiz)
        
def mostrar_notificaciones():
    messagebox.showinfo("ServiExpress","Sin notificaciones disponibles.")

def infoApp():
    messagebox.showinfo("Acerca de...", "Aplicacion para Servicios a Domicilio. Version 2020")

def infoCreador():
    messagebox.showinfo("Info", "Creador: Angela Romero 27650409- rusher1508@gmail.com - 0424-8836001 - Influido por: Python 3.7.4")

def salirApp():
    valor=messagebox.askokcancel("Salir", "¿Está seguro que desea salir de la aplicacion?")
    
    if valor==True:
        raiz.destroy()

def iniciar_sesion():
    
    Label(raiz, text="Iniciar Sesion", bg="black", fg="white").pack()
    
    usuarioLabel = Label(raiz, text="Usuario: ").pack()
    cuadroUsuario = Entry(raiz).pack()
        
    claveLabel = Label(raiz, text="Clave: ").pack()
    cuadroClave = Entry(raiz, show="*").pack()

    def entrar():
    
        messagebox.showinfo("ServiExpress","Te hemos echado de menos,¡Bienvenido otra vez!")
        raiz.geometry("623x277")      
    
    Button(raiz, text="Entrar", bg="black", fg="white", command=entrar).pack()

def registrarse():
    
    Label(raiz, text="Tipo de usuario: ", bg="black", fg="white").pack()

    Radiobutton(raiz, text="Cliente", variable=varOpcion, value=1, command=registrarse).pack()

    Radiobutton(raiz, text="Servicio", variable=varOpcion, value=2, command=registrarse).pack()

    etiqueta1=Label(raiz)
    etiqueta1.pack() 
    
    if varOpcion.get()==1:

        raiz.geometry("623x277")
        ventana = Toplevel(raiz)
        ventana.title("Cliente")
        etiqueta = Label(ventana,text="Ingrese sus datos: ", bg="black", fg="white").pack()
        
        nombreLabel = Label(ventana, text="Nombre: ").pack()
        cuadroNombre = Entry(ventana).pack()
        
        apellidoLabel = Label(ventana, text="Apellido: ").pack()
        cuadroApellido = Entry(ventana).pack()
        
        ubicacionLabel = Label(ventana, text="Ubicacion: ").pack()
        cuadroUbicacion = Entry(ventana).pack()
        
        codigo_postalLabel = Label(ventana, text="Codigo postal: ").pack()
        cuadroCodigo_postal = Entry(ventana).pack()
        
        telefonoLabel = Label(ventana, text="Telefono: ").pack()
        cuadroTelefono = Entry(ventana).pack()
        
        correoLabel = Label(ventana, text="Correo: ").pack()
        cuadroCorreo = Entry(ventana).pack()
        
        usuarioLabel = Label(ventana, text="Usuario: ").pack()
        cuadroUsuario = Entry(ventana).pack()
        
        claveLabel = Label(ventana, text="Clave: ").pack()
        cuadroClave = Entry(ventana, show="*").pack()

        def cliente_registrado():
            messagebox.showinfo("Bienvenido a ServiExpress","¡Sus datos fueron registrado con exito!")
    
        Button(ventana, text="Registrar", bg="black", fg="white", command=cliente_registrado).pack()

        ventana.resizable(0,0)
        ventana.geometry("300x400")
        ventana.transient(raiz)
                
    elif varOpcion.get()==2:

        raiz.geometry("623x277")
        ventana = Toplevel(raiz)
        ventana.title("Servicio")
        etiqueta = Label(ventana,text="Ingrese sus datos: ", bg="black", fg="white").pack()
        nombreLabel = Label(ventana, text="Nombre: ").pack()
        cuadroNombre = Entry(ventana).pack()

        tipoLabel = Label(ventana, text="Tipo de Sevicio: ").pack()
        cuadroTipo = Entry(ventana).pack()

        ubicacionLabel = Label(ventana, text="Descripcion: ").pack()
        cuadroUbicacion = Entry(ventana).pack()

        ubicacionLabel = Label(ventana, text="Ubicacion: ").pack()
        cuadroUbicacion = Entry(ventana).pack()
        
        codigo_postalLabel = Label(ventana, text="Codigo postal: ").pack()
        cuadroCodigo_postal = Entry(ventana).pack()
        
        telefonoLabel = Label(ventana, text="Telefono: ").pack()
        cuadroTelefono = Entry(ventana).pack()
        
        correoLabel = Label(ventana, text="Correo: ").pack()
        cuadroCorreo = Entry(ventana).pack()
        
        usuarioLabel = Label(ventana, text="Usuario: ").pack()
        cuadroUsuario = Entry(ventana).pack()
        
        claveLabel = Label(ventana, text="Clave: ").pack()
        cuadroClave = Entry(ventana, show="*").pack()

        def servicio_registrado():
            messagebox.showinfo("Bienvenido a ServiExpress","¡Sus datos fueron registrado con exito!")
    
        Button(ventana, text="Registrar", bg="black", fg="white", command=servicio_registrado).pack()

        ventana.resizable(0,0)
        ventana.geometry("400x450")
        ventana.transient(raiz)
        
    else:
        etiqueta1.destroy()


def configurar():
    Label(raiz, text="Opciones de Configuracion", bg="black", fg="white").pack()
    check1 = Checkbutton(raiz, text="Notificaciones", variable=1).pack()
    check2 = Checkbutton(raiz, text="Mostrar Ubicacion", variable=2).pack()
    check3 = Checkbutton(raiz, text="Sonido", variable=3).pack()
    check4 = Checkbutton(raiz, text="Recibir", variable=4).pack()

    def configuracion_lista():
        valor=messagebox.askokcancel("ServiExpress","¿Está seguro que desea esa configuracion?")
        if valor==True:
            messagebox.showinfo("ServiExpress","¡Configuración exitosa!")
            raiz.destroy()

        Button(raiz, text="Listo", bg="black", fg="white", command=configuracion_lista).pack()

def servicio_albanileria():

        raiz.geometry("623x277")
        ventana = Toplevel(raiz)
        
        ventana.title("Servicio de Albañileria")
        
        ventana.config(bg="green")

        Label(ventana, text="¿En que consiste?").pack()
        
        Label(ventana, text="Este servicio ofrece la construcción y restauración de muros, paredes, monumentos y diferentes partes del hogar. Permitiendo crear estructuras,  revestimientos, estucados, yesos en paredes, frescos, colocación de mármol, granito, instalaciones de tubería y sistemas de calefacción", justify = CENTER, wraplength = 300).pack()
    
        Button(ventana, text="Salir", bg="black", fg="white", command=salirApp).pack()

        ventana.resizable(0,0)
        ventana.geometry("300x150")
        ventana.transient(raiz)

def servicio_animacion():

        raiz.geometry("623x277")
        ventana = Toplevel(raiz)
        
        ventana.title("Servicio de Animacion")
        
        ventana.config(bg="red")

        Label(ventana, text="¿En que consiste?").pack()
        
        Label(ventana, text="Este servicio ofrece desde los clásicos payasos de los cumpleaños infantiles hasta los teatros de marionetas, pintacaritas y magos, así como se enfoca en mantener entretenidos a los más pequeños también está la parte de presentaciones musicales y temáticas para bodas, comuniones o bautizos.", justify = CENTER, wraplength = 300).pack()
    
        Button(ventana, text="Salir", bg="black", fg="white", command=salirApp).pack()

        ventana.resizable(0,0)
        ventana.geometry("300x150")
        ventana.transient(raiz)

def servicio_bartender():

        raiz.geometry("623x277")
        ventana = Toplevel(raiz)
        
        ventana.title("Servicio de Bartender")
        
        ventana.config(bg="green")

        Label(ventana, text="¿En que consiste?").pack()
        
        Label(ventana, text="Este servicio ofrece un personal preparado para la elaboración de bebidas con licencia detrás de una barra a los clientes. Dónde se incluyen tragos, cervezas, vino, coctelería y shots. Además estos preparan sus propias bebidas de autor y pueden hacer espectáculo, si se trata de un flair bartender.", justify = CENTER, wraplength = 300).pack()
    
        Button(ventana, text="Salir", bg="black", fg="white", command=salirApp).pack()

        ventana.resizable(0,0)
        ventana.geometry("300x150")
        ventana.transient(raiz)
        
def servicio_decoracion():

        raiz.geometry("623x277")
        ventana = Toplevel(raiz)
        
        ventana.title("Servicio de Decoracion")
        
        ventana.config(bg="orange")

        Label(ventana, text="¿En que consiste?").pack()
        
        Label(ventana, text="Este servicio ofrece la mejor experiencia en la creación de ambientes en eventos sociales, por medio de nuestros servicios de decoración. Dónde se ambientará un espacio de forma temática, caracterizada por las necesidades y gustos de los clientes implementando técnicas de nuestros servicios de decoración contaremos con la mejor iluminación, escenografía, arreglos florales.", justify = CENTER, wraplength = 300).pack()
    
        Button(ventana, text="Salir", bg="black", fg="white", command=salirApp).pack()

        ventana.resizable(0,0)
        ventana.geometry("300x180")
        ventana.transient(raiz)

def servicio_gastronomico():

        raiz.geometry("623x277")
        ventana = Toplevel(raiz)
        
        ventana.title("Servicio Gastronomico")
        
        ventana.config(bg="green2")

        Label(ventana, text="¿En que consiste?").pack()
        
        Label(ventana, text="Este servicio ofrece personal capacitado con un conjunto de técnicas, medios y sesiones que se le ofrecen al cliente relacionados con la restauración y alimentación en bodas, fiestas, tertulias, comunión o cumpleaños. Dónde contamos con el servicio de cocina tipo buffet y familiar, además de la atención de un grupo de mesoneros que se encargarán de las necesidades de los clientes durante la velada.", justify = CENTER, wraplength = 300).pack()
    
        Button(ventana, text="Salir", bg="black", fg="white", command=salirApp).pack()

        ventana.resizable(0,0)
        ventana.geometry("300x180")
        ventana.transient(raiz)

def servicio_guarderia():

        raiz.geometry("623x277")
        ventana = Toplevel(raiz)
        
        ventana.title("Servicio de Guarderia")
        
        ventana.config(bg="blue")

        Label(ventana, text="¿En que consiste?").pack()
        
        Label(ventana, text="Este servicio ofrece facilitar el desarrollo integral de niños y niñas. dónde la guardería debe ser un entorno, al igual que la familia, rico en relaciones, oportunidades y retos, que dé respuesta a sus necesidades y amplíe y diversifique las experiencias vividas en su contexto familiar. Un lugar donde jugar, relacionarse con otros niños, disfrutar de espacios y materiales especialmente pensados ​​para ellos, actividades y propuestas educativas, claves para fomentar su desarrollo.", justify = CENTER, wraplength = 300).pack()
    
        Button(ventana, text="Salir", bg="black", fg="white", command=salirApp).pack()

        ventana.resizable(0,0)
        ventana.geometry("300x200")
        ventana.transient(raiz)
        
def servicio_jardineria():

        raiz.geometry("623x277")
        ventana = Toplevel(raiz)
        
        ventana.title("Servicio de Jardineria")
        
        ventana.config(bg="green")

        Label(ventana, text="¿En que consiste?").pack()
        
        Label(ventana, text="Este servicio es capaz de garantizar el aspecto y la salud de árboles, plantas y flores. Ya que suelen aportar una estética perfecta a casas privadas, comunidades y urbanizaciones. La vida vegetal es ideal para que acompañe en el día a día o que mejore considerablemente una vivienda o bloque de viviendas.", justify = CENTER, wraplength = 300).pack()
    
        Button(ventana, text="Salir", bg="black", fg="white", command=salirApp).pack()

        ventana.resizable(0,0)
        ventana.geometry("300x150")
        ventana.transient(raiz)
        
def servicio_limpieza():

        raiz.geometry("623x277")
        ventana = Toplevel(raiz)
        
        ventana.title("Servicio de Limpieza")
        
        ventana.config(bg="red")

        Label(ventana, text="¿En que consiste?").pack()
        
        Label(ventana, text="Este servicio ofrece un personal que atienda tareas puntuales como limpieza por fin de construcción, limpieza profunda de hogar, suelos, azulejos, ventanas, persianas, paredes, cocina, patios y muebles. Además de aseo antes y después de fiestas particulares o eventos sociales, como bodas.", justify = CENTER, wraplength = 300).pack()
    
        Button(ventana, text="Salir", bg="black", fg="white", command=salirApp).pack()

        ventana.resizable(0,0)
        ventana.geometry("300x150")
        ventana.transient(raiz)

def servicio_mantenimiento():

        raiz.geometry("623x277")
        ventana = Toplevel(raiz)
        
        ventana.title("Servicio de Mantenimiento")
        
        ventana.config(bg="green")

        Label(ventana, text="¿En que consiste?").pack()
        
        Label(ventana, text="Este servicio ofrece el mantenimiento del área de la cocina la reparación así como la instalación de piezas, mantenimiento de tipo preventivos y correctivos a aires acondicionados, lavadoras, secadoras, televisores, ventiladores, entre otros aparatos eléctricos que conforman el  hogar y darle mas vida útil a su inversión.", justify = CENTER, wraplength = 300).pack()
    
        Button(ventana, text="Salir", bg="black", fg="white", command=salirApp).pack()

        ventana.resizable(0,0)
        ventana.geometry("300x150")
        ventana.transient(raiz)


def servicio_plomeria():

        raiz.geometry("623x277")
        ventana = Toplevel(raiz)
        
        ventana.title("Servicio de Plomeria")
        
        ventana.config(bg="light blue")

        Label(ventana, text="¿En que consiste?").pack()
        
        Label(ventana, text="Este servicio ofrece personal capacitado para la instalación, mantenimiento y reparación de tuberías, así como revisión y arreglo de filtraciones y desagües dentro de el hogar proporcionando soluciones a los clientes para su calidad de vida óptima en sus hogares.", justify = CENTER, wraplength = 300).pack()
    
        Button(ventana, text="Salir", bg="black", fg="white", command=salirApp).pack()

        ventana.resizable(0,0)
        ventana.geometry("300x150")
        ventana.transient(raiz)
  
        

        
    
raiz.title("ServiExpress")

raiz.resizable(0,0)

raiz.config(bg="white")

miFrame=Frame(raiz, width=623, height=277)

miFrame.config(bg="white")

miFrame.config(bd=35)

miFrame.pack()

miImagen=PhotoImage(file="logo.png")

Label(raiz, image=miImagen).place(x=0, y=0)

menuOpciones=Menu(raiz)
raiz.config(menu=menuOpciones, width=623, height=277)
raiz.config(cursor="hand2")

archivoInicio=Menu(menuOpciones, tearoff=0, bg="black", fg="white")
archivoInicio.add_command(label="Agenda", command=agendar)
archivoInicio.add_command(label="Mensajeria", command=enviar_mensaje)
archivoInicio.add_command(label="Notificaciones", command=mostrar_notificaciones)
archivoInicio.add_separator()
archivoInicio.add_command(label="Salir", command=salirApp)

archivoUsuario=Menu(menuOpciones, tearoff=0, bg="black", fg="white")
archivoUsuario.add_command(label="Iniciar Sesion", command=iniciar_sesion)
archivoUsuario.add_command(label="Registrarse", command=registrarse)
archivoUsuario.add_separator()
archivoUsuario.add_command(label="Configuracion", command=configurar)
archivoUsuario.add_separator()

archivoServicios=Menu(menuOpciones, tearoff=0, bg="black", fg="white")
archivoServicios.add_command(label="Albañileria", command=servicio_albanileria)
archivoServicios.add_command(label="Animación", command=servicio_animacion)
archivoServicios.add_command(label="Bartender", command=servicio_bartender)
archivoServicios.add_command(label="Decoración", command=servicio_decoracion)
archivoServicios.add_command(label="Gastronómico", command=servicio_gastronomico)
archivoServicios.add_command(label="Guarderia", command=servicio_guarderia)
archivoServicios.add_command(label="Jardineria", command=servicio_jardineria)
archivoServicios.add_command(label="Limpieza", command=servicio_limpieza)
archivoServicios.add_command(label="Mantenimiento", command=servicio_mantenimiento)
archivoServicios.add_command(label="Plomeria", command=servicio_plomeria)

archivoAyuda=Menu(menuOpciones,tearoff=0, bg="black", fg="white")
archivoAyuda.add_command(label="Info", command=infoCreador)
archivoAyuda.add_command(label="Acerca de...", command=infoApp)

menuOpciones.add_cascade(label="Inicio", menu=archivoInicio)

menuOpciones.add_cascade(label="Usuario", menu=archivoUsuario)

menuOpciones.add_cascade(label="Servicios", menu=archivoServicios)

menuOpciones.add_cascade(label="Ayuda", menu=archivoAyuda)

raiz.mainloop()
