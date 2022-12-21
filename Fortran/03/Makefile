FC = gfortran -c
FL = gfortran 

solution : solution.o
	$(FL) $^ -o $@

solution.o : solution.f90
	$(FC) $< 
