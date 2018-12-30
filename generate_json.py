import json

if __name__ == '__main__':

    for split in ['train','test']:
        anno_list = open('exp_data/Charades_STA/charades_sta_{}.txt'.format(split)).readlines()
        json_path = 'exp_data/Charades_STA/charades_sta_{}.json'.format(split)

        data = []
        for anno in anno_list:
            info, sentence = anno.split('##')
            sentence = sentence.split('.\n')[0]
            video_id, start, end = info.split(' ')
            row = {'video':video_id, 'description': sentence, 'timestamp':[float(start), float(end)]}
            data.append(row)
        with open(json_path, 'w') as json_file:
            json.dump(data, json_file)



