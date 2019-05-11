// https://app.codesignal.com/arcade/intro/level-1/s5PbmwxfECC52PWyQ/
bool checkPalindrome(char * inputString) {
    int l = strlen(inputString);
    for(int i = 0; i < l/2; i++)
        if(inputString[i] != inputString[l - 1 - i])
            return false;
    return true;
}