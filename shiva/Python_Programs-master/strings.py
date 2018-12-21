'''Strings
You are presenting text to students on python strings, but its not formated and has few mistakes, you need to correct it using a python program. Fix the below issues. Input is the setence and output needs to be the same setence without mentioed issues. 
Sentence:
" Using string methods in Jython is very he1pful. but you need to have a clear understanding of the method syntax and usage or e1se your jython program may fail complet1y. There is no wonder jython string methods are usefu1 in handling text proper1y. "
Issues:
Python is missed typed as Jython or jython
l in few places is typed as 1.
Setnence starting word after . (full stop symbol) should start with capital letter
Make syntax and usage words all capitals as they need emphasis.'''


wrong_data = "Using string methods in Jython is very he1pful. but you need to have a clear understanding of the method syntax and usage or e1se your jython program may fail complet1y. There is no wonder jython string methods are usefu1 in handling text proper1y."
right_data=wrong_data.replace("Jython","Python")
right_data=right_data.replace("jython","Python")

right_data_list = right_data.split(' ')
for i in range(len(right_data_list)):
    if('1' in right_data_list[i]):
        str1 = right_data_list[i].replace('1','l')
        right_data_list[i] = str1
    if('.' in right_data_list[i] and i < len(right_data_list)-1 ):
        right_data_list[i+1] = right_data_list[i+1].capitalize()
    if(right_data_list[i] =='syntax' and right_data_list[i+2] == 'usage'):
        right_data_list[i] = right_data_list[i].upper()
        right_data_list[i+1] = right_data_list[i+1].upper()
        right_data_list[i+2] = right_data_list[i+2].upper()
        
print(' '.join(right_data_list))