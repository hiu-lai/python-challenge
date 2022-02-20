from cgitb import text
import os
import csv

sourcefile = os.path.join("Resources", "election_data.csv")
outputfile = os.path.join("analysis", "election_analysis.txt")

voterList = []
VcandidateList = []
numVotePerCandidate = []

outCandidate = []

with open(sourcefile, "r") as datafile:
    csvreader = csv.reader(datafile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        voterList.append(row[0])
#        countyList.append(row[1])
        VcandidateList.append(row[2])
    numVoters = len(voterList)

    outputHeading = "Election Results"
    lineBreak = "-----------------------------------"
    line01Text = "Total Votes: "
    line99Text = "Winner: "

    print(outputHeading)
    print(lineBreak)    
    print(f"{line01Text} {numVoters}")
    print(lineBreak)
    
    # Remove duplicates from candidate list
    candidateList = list(dict.fromkeys(VcandidateList))

# Write to analysis file
with open(outputfile, "w") as ptext:
    ptext.writelines(outputHeading)
    ptext.write('\n')
    ptext.writelines(lineBreak)
    ptext.write('\n')
    outputLine = f"{line01Text} {numVoters}"
    ptext.writelines(outputLine)
    ptext.write('\n')
    ptext.writelines(lineBreak)
    ptext.write('\n')

 #   print(len(candidateList))
    for candidate in candidateList:
        numVote = VcandidateList.count(candidate)
        numVotePerCandidate.append(numVote)
        VotePercent = numVote/numVoters
        VotePercent = "{:.3%}".format(VotePercent)

        outputLine = f"{candidate}: {VotePercent} ({numVote})"
        print(outputLine)
        ptext.writelines(outputLine)
        ptext.write('\n')
    print(lineBreak)
    ptext.writelines(lineBreak)     
    ptext.write('\n')

    winner = max(numVotePerCandidate)
    winner = numVotePerCandidate.index(winner)
    winner = candidateList[winner]
    print(f"{line99Text} {winner}")
    print(lineBreak)    

    outputLine = line99Text + winner
    ptext.writelines(outputLine)
    ptext.write('\n')
    ptext.writelines(lineBreak)

# End File