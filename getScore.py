from textblob import TextBlob
import statistics

text = ''

text=open("log.txt","r").read()

blob = TextBlob(text)
blob.tags           
                    

blob.noun_phrases 

happinessQ=[]  

for sentence in blob.sentences:
    P=(sentence.sentiment.polarity)
    S=(sentence.sentiment.subjectivity)

    if P>=0:
    	happinessQ.append(P+P*(S-0.5))
    else:
    	happinessQ.append(P-P*(S-0.5))

    #print(P)
    #print(S)


mhq=statistics.median(happinessQ)

f=open("score.txt","w")

f.write(str(mhq))

blob.translate(to="es")