

def valid_attempts (failed_attemtps):
    if failed_attemtps < 0:
        return False

    else:
        return True

failed_attempts = int(input("Enter failed login attempts: "))
is_valid = valid_attempts(failed_attempts)


def check_account_status (failed_attempts, account_permission):
    if failed_attempts < 0 :
        print("Invalid Number")
        

    elif account_permission == "yes":
        if failed_attempts <= 1:
            print("Account Normal")

        else:
            print("Account Locked")

    elif failed_attempts <= 2:
        print("Account Normal")

    elif failed_attempts <= 4:
        print("Warning")

    else:
        print("Account Locked")



account_permission = input("Is this a priviledged/admin account: ").lower().strip()

valid_attempts(failed_attempts)
check_account_status(failed_attempts,account_permission)