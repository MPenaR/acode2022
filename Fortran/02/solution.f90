program solution
    use games
    use iso_fortran_env, only: iostat_end
    implicit none

    character(len=32) :: filename 
    integer :: u, total_score, io_code
    character(len=1) :: me_code, you_code
    type(game), allocatable :: g

    call get_command_argument(1,filename)
    open(file=filename, newunit = u, status = 'old', action = 'read')

    do
        read(unit=u, fmt=*, iostat=io_code) you_code, me_code
        select case( io_code)
        case(0)
            g = game_from_code(you_code, me_code)
            total_score = total_score + g%score()
        case(iostat_end)
            exit
        end select
    end do

    close(u)

    print '(A,I0)', "Part 1, total score: ", total_score
    
end program solution