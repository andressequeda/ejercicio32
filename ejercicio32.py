year  =  int ( input ( "Ingrese un año:" ))
si  año  %  4  ==  0  y ( año  %  100  ! =  0  o  año  %  400  ==  0 ):
    print ( "El año es bisiesto" )
otra cosa :
    print ( "El año no es bisiesto" )