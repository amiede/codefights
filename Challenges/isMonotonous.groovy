// https://app.codesignal.com/challenge/Bbr2AGZQw2CHofuao
// Trying Groovy for the first time ;-\
boolean isMonotonous(List<Integer> S) {
    
    int s = S.size()
    
    if (s == 1) return 1

    // direction: < 0 (inc), 0 (eq), > 0 (dec)
    int d = S.get(0) - S.get(1) 
    
    for (i in 0..s-2) {
        
        // change in direction makes result negative (no inc/dec --> 0)
        if (d * (S.get(i) - S.get(i+1)) <= 0) return 0
        
    }
    
    return 1
}