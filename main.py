coef = {"english": [0.5, 0.3, 0.2]}

def bprint(*n, sep=' ', end='\n'):
    for i in n:
        if type(i) is float:
            print(f"{i:.2f}", end=sep)
        else:
            print(i, end=sep)
    print(end)

def calc_total_average(subject, k, f, t):
    total = k * coef[subject][0] + f * coef[subject][1] + t * coef[subject][2]
    return total

def calc_averages(res):
    avg_k = avg_f = avg_t = count_k = count_f = count_t = 0

    for i in res:
        if i[1] == 'f':
            count_f += 1
            avg_f += i[0]
        if i[1] == 'k':
            count_k += 1
            avg_k += i[0]
        if i[1] == 't':
            count_t += 1
            avg_t += i[0]

    avg_k /= count_k
    avg_f /= count_f
    avg_t /= count_t

    return avg_k, avg_f, avg_t

subject = input("Please input subject  ").lower()
mode = input("Select mode: fromready/raw  ")
if mode == 'fromready':
    k = float(input("Please input average konst mark  "))
    f = float(input("Please input average form mark  "))
    t = float(input("Please input average creative mark  "))

    bprint(calc_total_average(subject, k, f, t))
elif mode == "raw":
    res = []
    print("Please input numbers in format of 5k 4f 5t 5f and so on  ")
    raw = input().split()
    for i in raw:
        res.append((int(i[0]), i[1]))

    # res.sort(key= lambda x: x[1])

    k, f, t = calc_averages(res)

    bprint("Average konst:", k,
           "Average form:", f,
           "Average creative:", t,
           "Total:", calc_total_average(subject, k, f, t))
    while True:
        print("Do you want to change a mark and see what happens? y/n")
        ans = input().lower()
        if ans == 'n':
            print("Bye then!")
            break
        elif ans == 'y':

            print("Input what mark to change in format of 2k")
            mark = input()
            i = res.index((int(mark[0]), mark[1]))
            if i:
                print("Mark found! Enter new value in format of 5k")
                new_mark = input()
                res[i] = (int(new_mark[0]), new_mark[1])
                k, f, t = calc_averages(res)
                print("For marks", *res, "here are averages:")

                bprint("Average konst:", k,
                       "Average form:", f,
                       "Average creative:", t,
                       "Total:", calc_total_average(subject, k, f, t))

# 5f 5f 0k 5f 4k 5t 5t 4f 5f 5k 5t 5f 5k 4k