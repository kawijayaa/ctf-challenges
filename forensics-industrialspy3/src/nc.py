q1 = input("1. What ports are open on the attacked machine? (ex: 1,2,3,4)\n")
if set(q1.split(",")) != {'22', '5432'}:
    print("Incorrect.")
    exit()

q2 = input("2. What is the credentials used to access the database? (ex: root:root)\n")
if q2 != "server:changeme":
    print("Incorrect.")
    exit()

q3 = input("3. What is the password for the \"super\" user on the database?\n")
if q3 != "cafecoagroindustrialdelpacfico":
    print("Incorrect.")
    exit()

q4 = input("4. What table does the attacker modify?\n")
if q4 != "penalties":
    print("Incorrect.")
    exit()

q5 = input("5. It seems that the attacker has modified their own data, what is their full name?\n")
if q5 != "Lyubov Pryadko":
    print("Incorrect.")
    exit()

print()
print("Thank you for submitting your report. We will review it and get back to you as soon as possible.")
print("COMPFEST16{t00_3z_3vEN_f0R_4N_1ntErn_abdfe98ce2}")
