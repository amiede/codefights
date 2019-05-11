// https://app.codesignal.com/arcade/code-arcade/intro-gates/aiKck9MwwAKyF8D4L
int lateRide(int n) {
    int m = n % 60;
    int h = n / 60;
    
    return (h % 10 + h ~/ 10 + m % 10 + m ~/ 10).toInt();
     
}