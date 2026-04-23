test1=int(input("Enter your score of first 1"))
test2=int(input("Enter your score second test"))
main_exam=int(input("Enter the number of your main exam"))

if 50>=main_exam>=0 and 25>=test2>=0 and 25>=test1>=0:
    total=test1+test2+main_exam
    if total<50 and main_exam<25:
        print("fail")
    else:
        if total>=80:
            print("Distinction")
        elif 80>total>=60:
            print("Credit")
        else:
            print("pass")
else:
    print("An erro")



