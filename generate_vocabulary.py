import re

def word_tokenize(s):
    sent = s.lower()
    sent = re.sub('[^A-Za-z0-9\s]+',' ', sent)
    return sent.split()

if __name__ == '__main__':

    txt_path = 'exp_data/Charades_STA/vocab_glove_complete.txt'
    vocab_file = open(txt_path, 'w')
    words = []
    for split in ['train','test']:
        anno_list = open('exp_data/Charades_STA/charades_sta_{}.txt'.format(split)).readlines()

        for anno in anno_list:
            info, sentence = anno.split('##')
            sentence = sentence.split('.\n')[0]
            words.extend(word_tokenize(sentence))
    vocab_file.write('\n'.join(set(words)))


