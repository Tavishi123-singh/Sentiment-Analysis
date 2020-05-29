punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']
# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())

def strip_punctuation(s):
    for c in punctuation_chars:
        s=s.replace(c,"")
    return s  

def get_neg(s):
    ss=strip_punctuation(s)
    t=ss.lower()
    st=t.split()
    c=0
    for i in st:
        if i in negative_words:
            c+=1
    return -c

def get_pos(s):
    ss=strip_punctuation(s)
    t=ss.lower()
    st=t.split()
    c=0
    for i in st:
        if i in positive_words:
            c+=1
    return c

f=open('project_twitter_data.csv','r')
rd=f.readline()
file=open('resulting_data.csv','w')
file.write('Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score')
file.write('\n')
for data in f.readlines():
    data1=data.split(",")
    row_string = '{},{},{},{},{}'.format(int(data1[1]),int(data1[2]),get_pos(data),get_neg(data),(get_pos(data)+get_neg(data)) )
    file.write(row_string)
    file.write('\n')
file.close()
f.close()
