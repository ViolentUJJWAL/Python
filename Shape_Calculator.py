def welcome():
	print('''
	 *       *  ******  *        *****   *****   *       *  ******
	 *       *  *       *       *       *     *  * *   * *  *
	 *       *  *       *       *       *     *  *  * *  *  *
	 *   *   *  *****   *       *       *     *  *   *   *  *****
	 *  * *  *  *       *       *       *     *  *       *  *
	 * *   * *  *       *       *       *     *  *       *  *
	 *       *  ******  ******   *****   *****   *       *  ******
	''')
def d2():
	print('''
           ****   ****
          *    *  *    *
              *   *     *
             *    *     *
            *     *     *
           *      *    *
          *****   ****
		''')
def d3():
	print('''
         ******  ****
             *   *    *
            *    *     *
           ***   *     *
              *  *     *
              *  *    *
         *****   ****
		''')
def exit():
	print('''
	  ******  *     *  *****  *******
	  *        *   *     *       *
	  *         * *      *       *
	  *****      *       *       *
	  *         * *      *       *
	  *        *   *     *       *
	  ******  *     *  *****     *
	''')
def back():
	print('''           

            <----------BACK

		''')
def pai():
	a=22/7
	return a

def mult(a,b):
	c=a*b
	return c
def add(a,b):
	c=a+b
	return c
def squ(a,b=2):
	c=a**b
	return c
def pair(a):
	c=pai()*a
	return c
def pairsq(a):
	d=a*a
	c=pai()*d
	return c
def eqtri(a):
	d=a*a
	e=pairsq(3,0.5)
	f=e/4
	c=e*d
	return c
def sub(a,b):
	c=a-b
	return c




welcome()
while True:
	print("Shape Calculater")
	st=int(input('''
		1. For 2D Shapes
		2. For 3D Shapes
		3. For show 2D and 3D Shapes
		4. For EXIT
		--->>>''' ))
	if st==1:                         #2D shapes
		d2()
		s2d=int(input('''
			1. >>> RECTANGLE
			2. >>> SQUARE
			3. >>> CIRCLE
			4. >>> SEMI-CIRCLE
			5. >>> TRIANGLE
			6. >>> PARALLELOGRAM
			7. >>> RHOMBUS
			8. BACK
			>>>>'''))
		if s2d==1:                            #rectangle
			print("RECTANGLE")
			l=eval(input("Lenght >"))
			b=eval(input("Breadth >"))
			op=eval(input('''
		1. find AREA
		2. find PERIMETER
		----'''))
			if op==1:
				area=mult(l,b)
				print("Area of RECTANGLE is ", area,"sq. unit")
			elif op==2:
				per=2*add(l,b)
				print("Perimeter of RECTANGLE is ", per,"unit")
			else:
				pass

		elif s2d==2:                           #square
			print("SQUARE") 
			a=eval(input("Side >"))
			op=int(input('''
		1. find AREA
		2. find PERIMETER
		----'''))
			if op==1:
				area=squ(a)
				print("Area of SQUARE is ", area,"sq. unit")
			elif op==2:
				per=4*a
				print("Perimeter of SQUARE is ", per,"unit")
			else:
				pass

		elif s2d==3:                           #circle
			print("CIRCLE")
			r=eval(input("Radius >"))
			op=int(input('''
		1. find AREA
		2. find Circumference
		----'''))
			if op==1:
				area=pairsq(r)
				print("Area of CIRCLE is ", area,"sq. unit")
			elif op==2:
				per=2*pair(r)
				print("Circumference of CIRCLE is ", per,"unit")
			else:
				pass

		elif s2d==4:                            #semi-circle
			print("SEMI-CIRCLE")
			r=eval(input("Radius >"))
			op=int(input('''
		1. find AREA
		2. find Circumference
		----'''))
			if op==1:
				area=pairsq(r)/2
				print("Area of SEMI-CIRCLE is ", area,"sq. unit")
			elif op==2:
				p=pair(r)
				r2=mult(r,2)
				per=add(p,r2)
				print("Circumference of SEMI-CIRCLE is ", per,"unit")
			else:
				pass

		elif s2d==5:                            #triangle
			print("TRIANGLE")
			tt=int(input('''
				Type of TRIANGLE
				1. EQUILATRAL TRIANGLE
				2. RIGHT-ANGLE TRIANGLE
				3. TRIANGLE WITH DIFFRENT SIDE
				---- '''))
			if tt==1:                           #EQUILATRAL TRIANGLE
				print("EQUILATRAL TRIANGLE")
				a=eval(input("Side >"))
				op=int(input('''
		1. find AREA
		2. find PERIMETER
		----'''))
				if op==1:
					area=eqtri(a)
					print("Area of EQUILATRAL TRIANGLE is ", area,"sq. unit")
				elif op==2:
					per=3*a
					print("Perimeter of EQUILATRAL TRIANGLE is ", per,"unit")
				else:
					pass

			elif tt==2:                        #RIGHT-ANGLE TRIANGLE
				print("RIGHT-ANGLE TRIANGLE")
				h=eval(input("height >"))
				b=eval(input("Base >"))
				op=int(input('''
		1. find AREA
		2. find PERIMETER
		----'''))
				if op==1:
					area=mult(h,b)/2
					print("Area of RIGHT-ANGLE TRIANGLE is ", area,"sq. unit")
				elif op==2:
					sq=squ(h)+squ(b)
					sq1=squ(sq,0.5)
					per=add(h,b)+sq1
					print("Perimeter of RIGHT-ANGLE TRIANGLE is ", per,"unit")
				else:
					pass

			elif tt==3:                  #TRIANGLE WITH DIFFRENT SIDE
				print("TRIANGLE WITH DIFFRENT SIDE")
				a=eval(input("1st Side >"))
				b=eval(input("2nd Side >"))
				c=eval(input("3rd Side >"))
				op=int(input('''
		1. find AREA
		2. find PERIMETER
		----'''))
				if op==1:
					sa=add(a,b)+c
					s=sa/2
					sa=sub(s,a)
					sb=sub(s,d)
					sc=sub(s,c)
					area=mult(s,sa)*mult(sb)
					farea=squ(area,0.5)
					print("Area of RIGHT-ANGLE TRIANGLE is ", farea,"sq. unit")
				elif op==2:
					per=add(a,b)+c
					print("Perimeter of RIGHT-ANGLE TRIANGLE is ", per,"unit")
				else:
					pass

			else:
				pass

		elif s2d==6:                                     #parallelogram
			print("PARALLELOGRAM")
			l=eval(input("Lenght >"))
			b=eval(input("Breadth >"))
			op=int(input('''
		1. find AREA
		2. find PERIMETER
		----'''))
			if op==1:
				area=mult(l,b)
				print("Area of PARALLELOGRAM is ", area,"sq. unit")
			elif op==2:
				per=2*add(l,b)
				print("Perimeter of PARALLELOGRAM is ", per,"unit")
			else:
				pass

		elif s2d==7:                                       #rhombas
			print("RHOMBUS")
			a=eval(input("Side >"))
			op=int(input('''
		1. find AREA
		2. find PERIMETER
		----'''))
			if op==1:
				area=squ(a)
				print("Area of RHOMBUS is ", area,"sq. unit")
			elif op==2:
				per=4*a
				print("Perimeter of RHOMBUS is ", per,"unit")
			else:
				pass

		elif s2d==8:                                        #back
			back()
			pass

		else:
			print("ERROR: {Only opretion with 1, 2, 3, 4, 5, 6 and 7}")

	elif st==2:
		d3()
		s3d=int(input('''
			1. >>> CUBE
			2. >>> CUBOID
			3. >>> CYLINDER
			4. >>> CONE
			5. >>> SPHERE
			6. >>> HEMI-SPHERE
			7. >>> FRUSTUM OF CONE
			8. BACK
			>>>>'''))
		if s3d==1:                                             #cube
			print("CUBE")
			a=eval(input("Side >"))
			op=int(input('''
		1. find Total Surface Area
		2. find Lateral Surface Area
		3. find Volume
		----'''))
			if op==1:
				tsa=6*squ(a)
				print(squ(a))
				print("Total Surface Area of CUBE is ", tsa,"sq. unit")

			elif op==2:
				lsa=4*squ(a)
				print("Lateral Surface Area of CUBE is ", lsa,"sq. unit")

			elif op==3:
				v=squ(a,3)
				print("Volume of CUBE is ", v,"cu. unit")

			else:
				back()
				pass

		elif s3d==2:                                           #cuboid
			print("CUBOID")
			l=eval(input("Length >"))
			b=eval(input("Breadth >"))
			h=eval(input("height >"))
			op=int(input('''
		1. find Total Surface Area
		2. find Lateral Surface Area
		3. find Volume
		----'''))
			if op==1:
				tsa=mult(l,b)+mult(b,h)+mult(h,l)
				ftsa=2*tsa
				print("Total Surface Area of CUBOID is ", ftsa,"sq. unit")

			elif op==2:
				lsa=2*add(l,b)*h
				print("Lateral Surface Area of CUBE is ", lsa,"sq. unit")

			elif op==3:
				v=mult(l,b)*h
				print("Volume of CUBOID is ", v,"cu. unit")

			else:
				back()
				pass

		elif s3d==3:                                              #cylinder
			print("CYLINDER")
			r=eval(input("Radius >"))
			h=eval(input("height >"))
			op=int(input('''
		1. find Total Surface Area
		2. find Lateral Surface Area
		3. find Volume
		----'''))
			if op==1:
				tsa=2*pair(r)
				ftsa=tsa*add(h,r)
				print("Total Surface Area of CYLINDER is ", ftsa,"sq. unit")

			elif op==2:
				lsa=2*pair(r)
				flsa=mult(lsa,h)
				print("Lateral Surface Area of CYLINDER is ", flsa,"sq. unit")

			elif op==3:
				v=pairsq(r)*h
				print("Volume of CYLINDER is ", v,"cu. unit")

			else:
				back()
				pass

		elif s3d==4:                                                  #cone
			print("CONE")
			r=eval(input("Radius >"))
			h=eval(input("height >"))
			rl=squ(r)+squ(h)
			l=squ(rl,0.5)
			print("l=",l)
			op=int(input('''
		1. find Total Surface Area
		2. find Lateral Surface Area
		3. find Volume
		----'''))
			if op==1:
				tsa=pair(r)*add(r,l)
				print("Total Surface Area of CONE is ", tsa,"sq. unit")

			elif op==2:
				lsa=pair(r)*l
				print("Lateral Surface Area of CONE is ", lsa,"sq. unit")

			elif op==3:
				v=pairsq(r)*h
				fv=v/3
				print("Volume of CONE is ", fv,"cu. unit")

			else:
				back()
				pass

		elif s3d==5:                                             #sphere
			print("SPHERE")
			r=eval(input("Radius >"))
			op=int(input('''
		1. find Total Surface Area
		2. find Volume
		----'''))
			if op==1:
				tsa=4*pairsq(r)
				print("Total Surface Area of SPHERE is ", tsa,"sq. unit")

			elif op==2:
				v=pairsq(r)*r
				d=4/3
				fv=d*v
				print("Volume of SPHERE is ", fv,"cu. unit")

			else:
				back()
				pass

		elif s3d==6:                                          #hemi-sphere
			print("HEMI-SPHERE")
			r=eval(input("Radius >"))
			op=int(input('''
		1. find Total Surface Area
		2. find Lateral Surface Area
		3. find Volume
		----'''))
			if op==1:
				tsa=pairsq(r)*3
				print("Total Surface Area of HEMI-SPHERE is ", tsa,"sq. unit")

			elif op==2:
				lsa=pairsq(r)*2
				print("Lateral Surface Area of HEMI-SPHERE is ", lsa,"sq. unit")

			elif op==3:
				v=pairsq(r)*r
				d=2/3
				fv=d*v
				print("Volume of HEMI-SPHERE is ", fv,"cu. unit")

			else:
				back()
				pass

		elif s3d==7:                                         #frustum of cone
			print("FRUSTUM OF CONE")
			r=eval(input("Big Radius >"))
			r1=eval(input("Small Radius >"))
			h=eval(input("height >"))
			ls=r-r1
			ls1=squ(ls)+squ(h)
			l=squ(ls1,0.5)
			print("l=",l)
			op=int(input('''
		1. find Total Surface Area
		2. find Lateral Surface Area
		3. find Volume
		----'''))
			if op==1:
				tsa1=pairsq(r)+pairsq(r1)
				tsa2=add(r,r1)*l
				tsa=pai()*tsa2
				ftsa=tsa+tsa1
				print("Total Surface Area of FRUSTUM OF CONE is ", ftsa,"sq. unit")

			elif op==2:
				lsa1=add(r,r1)
				lsa=pair(lsa1)*l
				print("Lateral Surface Area of FRUSTUM OF CONE is ", lsa,"sq. unit")

			elif op==3:
				v1=squ(r)+squ(r1)
				v2=r*r1
				v3=add(v1,v2)
				v4=pair(h)*v3
				v=v4/3
				print("Volume of FRUSTUM OF CONE is ", v,"cu. unit")


			else:
				back()
				pass

		elif s3d==8: #back
			back()
			pass

		else:
			print("ERROR: {Only opretion with 1, 2, 3, 4, 5, 6, 7 and 8}")


	elif st==3:
		d2()
		print('''
		1. >>> RECTANGLE
		2. >>> SQUARE
		3. >>> CIRCLE
		4. >>> SEMI-CIRCLE
		5. >>> TRIANGLE
		6. >>> PARALLELOGRAM
		7. >>> RHOMBUS
		''')

		d3()
		print('''
		1. >>> CUBE
		2. >>> CUBOID
		3. >>> CYLINDER
		4. >>> CONE
		5. >>> SPHERE
		6. >>> HEMI-SPHERE
		7. >>> FRUSTUM OF CONE
		''')

	elif st==4:
		exit()
		sc=input("yes/no (Y/N)-")
		if sc=="yes" or sc=="Y" or sc=="y":
			break
		elif sc=="no" or sc=="N" or sc=="n":
			pass
		else:
			print("error")

	else:
		print("error: {enter only 1, 2, 3 and 4}")
	