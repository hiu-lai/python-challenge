import os
import csv

# Define source file location and name
readfile = os.path.join("resources", "budget_data.csv")

# Define output file location and name
outputfile = os.path.join("analysis", "budget_analysis.txt")

datecol = []
# P & L value
plval = []

# P & L changes between months
plvar = []

with open(readfile, "r") as budget_datafile:
    csvreader = csv.reader(budget_datafile, delimiter=',')
    csv_header = next(csvreader)

    # Loop file and load columns into list
    for row in csvreader:
        datecol.append(row[0])
        plval.append(int(row[1]))
    sumplval = "${:.0f}".format(sum(plval))
    countmth = len(datecol)

    # Rows comparison to calculate changes between each data rows
    # i being current row and j being the next row
    for i in range(len(plval)):
           for j in range(i + 1, i + 2): # loop range between current row and next next row to ensure it does not go past data table
               if (i + 2) <= len(plval):
                    plvar.append(plval[j] - plval[i])
    sumplvar = sum(plvar)/len(plvar)
    sumplvar = "${:.2f}".format(sumplvar)

    # Greatest Increase Calc
    maxIncrease = max(plvar)
    maxIncreaseIndex = plvar.index(maxIncrease) + 1
    maxIncreaseMonth = datecol[maxIncreaseIndex]
    maxIncrease = "${:.0f}".format(max(plvar))

    # Greatest Decrease Calc
    minDecrease = min(plvar)
    minDecreaseIndex = plvar.index(minDecrease) + 1
    minDecreaseMonth = datecol[minDecreaseIndex]
    minDecrease = "${:.0f}".format(min(plvar))

    # Uniform output
    line01Text = "Financial Analysis"
    lineBreak = "-------------------------------------------"
    line02Text = f"Total Months: {countmth}"
    line03Text = f"Total: {sumplval}"
    line04Text = f"Average Change: {sumplvar}"
    line05Text = f"Greatest Increase in Profits: {maxIncreaseMonth} ({maxIncrease})"
    line06Text = f"Greatest Decrease in Profits: {minDecreaseMonth} ({minDecrease})"


    # Print output to screen
    print(line01Text)
    print(lineBreak)
    print(line02Text)
    print(line03Text)
    print(line04Text)
    print(line05Text)
    print(line06Text)

# Write output to file 
with open(outputfile, "w") as btext:
    btext.write(line01Text + '\n')
    btext.write(lineBreak + '\n')
    btext.write(line02Text + '\n')
    btext.write(line03Text + '\n')
    btext.write(line04Text + '\n')
    btext.write(line05Text + '\n')
    btext.write(line06Text + '\n')
# End 