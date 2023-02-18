import csv

def word_traker(prompt):
    with open('dataset.csv', 'r') as csvfile:
        reader = csv.reader(csvfile)
        keyword = [row[0] for row in reader]
    
    prompt_words = prompt.split()
    
    for word in prompt_words:
        if word in keyword:
            print("Given prompt is inappropriate")
    
    return False


text  = "Place the text data herer" #if you are sing this for an app pass the text data here

word_traker(text)