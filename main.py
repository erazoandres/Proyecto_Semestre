def todo():
	#Funciones

	def aviso():

		#Ventana emerguente que aparecera en el momento en el que el usuario halla perdido sus 3 vidas.

		ventanaAviso = Tk()
		ventanaAviso.title('Que deseas hacer ?')

		aviso = Label(ventanaAviso, text="Perdiste :(\n Intentar de nuevo ?", width=40, height=10, bg = "light cyan") #Etiqueta de aviso
		aviso.pack() #Blitear aviso

		botonSalir = Button(ventanaAviso, text="Lo intentare de nuevo", command= ventanaAviso.destroy) # Destruir la ventana para continuar jugando
		botonContinuar = Button(ventanaAviso, text = "Quiero irme..", command = None) # Destruye la ventana principal del juego para salir.

		botonSalir.place(  x = 50, y = 120)
		botonContinuar.place( x = 180, y = 120)

		ventanaAviso.mainloop()
	def randomColor():

			#Esta funcion retorna un color de la lista
			color = ["red", "blue" , "white" , "pink" , "yellow", "gray", "orange", "purple", "chartreuse", "firebrick" , "purple1", "SkyBlue2","gold2","sienna1"]

			indiceRandom = random.randint(0,len(color)-1) # genero un indice de la lista aleatorio - rango : 0, #Tamñ lista -1 (para no sobrepasar la lista)
			colorRandom = color[indiceRandom] # Variable que encapsula el color
			return colorRandom # Retorna el    		# Color aleatorio para los objetos.
	def loadBotones():
		starGame = Button(capaMain , text = "Empieza !", command = shootBall , bg = "purple" , highlightbackground = "SkyBlue2" , relief = GROOVE ) 
		starGame.place(x = 435 , y =  10)			# Corregir el command 
	def saveUserInText():

		print(entryLabel.get())
		#-Guardando Informacion Usuario-#

		# Importacion del archivo, si no existe este se creará
		file = open("userDates.txt","w+")

		labelShowUser = Label(capaMain, text="Usuario", bg="VIOLET", relief= GROOVE ).place(x = 232, y = 340)
		entryLabel = Entry(root)

		continueMenu = Button(root , text = "Continuar...", command = borrar , bg = "red", relief = GROOVE).place(x = 220, y = 400)

		def borrar(obj):

			print(entryLabel.get())		#Falta por implementar
	def shootBall():

		x1pel, y1pel, x2pel, y2pel = capaMain.coords(Pelota['widg'])
		overPelota = capaMain.find_overlapping(x1pel, y1pel, x2pel, y2pel) #Retorna ID de objeto con el que colision
		print(overPelota)
		
		#Limites de paredes
			
		if x1pel < 10:					#limite con eje x(0)
			
			Pelota["x"] *= - 1
			Pelota["y"] -= 0.5 
			
		elif x2pel > 490:				#Limite con ejex(700)
			
			Pelota["x"] *= - 1
			Pelota["y"] -= 0.5 
		elif y2pel < 10 :				#Limite con eje y (0)
			
			Pelota["y"] *= - 1
			Pelota["y"] -= 0.5 

		

		capaMain.move(Pelota["widg"],Pelota["x"],Pelota["y"])
		root.after(35,shootBall)			#Disparar la bola
	def loadEnemiesStatics():

		
		Colores = randomColor()

		#Obstaculos
		enemies = {
				"rombo1": capaMain.create_polygon(130,300,130,400,200,420,fill = "yellow"),
				"rombo2": capaMain.create_polygon(370,300,370,400,290,420 ,fill ="yellow"),
				"triangulo": capaMain.create_polygon(590,700,590,500,510,450,fill="orange"),
				"lateral1": capaMain.create_polygon((0,700),(100,700),(0,600), fill = "RED"),
				"lateral2": capaMain.create_polygon((400,700),(500,700),(500,600), fill = "chartreuse"),
				"lateral3" : capaMain.create_polygon((0,0,),(0,100,),(100,0), fill = "deep sky blue"),
				"lateral4" :capaMain.create_polygon((400,0),(500,0),(500,100), fill = "purple"),

				"tamborUp": capaMain.create_oval(230,50,260,80, fill = Colores),
				"tamborDown": capaMain.create_oval(230,120,260,150, fill = Colores),
				"tamborLef": capaMain.create_oval(180,90,200,110, fill = Colores),
				"tamborRight": capaMain.create_oval(290,90,310,110, fill = Colores),
				
				}	#Carga el diccionario con todos los obstaculos estaticos.
	def moverPaletas(event):




	    global paletaIz,paletaDer,paletaIzA, paletaDerA
	    x1pel, y1pel, x2pel, y2pel = capaMain.coords(Pelota['widg'])
	    overPelota = capaMain.find_overlapping(x1pel, y1pel, x2pel, y2pel) #Retorna ID de objeto con el que colisionv
	    

	    if overPelota != (1,):
	    	Pelota["y"] *= -1


	    
	    tecla1 = repr(event.char)
	    tecla2 = repr(event.char)


	    #Audicion de paleta IZQUIERDA
	    if (tecla1 == "'q'"):

	        capaMain.delete(paletaIz) 
	        capaMain.delete(paletaIzA)    

	        
	        paletaIz = capaMain.create_polygon((120,650),(120,630),(200,580),(200,590),fill="red")
	        paletaIzA  = capaMain.create_polygon((150,350),(140,370),(220,350),(220,340),  fill = "yellow")

	        capaMain.update()
	        capaMain.delete(paletaIz , paletaIzA)

	        time.sleep(0.10)
	        paletaIz  = capaMain.create_polygon((120,630),(120,650),(200,680),(200,670),fill="blue", outline = "white")
	        paletaIzA  = capaMain.create_polygon((150,350),(140,370),(220,400),(220,390),  fill = "yellow")
	        tornilloIzquierdo = capaMain.create_oval(110,620,150,660, fill = "red" , outline = "white")

	    # Aucion de paleta DERECHA
	    if (tecla2 == "'a'"):

	        capaMain.delete(paletaDer)
	        capaMain.delete(paletaDerA)

	        paletaDer = capaMain.create_polygon((270,590),(270,580),(350,630),(350,650),fill="green", outline = "white")
	        tornilloDerecho = capaMain.create_oval(330,620,370,660, fill = "red" , outline = "white")
	        paletaDerA = capaMain.create_polygon((260,350),(260,360),(350,370),(350,350) , fill = "yellow")

	      

	        capaMain.update()
	        capaMain.delete(paletaDer,paletaDerA)


	        time.sleep(0.10)
	        paletaDer = capaMain.create_polygon((270,680),(270,670),(350,630),(350,650),fill="blue", outline = "white")
	        paletaDerA = capaMain.create_polygon((260,390),(260,400),(350,370),(350,350) , fill = "yellow")	# Falta por documentar
	        tornilloDerecho = capaMain.create_oval(330,620,370,660, fill = "red" , outline = "white")	#Movimiento de palestas y colisiones
	def potencia():
		i = 0.1
		potencia = random.randrange(0,2)
		for i in range(1,100):
			potencia -= i 				#Potencia de disparo
	def enemigosMoviles():

		xIz,yIz,x2Iz,y2Iz = capaMain.coords(moviles["barraIZ"]) #cuatro cordenadas de los objetos moviles
		moviles["y2Iz"]  += 1	
		capaMain.move(moviles["barraIZ"], 0 , moviles["y2Iz"])
		capaMain.update()

		root.after(1000, enemigosMoviles)		#Cargar diccionario que contiene los obstaculos y puntuadores moviles.

	#Ventana Principal 
	root = Tk()
	root.geometry("500x700-450-30")
	root.title('Pin Ball Future ! - By: Andres Erazo')
	capaMain = Canvas(root,bg = "Black" ,  width = 500, height = 700) #Canvas fondo de la ventana princial
	capa2= Canvas(root,bg = "red" ,  width = 500, height = 700) #Canvas fondo de la ventana princial



	#-Background Menu-#
	#loadGroundMenu = PhotoImage(file="backMenu.png")
	#capaMain.create_image(0,0, image = loadGroundMenu, anchor = NW)


	#Diccionario que contiene los atributos de la pelota y objetos moviles
	Pelota = { "x": 10 , "y": 10 , "widg": capaMain.create_oval(50,10,70,30, fill="WHITE")}
	moviles = {"barraIZ" : capaMain.create_rectangle(10,100,20,120, fill = "BLUE"),"xIz": 10,"y2Iz": 120,
			   "barraDER": capaMain.create_rectangle(490,570,500,590, fill = "gold2")}  			



	#Paletas

		# Paletas Bajas
	paletaIz  = capaMain.create_polygon((150,630),(140,650),(220,680),(220,670),  fill = "blue", outline = "white")
	paletaDer = capaMain.create_polygon((260,680),(260,670),(350,630),(350,650) , fill = "blue", outline = "white")

		# Paletas Altas
	paletaIzA  = capaMain.create_polygon((150,350),(140,370),(220,400),(220,390),  fill = "yellow")
	paletaDerA = capaMain.create_polygon((260,390),(260,400),(350,370),(350,350) , fill = "yellow")

		# Tornillo de paletas
	tornilloIzquierdo = capaMain.create_oval(110,620,150,660, fill = "red" , outline = "white")
	tornilloDerecho = capaMain.create_oval(330,620,370,660, fill = "red" , outline = "white")


	#Llamado a funciones y eventos.

	loadEnemiesStatics() 						#Carga de obstaculos
	loadBotones()								#Carga todos los botones del juego.													
	#enemigosMoviles()				 			#Cargando Puntuadores Moviles
	root.bind("<Key>",moverPaletas)		        #Audicion de teclas
	root.resizable(0,0)							#Reajuste de ventana False - (width=False,height=False)
	capaMain.pack()		     					#Empaquetando atributos de widgt para blitear.
	potencia = 1
	root.mainloop()								#Ejecucion de evento principal (Tk())