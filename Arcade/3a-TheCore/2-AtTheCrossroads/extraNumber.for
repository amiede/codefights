! https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/sgDWKCFQHHi5D3Szj/
function extraNumber(a, b, c) result(res)
    implicit none
    integer(4) :: a
    integer(4) :: b
    integer(4) :: c
    integer(4) :: res
    
    if (a == b) then 
        res = c
    else if (a == c) then
        res = b
    else 
        res = a
    end if
    
end function extraNumber