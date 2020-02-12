input = open("purchases.txt", "r")
out = open("01.txt", "w")

for line in input:
    datalist = line.strip().split("    ")
    date, time,store, item, cost, paymentType = datalist
    out.write(paymentType + "\t" + "1" + "\n")

input.close()
out.close()