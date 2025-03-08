job_details = [
    ['a', 2, 100],  # Job 'a' with deadline 2 and profit 100
    ['b', 2, 20],   # Job 'b' with deadline 2 and profit 20
    ['c', 1, 40],   # Job 'c' with deadline 1 and profit 40
    ['d', 3, 35],   # Job 'd' with deadline 3 and profit 35
    ['e', 1, 25]    # Job 'e' with deadline 1 and profit 25
]

n = len(job_details)  # Total number of jobs
maxD = 3  # Maximum deadline

# Sort jobs in descending order of profit (Bubble Sort)
for i in range(n):
    for j in range(n-1-i):
        if job_details[j][2] < job_details[j+1][2]:
            job_details[j], job_details[j+1] = job_details[j+1], job_details[j]

# Initialize job slots with 'empty'
slot = ['empty'] * maxD
total_profit = 0  

# Assign jobs to slots
for i in range(n):
    k = int(job_details[i][1]) 
    while k > 0:
        if slot[k-1] == 'empty':  # Check if the slot is available
            slot[k-1] = job_details[i][0]  # Assign job to the slot
            total_profit += job_details[i][2]  # Add profit
            break  # Move to the next job
        k -= 1  # Check the previous slot if the current one is occupied

# Output the final job sequence and total profit
print("Scheduled Jobs:", slot)
print("Total Profit:", total_profit)
