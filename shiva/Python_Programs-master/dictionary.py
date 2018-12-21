'''Dictonaries
you are in a business conference, the french team near you are your potential clients, you want to greet them and talk about their new project ? 
To start with you ask a question , if they can speak english and they say No. 
So you need to talk to them in French, create a dictonary out of the below table, key = english word --> value is a list of french word,Pronunciation.
So now when ever you want to talk something in english , you say that sentence to this program and it translates it to French for you 
If some words are not present in below conversion table , keep the same word in english to french. 
Example: 
Enter your setence: How are you ? 
In French: Comment allez-vous? - kommahng tahlay voo 
Enter your setence: How many products ? 
In French: Combien? products - kong-byang products 
Exit conversation if entered setence is bye or exit'''


dd = {'Yes':['Oui','wee'],'No':['Non','nong'],'Yes,please':['Oui,s il vous plaît','wee, seel voo play'],'No, thank you':['Non, merci','nong, mair-see'],'Please':['S il vous plaît','seel voo play'],'Thank you':['Merci (madame/monsieur)','mair-see (mah-dahm/mer-syer)'],"You're welcome":["Il n'y a pas de quoi",'eel nyah pah der kwah'],'Here is/are':['Voici...','vwah-see'],'There is/are':['Voilà...','vwah-la'],'Hello':['Bonjour','bong-zhoor'],'Goodbye':['Au revoir','oh rer-vwahr'],'Good night':['Bonne nuit','bonn nwee'],'How are you?':['Comment allez-vous?','kommahng tahlay voo'],'Very well, thanks':['Très bien, merci','tray byang mair-see'],'Excuse me':['Excusez-moi','ex-kewzay mwah'],'Do you speak English?':['Est-ce que vous parlez anglais?','essker voo pahrlay ahng-glay']}
french_words = []
pron_words= []
s = ' '
while(True):
    inp1 = input("Enter your sentence:")
    if(inp1 in ['bye','exit']):
        break
    else:
        li = inp1.split(' ')
        for i in range(len(li)):
            if(li[i] in dd.keys()):
                french_words.append(dd[li[i]][0])
                pron_words.append(dd[li[i]][1])
            else:
                french_words.append(li[i])
                pron_words.append(li[i])
        print("In French:",s.join(french_words),'-',s.join(pron_words))
        french_words.clear()
        pron_words.clear()
