program solution
    use games
    use iso_fortran_env, only: iostat_end
    implicit none

    character(len=32) :: filename 
    integer :: u, total_score, io_code
    character(len=1) :: me_code, you_code, part 
    type(game), allocatable :: g
    

    call get_command_argument(1,filename)
    call get_command_argument(2,part)
    
    open(file=filename, newunit = u, status = 'old', action = 'read')

    select case( part )
    case('1')
        do
            read(unit=u, fmt=*, iostat=io_code) you_code, me_code
            select case( io_code)
            case(0)
                g = game_from_code_1(you_code, me_code)
                total_score = total_score + g%score()
            case(iostat_end)
                exit
            end select
        end do
    case('2')
        do
            read(unit=u, fmt=*, iostat=io_code) you_code, me_code
            select case( io_code)
            case(0)
                g = game_from_code_2(you_code, me_code)
                total_score = total_score + g%score()
            case(iostat_end)
                exit
            end select
        end do
    end select 

    close(u)

    print '(A,A,A,I0)', "Part ", part, ", total score: ", total_score
    
end program solution