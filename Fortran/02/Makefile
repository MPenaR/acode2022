FC= gfortran -c 
FL= gfortran 

%.o : %.mod

solution: solution.o games.o
	$(FL) $^ -o $@

%.o: %.f90
	$(FC) $<
	
