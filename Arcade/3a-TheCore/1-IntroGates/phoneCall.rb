# https://app.codesignal.com/arcade/code-arcade/intro-gates/mZAucMXhNMmT7JWta/
def phoneCall(min1, min2_10, min11, s)
    
    minute = 1
    
    while true do
        
        cost = 0
        
        case minute         
        when 1
                cost = min1
        when 2..10
                cost = min2_10
        else
                cost = min11
        end
        
        s -= cost 
                   
        if s < 0 then
                return minute -1
        elsif s == 0 then
                return minute
        end
        
        minute += 1
                
    end
           
end
