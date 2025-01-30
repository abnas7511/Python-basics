# FloatingPointError is a built-in exception
try:
    float("abc")
except FloatingPointError:
    print("Invalid floating-point literal")