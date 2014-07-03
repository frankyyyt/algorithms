prob1 n = [ x | x <- [1..n-1], (x `mod` 3 == 0 || x `mod` 5 == 0)]
numbers = prob1 1000
answer = sum numbers
