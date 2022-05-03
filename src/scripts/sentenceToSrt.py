import datetime


def time_addition(current_time, sentence, block_num):
    time_add = (len(sentence.split())) * 0.75
    end_time = current_time + datetime.timedelta(0, time_add)
    str_current_time = str(current_time.time())
    str_end_time = str(end_time.time())
    with open("srtMovieName.srt", "a") as f:
        f.write(str(block_num))
        f.write("\n")
        f.write(str_current_time)
        f.write("-->")
        f.write(str_end_time)
        f.write("\n")
        f.write(sentence)
        f.write("\n")
        f.write("\n")
    return end_time, block_num + 1


test_sentence = "My Name Guy Dahan and i Like Pussy"
stat_time = datetime.datetime(100, 1, 1, 0, 0, 0)
block_num = 10
stat_time, block_num = time_addition(stat_time, test_sentence, block_num)

test_sentence = "And Lior Elisberg Love Balls"
stat_time, block_num = time_addition(stat_time, test_sentence, block_num)

test_sentence = "And we Both love each other"
time_addition(stat_time, test_sentence, block_num)
