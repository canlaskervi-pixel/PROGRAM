print("=======================================================")
print("           🐍INTERACTIVE PYTHON TUTORIAL               ")
print("=======================================================")

while True:
    print(" 📗 PRELIMS LESSON ")
    print("1. INTRODUCTION ")
    print("2. What is Programming ")
    print("3. Python Print Syntax ")
    print("4. Python Comments ")
    print("5. Variables and Data Types ")
    print("6. Arithmetic Operators ")

    print(" 📘MIDTERM LESSON ")
    print("7. Input Function ")
    print("8. f-String ")
    print("9. Conditional Statement ")

    print(" 📕FINAL LESSON ")
    print("10. Looping ")
    print("0. Exit ")

    choices = int(input("Enter your Choice. (0-10) :"))
    if choices ==0:
        break #exit if the loop is entered 0
    if choices ==1:
        print ("INTRODUCTION")
        print ("Python is a versatile, high-level, and beginner-friendly programming language")
        print ("used for a wide range of applications ")
        print ("like web development, data science, and automation.")
        print ("It is known for its readable syntax ")
        print ("that emphasizes simplicity and allows for rapid development. ")
        print ("EXAM:")
        print ("Hello, World")
    elif choices==2:
        print ("What is Programming")
        print ("Programming is the process of writing instructions, called code,")
        print ("that tell a computer what to do to solve a problem or perform a task.")
        print ("It involves designing and implementing algorithms, ")
        print ("which are step-by-step procedures, using a specific programming language. ")
        print ("This code allows people to create software, applications, websites,")
        print ("and systems that enable the technology we use every day,")
        print ("from mobile apps to complex business software.")
    elif choices ==3:
        print ("Print syntax is the specific set of rules used to instruct a program to display output, ")
        print (" which varies depending on the programming language.")
        print ("EXAMPLE:")
        print ("Hello", "world", sep="-")
    elif choices ==4:
        print("Python Comments ")
        print ("Comments are used to explain sections of code,")
        print ("clarify complex logic, or describe the purpose of variables, functions,or classes.")
        print (" This makes the code easier to understand for both the original author")
        print ("(when revisiting the code later) and other developers.")
    elif choices ==5:
        print ("Variables and Data Types")
        print ("Variables are named containers for storing data, while data types")
        print ("are categories that define the kind of data a variable can hold")
        print ("and what operations can be performed on it.")
        print ("For example, a variable named age could be an integer data type")
        print ("to store a whole number, or a variable named name")
        print ("could be a string data type to store text. ")
    elif choices ==6:
        print ("Arithmetic Operators")
        print ("Python supports arithemetic operators")
        print ("like + (add), - (subtract), * (multiply), / (divide)")
        print ("// (floor division), % (modulus), and ** (exponentiation).")
    elif choices ==7:
        print ("Input Function")
        name = input ("Enter your name:")
        print ("Hello," + name + "!")
        age_str = input ("Enter your age:")
        age =int(age_str)## converter the string to an integer
        print ("You are",age,"Years old.")
    elif choices ==8:
        print ("f-String")
        txt = f"the price is 49 dollars"
        print (txt)
    elif choices ==9:
        print("Conditional Statement ")
        score = 75
        if score >= 90:
            print ("Grade: A")
        elif score >=80:
            print ("Grade: B")
        elif score >=70:
            print ("Grade: C")
        elif score >=60:
            print ("Grade: D")
        else:
            print ("Grade: F")
    elif choices ==10:
        print ("Looping in Python programming refers to the repeated execution of a block of code.")
        print ("This repetition continues until a specified condition is met or ")
        print ("or each item in a sequence. ")
        print ("Loops are fundamental control flow statements that enable efficient and")
        print ("concise code by avoiding redundant code writing.")

        print ("Example of a for Loop")
        for i in range (1,6):
            print (f"  Counting: {i}")

            print ("Example of a while loop:")
            count = 1
            while count <= 5:
                print (f"  Counting: {count}")
                count += 1









