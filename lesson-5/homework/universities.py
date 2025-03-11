def enrollment_stats(uni_list):
    overall_student = 0
    overall_fees = 0
    for i in uni_list:
        overall_fees += i[2]
        overall_student += i[1]

    return [overall_student, overall_fees]


def mean(uni_list):
    mean1 = 0
    mean2 = 0
    for i in uni_list:
        mean1 += i[1]
        mean2 += i[2]
    mean1 = mean1 / len(uni_list)
    mean2 = mean2 / len(uni_list)
    return [mean1, mean2]


def mediann(uni_list):
    median_student = 0
    median_fee = 0
    s_list = []
    f_list = []

    for i in uni_list:
        s_list.append(i[1])
        f_list.append(i[2])

    s_list.sort()
    f_list.sort()

    median_student = (
        s_list[len(s_list) // 2 + 1]
        if len(s_list) % 2 == 1
        else (s_list[len(s_list) // 2] + s_list[len(s_list) // 2 + 1]) // 2
    )
    median_fee = (
        f_list[len(f_list) // 2 + 1]
        if len(f_list) % 2 == 1
        else (f_list[len(f_list) // 2] + f_list[len(f_list) // 2 + 1]) // 2
    )

    return [median_student, median_fee]


num = int(input("Enter number of universities: "))
univer_list = []
for i in range(num):
    a = input(f"Enter a name of {i+1}-university: ")
    b = int(input("Enter the total number of enrolled students: "))
    c = int(input("Enter the annual tuition fees: "))
    univer_list.append([a, b, c])

result1 = enrollment_stats(univer_list)

overall_mean = mean(univer_list)
overall_median = mediann(univer_list)


print("******************************")
print(
    f"Total students: {format(result1[0],",")}\nTotal tuition: ${format(result1[1],",")}\n\n"
)

print(
    f"Student mean: {overall_mean[0]:,.2f}\nStudent median: {format(overall_median[0],",")}"
)

print(
    f"Tuition  mean: {overall_mean[1]:,.2f}\nTuition  median: {format(overall_median[1],",")}"
)
print("******************************")
