import codecs
from constants import *
import utils
import processor



def run():
    tapescript_content = processor.parse_data_file(TAPESCRIPT_PATH)
    typing_content = processor.parse_data_file(TYPING_PATH)

    # print (transcription_content)
    # print (typing_content)

    lcc_content = utils.longest_common_child(tapescript_content, typing_content)
    # print (lcc_content)

    tapescript_error_content = utils.marking_error(lcc_content, tapescript_content)
    typing_error_content = utils.marking_error(lcc_content, typing_content)
    matching_score = 2 * len(lcc_content) / (len(tapescript_content) + len(typing_content))

    #Write matching score and error to file
    error_file = open(ERROR_PATH, 'w')
    error_file.write('Matching score = {:.2f}%\n\n'.format(100 * matching_score))

    error_file.write('Yours:\n')
    utils.write_error_to_file(typing_error_content, error_file)

    error_file.write('Correct:\n')
    utils.write_error_to_file(tapescript_error_content, error_file)



run()