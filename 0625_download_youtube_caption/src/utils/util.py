

def num2str(x, k=6):
    x = str(x)
    for i in range(k - len(x)):
        x = '0' + x
    return x


def retrieve_text(text, begin_segment, end_segment):
    candidate_list = []

    begin_segment = begin_segment.split()
    end_segment = end_segment.split()

    text = text.lower().split()

    begin_ids = []
    for i in range(len(text) - len(begin_segment)):
        is_matching = True
        for j in range(len(begin_segment)):
            if text[i + j] != begin_segment[j]:
                is_matching = False
                break
        if is_matching: begin_ids.append(i)


    end_ids = []
    for i in range(len(text)-1, len(end_segment), -1):
        is_matching = True
        for j in range(len(end_segment)):
            if text[i-j] != end_segment[len(end_segment) - 1 - j]:
                is_matching = False
                break

        if is_matching: end_ids.append(i)
    end_ids.sort()

    for begin_id in begin_ids:
        for end_id in end_ids:
            if begin_id < end_id:
                segment = ' '.join(text[begin_id:end_id+1])
                candidate_list.append([segment, begin_id, end_id])

    return candidate_list

# text = 'ad dc ef a b cx ff gh a b cx ff gg'
# print (retrieve_text('a b', 'ff', text))

def edit_text(text, segment_data, new_segment):
    text = text.split()
    [_, begin_id, end_id] = segment_data

    new_segment = new_segment.split()
    new_text = ' '.join(text[:begin_id] + new_segment + text[end_id+1:])
    return new_text

# text = 'ad dc ef a b cx ff gh a b cx ff gg'
# print (edit_text(text, ['x', 10, 12], 'xxx yyy'))
