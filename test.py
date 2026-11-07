#IT Device Access Checker
"""* A device running Windows 11 is supported.
* Any other Windows version is unsupported.
* Supported devices receive network access.
* Unsupported devices are denied access."""

"""def check_device_support(os_version):
    if os_version == 11:
        return True
    else:
        return False

os_version = int(input("Enter the OS Version: "))

is_supported = check_device_support(os_version)

if is_supported == True :
    print("Network Access Granted")

else:
    print("Network Access Denied")"""

#Fuction Call 
def determine_priority(affected_users):
        if affected_users < 1:
            return "Invalid"

        elif affected_users <= 10:
            return "Low"

        elif affected_users <=50:
            return "Medium"

        else:
            return "High"


#Argument Variable      


#Main Flow
enter_ticket = "yes"

#counters for flow
total_valid_tickets = 0
high_priority_tickets = 0
escalations_required = 0

while enter_ticket == "yes":
    affected_users = int(input("Enter affected users: "))

    ticket_priority = determine_priority(affected_users)

    print(ticket_priority)

    #Escalation Flow Control 
    escalate = ticket_priority

    if escalate == "High":
        print("Escalation Required")
        high_priority_tickets = high_priority_tickets + 1
        escalations_required = escalations_required + 1

    elif escalate == "Invalid":
        print("Cannot Process Escalation")

    else:
        total_valid_tickets = total_valid_tickets + 1
        print("No Escalation Required")

    enter_ticket = input("Enter another ticket: ").lower()

    #print(ticket_priority)

"""A ticket must be escalated if its priority is "High".

All other priorities should not be escalated."""


#Summary Information 
print("===== HELPDESK SUMMARY =====")
print(f"Total Valid Tickets: {total_valid_tickets}")
print(f"High Priority Tickets: {high_priority_tickets}")
print(f"Escalations Required: {escalations_required}")

