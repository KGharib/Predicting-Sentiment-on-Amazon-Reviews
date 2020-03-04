from string import punctuation
from collections import Counter
from nltk.stem import WordNetLemmatizer 
from nltk.corpus import stopwords
import csv
''''''

word_bank = []
file_CSV = open('vocabs.csv')
data_CSV = csv.reader(file_CSV)
list_CSV = list(data_CSV)
for ele in list_CSV:
    for word in ele:
        word_bank.append(word)

''''''
vocab2index2 = {word: ii for ii, word in enumerate(word_bank, 1)}

''''''
def cleanup(sentence):
    sentence = str(sentence)
    sentence = sentence.lower()
    return sentence
''''''
def label_to_cata(label):
    num_classes = 5
    labels_encoded = pd.get_dummies(label)
    labels_cat = to_categorical(labels_encoded, num_classes)
    return labels_cat

''''''

def remove_stopwords(df):
    filtered_sentence = [w for w in reviews if not w in stop_words]
    filtered_sentence = [] 
  
    for w in reviews: 
        if w not in stop_words: 
            filtered_sentence.append(w) 
  

''''''
#Tokenize
from string import punctuation
punctuation = ['!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~']
def tokenize_review(test_review):
    test_review = test_review.lower() # lowercase
    # get rid of punctuation
    test_text = ''.join([c for c in test_review if c not in punctuation])

    # splitting by spaces
    test_words = test_text.split()

    # tokens
    test_ints = []
    test_ints.append([vocab2index[word] for word in test_words])

    return test_ints


''''''

#padding features
def pad_features(reviews_ints, seq_length):
    ''' Return features of review_ints, where each review is padded with 0's 
        or truncated to the input seq_length.
    '''
    
    # getting the correct rows x cols shape
    features = np.zeros((len(reviews_ints), seq_length), dtype=int)

    # for each review, I grab that review and 
    for i, row in enumerate(reviews_ints):
        features[i, -len(row):] = np.array(row)[:seq_length]
    
    return features

''''''

# Predict sentiment for a given sentence
def predict(net, test_review, sequence_length=200):
    
    net.eval()
    
    # tokenize review
    test_ints = tokenize_review(test_review)
    
    # pad tokenized sequence
    seq_length=sequence_length
    features = pad_features(test_ints, seq_length)
    
    # convert to tensor to pass into your model
    feature_tensor = torch.from_numpy(features)
    
    batch_size = feature_tensor.size(0)
    
    # initialize hidden state
    h = net.init_hidden(batch_size)
    
    if(train_on_gpu):
        feature_tensor = feature_tensor.cuda()
    
    # get the output from the model
    output, h = net(feature_tensor, h)
    
    # convert output probabilities to predicted class (0 or 1)
    pred = torch.round(output.squeeze()) 
    # printing output value, before rounding
    print('Prediction value, pre-rounding: {:.6f}'.format(output.item()))
    
    # print custom response
    if(pred.item()==1):
        print("Positive review detected!")
    else:
        print("Negative review detected.")
''''''
