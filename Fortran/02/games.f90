module games
    implicit none 

    type :: game
        integer :: you
        integer :: me
    contains
        procedure :: score => game_score
    end type game 

    contains 

    function game_score( self ) result(score)
        class(game), intent(in) :: self 
        integer :: score 
        score = self%me + 1 + 3*modulo( self%me - self%you + 1, 3 )
    end function 

    function game_from_code_1(you_code, me_code) result(g)
        character(len=1), intent(in) :: you_code, me_code
        type(game) :: g
        integer :: you, me 
        you = iachar(you_code) - iachar('A')
        me = iachar(me_code) - iachar('X')
        g = game(you, me)
    end function

    function game_from_code_2(you_code, me_code) result(g)
        character(len=1), intent(in) :: you_code, me_code
        type(game) :: g
        integer :: you, me 
        you = iachar(you_code) - iachar('A')
        me = modulo( you + iachar(me_code) - iachar('Y'), 3 )
        g = game(you, me )
    end function
    
end module