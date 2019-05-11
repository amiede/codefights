// https://app.codesignal.com/arcade/code-arcade/at-the-crossroads/r9azLYp2BDZPyzaG2
func knapsackLight(value1 int, weight1 int, value2 int, weight2 int, maxW int) int {
    
    // What a mess!
    if (weight1 + weight2) <= maxW {
        return value1 + value2;
    }
    if weight1 <= maxW {
        if value1 > value2 {
            return value1;
        } else if weight2 > maxW {
            return value1;
        }
    }
    if weight2 <= maxW {
        return value2;
    } else { 
        return 0; 
    }
       
}
