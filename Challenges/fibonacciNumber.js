// https://app.codesignal.com/challenge/hTvQiQuJTk9bSvY6n
// https://medium.com/@johanna.fulghum/write-the-fibonacci-sequence-in-every-computational-complexity-9adf5ef12775
function fibonacciNumber(n) {
  [a, b] = [0, 1]
  while (n > 0){
    [a, b] = [b, a + b]
    n -= 1
  }
  return a
}


// Tail recursion version
/*
function fib(n, a = 0, b = 1){
  if (n > 0) {
    return fib(n - 1, b, a + b)
  }
  return a
}
*/