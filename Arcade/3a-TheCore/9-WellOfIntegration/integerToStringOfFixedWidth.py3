# https://app.codesignal.com/arcade/code-arcade/well-of-integration/kvGfZZxGyjNbD7yxv
def integerToStringOfFixedWidth(number, width):
    
    s = str(number)
    l = len(s)
       
    return s.zfill(width) if width > l else s[l-width:] if width < l else s
    
    '''if width > l:
        s = s.zfill(width)
    
    elif width < l:
        s = s[l-width:]
    
    return s'''
	
	
# Solution by burkh4rt
#def integerToStringOfFixedWidth(number, width):
#    return str(number).zfill(width)[-width:]	