#opens the file project_twitter_data.csv which has the fake generated twitter data
TwitterFile = open("project_twitter_data.csv","r")

#create a csv file called resulting_data.csv
ResultFile = open("resulting_data.csv","w")


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

#function that removes punctuation marks

def strip_punctuation(str):
    for i in punctuation_chars:
        str = str.replace(i, "")
    return str

# list of positive words to use

positive_words = []
with open("positive_words.txt") as pos_f:
    for line in pos_f:
        if line[0] != ';' and line[0] != '\n':
            positive_words.append(line.strip())

#count positive words

def get_pos(sentence):
    s = strip_punctuation(sentence)
    lst= s.split()
    count=0
    for wrd in lst:
        for i in positive_words:
            if wrd.lower() == i:
                count+=1
    return count

# list of negative words to use

negative_words = []
with open("negative_words.txt") as pos_f:
    for line in pos_f:
        if line[0] != ';' and line[0] != '\n':
            negative_words.append(line.strip())

#count negative words

def get_neg(sentence):
    s = strip_punctuation(sentence)
    lst = s.split()
    accum = 0
    for wrd in lst:
        for j in negative_words:
            if j == wrd.lower():
                accum += 1
    return accum

'''csv file contains the Number of Retweets, Number of Replies, Positive Score
(which is how many happy words are in the tweet), Negative Score (which is how
many angry words are in the tweet), and the Net Score (how positive or negative
the text is overall) for each tweet.'''

def write_file(file):
    file.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
    file.write("\n")

    lines =  TwitterFile.readlines()
    remove_header = lines.pop(0)
    for line in lines:
        list = line.strip().split(',')
        file.write("{}, {}, {}, {}, {}".format(list[1], list[2], get_pos(list[0]), get_neg(list[0]), (get_pos(list[0])-get_neg(list[0]))))
        file.write("\n")

write_file(ResultFile)
TwitterFile.close()
ResultFile.close()
