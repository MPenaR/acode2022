program solution
    use iso_fortran_env, only: iostat_end
    implicit none
    character(len=10) :: filename
    integer :: u, score,  io_code, l
    integer, parameter :: buffer_size = 100
    character(len=buffer_size) :: buffer 
    character(len=:), allocatable :: line 

    call get_command_argument(1,filename)

    open( file = filename, newunit = u, status = 'old', action='read')

    score = 0
    do 
        read(u,*, iostat=io_code) buffer
        select case(io_code)
        case(0)
            line = trim(buffer)     
            l = len(line)
            score = score + compute_score(find_common_letter(line(1:l/2),line(l/2+1:)))
            deallocate(line)
        case(iostat_end)
            exit
        end select
    end do 

    print*, score

contains
    function find_common_letter( left, right) result(common)
        character(len=*), intent(in) :: left, right
        character(len=1) :: common
        integer :: i, j 

        outer : do i = 1,len(left)
                    do j=1,len(right)
                        if ( left(i:i) == right(j:j) ) exit outer
                    end do 
                end do outer
        common = left(i:i)
    end function

    function compute_score(letter) result(score)
        character(len=1), intent(in) :: letter 
        integer :: score 

        if ( (iachar(letter) >= iachar('A') ) .and. (iachar(letter) <= iachar('Z') ) ) score = iachar(letter) - iachar('A') + 27
        if ( (iachar(letter) >= iachar('a') ) .and. (iachar(letter) <= iachar('z') ) ) score = iachar(letter) - iachar('a') + 1

    end function 
end program 