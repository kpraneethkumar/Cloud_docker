import string
import socket
import os

def main():
    result_file = open("/home/output/result.txt", "w+")
    path = "/home/data"
    dir_list = os.listdir(path)
    result_file.write("All the files in /home/data are as follows:- ")
    result_file.write(path)
    for file_name in dir_list:
        result_file.write(" \n")
        result_file.write(file_name)
    if_file = open('/home/data/IF.txt','r')
    data = if_file.read()
    word_if_file = data.split()
    lime_file = open('/home/data/Limerick.txt','r')
    data = lime_file.read()
    word_lime_file = data.split()
    result_file.write(" \n")
    result_file.write("Limerick.txt has a word count of:- "+str(len(word_lime_file)))
    word_if = []
    for word in word_if_file:
        jo = word.translate(str.maketrans('', '', string.punctuation))
        jo = jo.capitalize()
        word_if.append(jo)
    result_file.write(" \n")
    result_file.write("IF.txt has a word count of:- "+str(len(word_if)))
    result_file.write(" \n")
    result_file.write("Total number of words in IF.txt and Limerick.txt are:- "+str(len(word_if) + len(word_lime_file)))
    count_if = []
    unique_words = set(word_if)
    for word in unique_words:
        count_if.append(word_if.count(word))
    word_if = list(unique_words)
    order_count_if = sorted(count_if, reverse=True)
    result_file.write("\n")
    result_file.write("The top 3 words with maximum number of counts in IF.txt are:- ")
    j = 0
    for j in range(0,3):
         for i in range(0,len(count_if)):
             if(count_if[i] == order_count_if[j]):
                 result_file.write("\n")
                 result_file.write(""+word_if[i]+" - "+ str(count_if[i]) )
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)
    result_file.write("\n")
    result_file.write("Docker machine IP Address is:" + IPAddr) 
    result_file.close()
    result_file = open('/home/output/result.txt','r')
    data_result = result_file.read()
    print(data_result)

if __name__ == "__main__":
    main()
