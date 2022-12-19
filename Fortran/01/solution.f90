program solution
    use, intrinsic :: iso_fortran_env, only: iostat_end
    implicit none

    integer :: u, io_code, current_elf, item 
    integer :: elf1, elf2, elf3
    character(len=6) :: line
    character(len=32) :: filename

    call get_command_argument(1, filename )
    
    open( file = trim(filename), newunit=u, status='old', action='read')

    current_elf = 0
    elf1 = 0
    elf2 = 0
    elf3 = 0
    do
        read( unit = u, fmt = '(A)', iostat=io_code) line
        select case (io_code) 
        case(0)
            if (line  == '') then
                call update_head( elf1, elf2, elf3, current_elf)
                current_elf = 0
            else
                read( line, * ) item
                current_elf = current_elf + item  
            end if
        case(iostat_end)
            exit
        end select 
    end do
    call update_head( elf1, elf2, elf3, current_elf)
    
    print '(A,I0)', 'Solution to part 1: ', elf1
    print '(A,I0," + ",I0," + ",I0," = ",I0)', 'Solution to part 2: ', elf1, elf2, elf3, sum( [ elf1, elf2, elf3 ] )
 
 contains

    subroutine update_head( first, second, third, current)
        !> updates the record of the 3 higher item counts
        integer, intent(inout) :: first, second, third
        integer, intent(in) :: current 
            if ( current > first ) then
                third = second
                second = first 
                first = current
            else if ( current < first ) then
                if ( current > second ) then
                    third = second
                    second = current
                else if (current < second ) then
                    third = max(current, third)
                end if 
            end if              
    end subroutine

end program solution
