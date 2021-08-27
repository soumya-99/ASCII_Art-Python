import math, cmath, numpy, 
z = 3 + 4j
print(type(z))

print(f"Conjugate of {z} is : {z.conjugate()}") # conjugate
print(f"Modulas of {z} is : {abs(z)}") # modulas

# Creating complex numbers:
z1 = complex(2, 3)
print("Real part: ", z1.real)
print("Imaginary part: ", z1.imag)

print(f"The phase angle of {z1} (in radian) is {cmath.phase(z1)}")
print(f"The phase angle of {z1} (in degree) is {numpy.degrees(cmath.phase(z1))}")