print("""
    -----------FIZZ BUZZ GAME-----------
    ---------IF A NUMBER IS 3 OR DIVISIBLE BY 3 THEN IT PRINT FIZZ------
    ---------IF A NUMBER IS 5 OR DIVISIBLE BY 5 THEN IT PRINT BUZZ------
    ---------IF A NUMBER IS DIVISIBLE OF BOTH 3 AND 5 THEN IT PRINT FIZZBUZZ-----

""")

for i in range(1, 101):
    if i%3==0 and i%5 ==0:
        print(f"{i} Fizzbuzz")
    if i%3 ==0 and i%5 !=0:
        print(f" {i} Fizz")
    if i%5 ==0 and i%3!=0:
        print(f"{i} Buzz")
