# BUILDING A LOG MONTITORING AND ANALYSIS SYSTEM TO IDENTFY SUSPICIOUS LOGIN ATTEMPTS


# Use lists  to create a collection of stored login records 
# use for loops to review authentication records of the company.
# use while loops to identify and monitor suspicious login attempts. The login attempts must not exceed 3
# Use if statements to print true of false login attempts
AUTHENTICATION_RECORD = ["berakah@123", "admin@123"]
for AUTH_RECORD in AUTHENTICATION_RECORD:
    print(AUTH_RECORD)
print("=" * 65)
print(f"                    LOG MONITORING AND ANALYSIS SYSTEM")
print("=" * 65)


LOG_ATTEMPT = 0
LOGIN_ATTEMPT = 3
while LOG_ATTEMPT < LOGIN_ATTEMPT:
    USER_NAME = input("Enter your username: ")
    LOG_ATTEMPT += 1
    if USER_NAME == AUTHENTICATION_RECORD:
        print("You have been granted access !!!")
        break

    else:
        print("You have been blocked !!!")
