#student grade calculator
subjects=int(input("how many subjects ? "))
total_marks=0
for i in range(subjects):
    marks=int(input(f"enter marks for subject {i+1}  : "))
    total_marks+=marks
#sum_marks=sum(total_marks)
print(f"total marks  : {total_marks} ")
average_marks=total_marks/2
print(f"average marks : {average_marks}")
if 10<=total_marks<=30:
    print("Grade : F , FAIL")
elif 40<=total_marks<=50:
    print("Grade B , do better")
elif 60<=total_marks<=80:
    print("Grade A , well done")
else:
    print("Grade A+ , Excellent")

