import threedfigures

print("1. Cylinder")
print("2. Cone")
print("3. Cuboid")

choice = int(input("Enter your choice: "))

if choice == 1:
    r = float(input("Enter radius: "))
    h = float(input("Enter height: "))
    print("CSA =", threedfigures.cylinder_csa(r, h))
    print("TSA =", threedfigures.cylinder_tsa(r, h))
    print("Volume =", threedfigures.cylinder_volume(r, h))

elif choice == 2:
    r = float(input("Enter radius: "))
    h = float(input("Enter height: "))
    l = (r*r + h*h) ** 0.5
    print("CSA =", threedfigures.cone_csa(r, l))
    print("TSA =", threedfigures.cone_tsa(r, l))
    print("Volume =", threedfigures.cone_volume(r, h))

elif choice == 3:
    l = float(input("Enter length: "))
    b = float(input("Enter breadth: "))
    h = float(input("Enter height: "))
    print("CSA =", threedfigures.cuboid_csa(l, b, h))
    print("TSA =", threedfigures.cuboid_tsa(l, b, h))
    print("Volume =", threedfigures.cuboid_volume(l, b, h))

else:
    print("Invalid choice")