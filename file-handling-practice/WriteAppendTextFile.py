# Writing new content (overwrites existing)
with open("summary.txt", "w") as file:
    file.write("Daily Report Summary\n")
    file.write("Total Transactions: 1200\n")
    
# Appending data
with open("summary.txt", "a") as file:
    file.write("Errors: 5\n")
