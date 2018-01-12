try:
    from xml.etree.cElementTree import XML
    import xml.etree.ElementTree as ET

except ImportError:
    from xml.etree.ElementTree import XML
    import xml.etree.ElementTree as ET

import zipfile
import csv
from collections import Counter
import re



WORD_NAMESPACE = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
TABLE = WORD_NAMESPACE + 'tbl'

SIZE= WORD_NAMESPACE + 'sz'
FTYPE= WORD_NAMESPACE + 'rFonts'

COL = WORD_NAMESPACE + 'tc'
ROW = WORD_NAMESPACE + 'tr'

PARA = WORD_NAMESPACE + 'p'
TEXT = WORD_NAMESPACE + 't'



sizeB =17
sizeC=15
sizeT=21
fontB='Arial'
fontC='Arial'
fontT='Georgia'

balls=[]
for t in range(20):
    for p in range(7):
        balls.append(str(t)+'.'+str(p))

def get_docx_text(path,r):
    """
    Take the path of a docx file as argument, return the text in unicode.
    """
    document = zipfile.ZipFile(path)
    xml_content = document.read('word/document.xml')
    document.close()
    tree = XML(xml_content)
    
    for body in tree:
        colsM = body.findall(COL)
    
    '''for s in root.findall(COL):
        rank = int(s.find(SIZE.attrib['{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val']))
        
        if rank ==18:
            print(True)
            root.remove(COL)
    for size in root.iter(SIZE):
        if size.attrib['{http://schemas.openxmlformats.org/wordprocessingml/2006/main}val']=='18':
            print(True)
            root.remove(COL)
            '''    

    for column in tree.getiterator(COL):
        
        
        texts = [node.text
                 for node in column.getiterator(TEXT)
                 if node.text]
        if texts:
            colsM.append(''.join(texts))
    i=0
    j=0 
    k=0
    l=0
    team_list = ['RCB', 'SRH', 'RPS', 'MI','GL','KKR','DD','KXIP']

    cols1=[]
    for j in range(len(colsM)):
        g=colsM[j]
        fw=''
        if g.count(' ')>0:
            fw= g.split(' ', 1)[0]
        
        if fw!='END':
            
            cols1.append(g)
    
    cols2=[]
    for l in range(len(cols1)):
        g=cols1[l]
        if g.count('-0-')==0:
            cols2.append(g)
                    
    cols=[]
    for k in range(len(cols2)):
        g=cols2[k]
        if g.count('b)')==0:
            cols.append(g)

    team_inc=[]       
    for t in range(len(colsM)):
        g=colsM[t]
        for t1 in range(len(team_list)):
            if g.count(team_list[t1])>0:
                team_inc.append(team_list[t1])
    new1=[]
    for i in range(len(cols)):
        new=[]
        t1=[]

        if is_number(cols[i]):
            
            a= next_num(i+1,cols)
            

            new.append(cols[i])
            if a==None and cols[i]=='0.1':
                a=len(cols)-1
            q=0
            for o in range(i+1,a):
                if(is_anum(cols[o]) or cols[o]=='W' or cols[o]=='1nb' or cols[o]=='1w' or cols[o]=='2w' or cols[o]=='1lb' or cols[o]=='2nb'):
                    if q<1:
                        new.append(cols[o])
                        q+=1

                else:
                    t1.append(cols[o])

            new.append(' '.join(t1[0:len(t1)]))
            if len(new)>2:

            	bow=new[2][-1+1:new[2].find(" to")]

            	bat = re.split(' to |, ',new[2])[1]

            	new.append(bow)
            	    
            	new.append(bat)
            	    
            	if new[1]=='W':
            	    if new[2].count(' c ')==1:
            	        f = re.split(' c | b ',new[2])[1]
            	        if 'sub' in f:
            	        	f=f.partition('(')[-1].rpartition(')')[0]
            	        if f=='&':
            	        	f=new[2].partition('& b ')[-1].rpartition(' ')[0]
            	        	i=0
            	        	e=0
            	        	for i in range(len(f)):
            	        		if is_anum(f[i]):
            	        			e=i
            	        			break
            	        	f=f[0:e]
            	        if '†' in f:
            	        	f = f.replace("†", "")	
            	        new.append(f)
            	
            	if new[2]!='':
            	    new1.append(new)
                   
            continue


    v=find_split(new1)
    new11=new1[0:v+1]
    new22=new1[(v+1):len(new1)]
    with open("outputf"+str(r)+'1st'+".csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([team_inc[0] , 'vs', team_inc[-1]])
        writer.writerow(["Ball No", "Runs", "General Commentary","Bowler",'Batsman','Fielder'])
        

        writer.writerows(new11)

    with open("outputf"+str(r)+'2nd'+".csv", "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([team_inc[-1] , 'vs', team_inc[0]])
        writer.writerow(["Ball No", "Runs", "General Commentary","Bowler",'Batsman','Fielder'])
        

        writer.writerows(new22)  

def next_num(w,cols1):
    for z in range(w,len(cols1)):
        
        if is_number(cols1[z]):
            return z


def is_number(s):
    if s in balls:
        return True
    else:
        return False

def is_anum(e):
    try:
        float(e)
        return True
    except ValueError:
        return False


def find_split(new1):
	for v in range(len(new1)):
		if new1[v][0]=='0.1':
			if new1[v+1][0]=='0.1':
				return v+1
			return v


for r in range(1,11):
    get_docx_text('/home/swap/Match'+str(r)+'.docx',r)



