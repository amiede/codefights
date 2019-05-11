sub circleOfNumbers {
	my ($n, $firstNumber) = @_;
    return ($n / 2 + $firstNumber) % $n;
}
