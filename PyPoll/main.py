import os
import csv

sourcefile = os.path.join("Resources", "election_data.csv")
outputfile = os.path.join("analysis", "election_analysis.csv")

voterList = []
countyList = []
VcandidateList = []
numVotePerCandidate = []

with open(sourcefile, "r") as datafile:
    csvreader = csv.reader(datafile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader:
        voterList.append(row[0])
        countyList.append(row[1])
        VcandidateList.append(row[2])
    numVoters = len(voterList)

    print("Election Results")
    print("-----------------------------------")    
    print(f"Total Votes: {numVoters}")
    print("-----------------------------------")
    # Remove duplicates from candidate list
    candidateList = list(dict.fromkeys(VcandidateList))
    
 #   print(len(candidateList))
    for candidate in candidateList:
        numVote = VcandidateList.count(candidate)
        numVotePerCandidate.append(numVote)
        VotePercent = numVote/numVoters
        VotePercent = "{:.3%}".format(VotePercent)
        print(f"{candidate}: {VotePercent} ({numVote})")
    print("-----------------------------------")     

    winner = max(numVotePerCandidate)
    winner = numVotePerCandidate.index(winner)
    winner = candidateList[winner]
    print(f"Winner: {winner}")
    print("-----------------------------------")    

# Write to analysis file
with open(outputfile, "w", encoding="UTF8") as poll_analysisfile:
    writer = csv.writer(poll_analysisfile)
    writer.writerow(["Election Results"])
    writer.writerow(["Total Votes:", numVoters])
## How to output names?

    writer.writerow(["Winner:", winner])

# End File