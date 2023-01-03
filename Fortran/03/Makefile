FC = gfortran -c
FL = gfortran 

solution : solution.o sets.o
	$(FL) $^ -o $@

solution.o : solution.f90
	$(FC) $< 

test : test_sets.o sets.o 
	$(FL) $^ -o $@

test_sets.o : test_sets.f90 sets.o
	$(FC) $< 

sets.o : sets.f90 
	$(FC) $<