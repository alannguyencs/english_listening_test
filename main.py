import codecs
import constants
import utils
import processor



def main():
    transcription_content = processor.parse_data_file(constants.transcription_path)
    typing_content = processor.parse_data_file(constants.typing_path)

    # print (transcription_content)
    # print (typing_content)

    lcc_content = utils.longest_common_child(transcription_content, typing_content)
    # print (lcc_content)

    error_content = utils.marking_error(lcc_content, typing_content)
    matching_score = 2 * len(lcc_content) / (len(transcription_content) + len(typing_content))

    print ('Matching score = {:.2f}%'.format(100 * matching_score))
    for error_content_id in range(len(error_content)):
        print (error_content[error_content_id], end=' ')
        if error_content_id % 15 == 14:
            print('')


main()