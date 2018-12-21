file_access = open('student-mat.csv','r')
data = file_access.read()
F_count = 0
M_count = 0
age_count = 0
G_count = 0
count = 0
data_lines = data.split('\n')
data_words = data_lines[0].split(';')
student_details = {}
for i in range(1,len(data_lines)-1):
    student_details[i] = {}
    details = data_lines[i].split(';')
    student_details[i] = dict(zip(data_words,[x.strip('"') for x in details]))
#print(student_details)
for j in range(1,len(student_details)+1):
    if(student_details[j]['sex'] == 'F'):
        F_count = F_count + 1
    if(student_details[j]['sex'] == 'M'):
        M_count = M_count + 1
    #print(student_details[j]['sex'])
print("Female Count:",F_count,"Male Count:",M_count)
for k in range(1,len(student_details)+1):
    if(student_details[k]['sex'] == 'F' and (int(student_details[k]['age']) >= 18 and int(student_details[k]['age']) <= 20 ) ):
        age_count = age_count + 1
print("Female and Age between 18 and 20:",age_count)
for l in range(1,len(student_details)+1):
    if student_details[l]['guardian'] in ['mother','father','others']:
        G_count = G_count + 1
print("Guardian count:",G_count)
for m in range(1,len(student_details)+1):
    if int(student_details[m]['age']) > 18 and student_details[m]['internet'] == 'yes' and student_details[m]['Mjob'] and int(student_details[m]['health']) >=3:
        count = count + 1
print(count)
#print(student_details[1]['guardian'])







'''file1 = open('siva.txt','w')
string = str(student_details)
file1.write(string)
file1.close()'''