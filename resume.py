print("::::::::::::::::::Resume keyword scanner:::::::::::::::::")

def get_key(text):
    text= text.lower()
    text = text.replace("-"," ")
    words = text.split()
    stop_words =  ['the', 'is', 'and', 'a', 'to', 'in', 'of', 'for', 'with', 'on']
    keywords = [word.strip('.,!?()[]{}_-') for word in words if word not in stop_words]
    return set(keywords)
#getting inputs
job_descrip = input("\nEnter the job description:\n")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
job_descrip = ' '.join(lines)    
resume = input("\nEnter your resume :\n")
lines = []
while True:
    line = input()
    if line == "":
        break
    lines.append(line)
resume = ' '.join(lines)  

#extracting keywords
job_key = get_key(job_descrip)
resume_key = get_key(resume)

#match analysis
matches = job_key.intersection(resume_key)
missing = job_key.difference(resume_key)


#matching percentage 
match_percentage  = (len(matches)/len(job_key))*100 if job_key else 0 

print("\n Keywords matched in resume:")
print(', '.join(matches) if matches else "No keywords matched")

print("\n Keywords missing from resume:")
print(', '.join(missing) if missing else "None! Best match")

print(f"\n Match percentage: {match_percentage:.2f}%")
