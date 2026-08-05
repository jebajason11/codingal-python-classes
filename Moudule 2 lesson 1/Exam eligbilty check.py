medical_cause = input("Do you have a medical cause Y/N"). strip(). upper()

if medical_cause == "Y":
    print("You can take the exam")

else:
    atten = int (input("Enter the attendace of the student"))
    if atten >= 75 :
        print("Allowed")
    else:
        print("Not allowed")
