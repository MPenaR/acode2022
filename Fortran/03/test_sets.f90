program test_sets
    use sets
    implicit none
 
    type(char_set) :: S1, S2, S3
   
    S1 = char_set('Manuel')
    S2 = char_set('Pena')
    S3 = S1 * S2
    print*, S1%to_array()
    print*, S2%to_array()
    print*, S3%to_array()
    print*, S1 >= S2
    

end program