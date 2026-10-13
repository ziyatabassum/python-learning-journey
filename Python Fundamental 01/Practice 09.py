'''Ask the user for: Principal (P), Rate (R), Time (T). Convert all to float and
compute simple interest: SI = (P ∗ R ∗ T)/100'''

#Let, invested $10000 for 3 years at a 4% annual rate

P = float(input("Enter the Principle: "))
R = float(input("Enter the Annual Rate: "))
T = float(input("Enter the Time: "))

float_P = float(P)
float_R = float(R)
float_T = float(T)

SI = (float_P * float_R * float_T) /100

print(f"Simple Interest is: ", SI)