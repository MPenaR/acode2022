FC= gfortran -c 
FL= gfortran 

%.o : %.mod

solution: solution.o 
	$(FL) $^ -o $@

%.o: %.f90
	$(FC) $<