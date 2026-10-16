#Employee  Access Checker Design 
# check two values of an employee if both value are true grant access if not deny access
"""As such I need to find a way to do the following:
1st have an employee variable
2nd assocaiate values with that employee
3rd read the values of those assocated values
4th compare values against standards 
5th allow or deny access based on compared values"""
#Day 1 of reps complete

#Day 2 Reps
"""Have the user input the information using the input() function and then evaluate the users access to the system. """

"""1. Ask for the employee’s name.
2. Ask whether the employee is active.
3. Ask whether security training is complete.
4. Grant access only when both answers are yes.
5. Otherwise deny access.
6. Include the employee’s name in the result.
"""
employee = input("What's your name?: ")
employee_active = input("Are you an active employee?: ").lower()
security_training_complete = input("Have you completed security training?: ").lower()

if employee_active == "yes" and security_training_complete == "yes":
    print(employee + ": Access Granted")
else:
    print(employee + ": Access Denied")
