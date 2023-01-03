module sets
    implicit none 

    private

    public :: char_set, operator(<=), operator(>=), operator(+), operator(*) 

    integer, parameter :: N_letters =  iachar('Z') - iachar('A') + 1 
    integer :: i 
    character(len=1), parameter :: UpperCase(N_letters) = [ ( achar(i + iachar('A')-1), i=1, N_letters ) ]
    character(len=1), parameter :: LowerCase(N_letters) = [ ( achar(i + iachar('a')-1), i=1, N_letters ) ]
    character(len=1), parameter :: ReverseHashTable(2*N_letters) = [UpperCase, LowerCase ]

    
    type char_set
        private
        logical :: contained( 2*N_letters ) = .false. 
    contains 
        procedure :: contains => is_in
        procedure :: size => number_of_elements
        procedure :: to_array => set_to_array
    end type 


    interface char_set
        module procedure set_from_string
    end interface


    interface operator(<=) 
        module procedure is_subset
    end interface

    interface operator(>=) 
        module procedure is_superset
    end interface

    interface operator(*) 
        module procedure intersection
    end interface

    interface operator(+) 
        module procedure union
    end interface


    contains 

    elemental function hash_char( char ) result( idx )
        character(len=1), intent(in) :: char
        integer :: idx 

        if ( ( iachar(char) >= iachar('A') ) .and. ( iachar(char) <= iachar('Z') ) ) then
            idx = iachar(char) - iachar('A') + 1
        else if ( ( iachar(char) >= iachar('a') ) .and. ( iachar(char) <= iachar('z') ) ) then
            idx = iachar(char) - iachar('a') + N_letters + 1
        end if 

    end function 

    elemental function reverse_hash_char( idx ) result( char )
        integer, intent(in) :: idx
        character(len=1) :: char  

        char = ReverseHashTable(idx)
    end function 


    function set_from_string( string ) result(S)
        character(len=*), intent(in) :: string
        type(char_set) :: S
        integer :: l, i, idx

        l = len(string)
        do i = 1, l
            idx = hash_char(string(i:i))
            S%contained(idx) = .true.
        end do 
    end function 


    function set_to_array( self ) result(array)
        class(char_set), intent(in) :: self
        character(len=1) :: array(self%size())
        array = pack( ReverseHashTable, self%contained )
    end function 


    elemental function is_in( self, char ) result( contained )
        class(char_set), intent(in) :: self 
        character(len=1), intent(in) :: char 
        logical :: contained
        
        contained = self%contained(hash_char(char))
        
    end function 

    pure function number_of_elements( self ) result(N) 
        class(char_set), intent(in) :: self 
        integer :: N 
        N = count(self%contained)
    end function 

    function is_subset(A, B) result( A_in_B )
        type(char_set), intent(in) :: A, B 
        logical :: A_in_B
        type(char_set) :: C
        C = A * B 
        A_in_B = C%size() == A%size()
    end function 

    function is_superset(A, B) result( A_in_B )
        type(char_set), intent(in) :: A, B 
        logical :: A_in_B
        type(char_set) :: C
        C = A * B 
        A_in_B = C%size() == B%size()
    end function 

    function intersection(A, B) result( A_and_B )
        type(char_set), intent(in) :: A, B 
        type(char_set) :: A_and_B
        A_and_B%contained = A%contained .and.  B%contained
    end function 

    function union(A, B) result( A_or_B )
        type(char_set), intent(in) :: A, B 
        type(char_set) :: A_or_B
        A_or_B%contained = A%contained .or.  B%contained
    end function 


end module sets