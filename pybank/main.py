import os
import csv

readfile = os.path.join("resources", "budget_data.csv")
outputfile = os.path.join("analysis", "budget_analysis.csv")

datecol = []
plval = []

with open(readfile, "r") as budget_datafile:
    csvreader = csv.reader(budget_datafile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        datecol.append(row[0])
        plval.append(int(row[1]))
    sumplval = "${:.0f}".format(sum(plval))
    countmth = len(datecol)

    print("Finacial Analysis")
    print("-------------------------------------------")
    print(f"Total Months: {countmth}")
    print(f"Total: {sumplval}")

with open(outputfile, "w", encoding="UTF8") as budget_analysisfile:
    writer = csv.writer(budget_analysisfile)
    writer.writerow(["Financial Analysis"])
    writer.writerow(["Total Months:", countmth])
    writer.writerow(["Total:", sumplval])

