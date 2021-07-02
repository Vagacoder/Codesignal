#
# * Core 147. LRC to SubRip

# During your most recent trip to Codelandia you decided to buy a brand new 
# CodePlayer, a music player that (allegedly) can work with any possible media 
# format. As it turns out, this isn't true: the player can't read lyrics written 
# in the LRC format. It can, however, read the SubRip format, so now you want to 
# translate all the lyrics you have from LRC to SubRip.

# Since you are a pro programmer (no noob would ever get to Codelandia!), you're 
# happy to implement a function that, given lrcLyrics and songLength, returns the 
# lyrics in SubRip format.

# Example

# For

# lrcLyrics = ["[00:12.00] Happy birthday dear coder,",
#              "[00:17.20] Happy birthday to you!"]

# and songLength = "00:00:20", the output should be

# lrc2subRip(lrcLyrics, songLength) = [
#   "1",
#   "00:00:12,000 --> 00:00:17,200",
#   "Happy birthday dear coder,",
#   "",
#   "2",
#   "00:00:17,200 --> 00:00:20,000",
#   "Happy birthday to you!"
# ]

# Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] array.string lrcLyrics

#     Lyrics in LRC format. Each string has the format [MM:SS.xx] <song_line>, 
#       (note the whitespace character after the time) where:
#         MM:SS.xx is the lyrics time (it is guaranteed that the elements of 
#       lrcLyrics are sorted in ascending order of this time);
#             0 ≤ int(xx) ≤ 99;
#             0 ≤ int(SS) ≤ 59;
#             0 ≤ int(MM) ≤ 99;
#         <song_line> is the corresponding lyrics line.

#     Guaranteed constraints:
#     1 ≤ lrcLyrics.length ≤ 50,
#     1 ≤ lrcLyrics[i].length ≤ 100.

#     [input] string songLength

#     The length of the song in the format "HH:MM:SS". It is guaranteed that it 
#       is greater than the last time in lrcLyrics.

#     Guaranteed constraints:
#     0 ≤ int(HH) ≤ 2,
#     0 ≤ int(MM) ≤ 59,
#     0 ≤ int(SS) ≤ 59.

#     [output] array.string

#     The given lyrics in the SubRip format. For each line in the lrcLyrics, three 
#       new lines should be generated:
#         the first line is the 1-based lyrics line number;
#         the second line should be in the format HH1:MM1:SS1,xxx1 --> HH2:MM2:SS2,xxx2, where:
#             HH1:MM1:SS1,xxx1 the time the row starts;
#             HH2:MM2:SS2,xxx2 when the next lyrics should appear, or the length 
#               of the song if it's the last lyrics line;
#         the last line is the lyrics text itself.

#     Each pair of consecutive three-lines groups should be separated by a single 
#       empty string.

#%%

# * Solution 1
def lrc2subRip(lrcLyrics, songLength):
    result = []
    n = len(lrcLyrics)
    for i in range(n):
        result.append(str(i+1))
        lyric = lrcLyrics[i]
        # print(lyric)
        tokens = lyric.split(']')
        # print(tokens)
        # time1 = '00:' + tokens[0].replace('[', '') + '0'
        time1 = tokens[0].replace('[', '')
        l = tokens[1].lstrip()
        time1Minutes = int(time1.split(':')[0])
        time1Sec = time1.split(':')[1]
        time1Hour = time1Minutes//60
        time1Min = time1Minutes%60
        time1 = '{:02d}:{:02d}:'.format(time1Hour, time1Min) + time1Sec + '0'
        time1 = time1.replace('.', ',')
        # print(time1)
        if i < n-1:
            # time2 = '00:' + lrcLyrics[i+1].split(']')[0].replace('[', '') + '0'
            # time2 = time2.replace('.', ',')
            lyric = lrcLyrics[i+1]
            tokens = lyric.split(']')
            time2 = tokens[0].replace('[', '')
            time2Minutes = int(time2.split(':')[0])
            time2Sec = time2.split(':')[1]
            time2Hour = time2Minutes//60
            time2Min = time2Minutes%60
            time2 = '{:02d}:{:02d}:'.format(time2Hour, time2Min) + time2Sec + '0'
            time2 = time2.replace('.', ',')
        else:
            time2 = songLength + ',000'
        # print(time2)
        result.append(time1 + ' --> ' + time2)
        result.append(l)
        if i != n-1:
            result.append("")


    return result


# l1 = ["[00:12.00] Happy birthday dear coder,",
#       "[00:17.20] Happy birthday to you!"]
# s1 = "00:00:20"
# r1 = lrc2subRip(l1, s1)
# print(r1)

l1 = ["[12:51.10] Hello tacher tell me whats my lesson", 
    "[16:57.10] Look right through me,", 
    "[24:00.36] look right through me", 
    "[27:04.57] And I find it kind of funny", 
    "[34:08.16] I find it kind of sad", 
    "[46:10.42] The dream in which Im dying", 
    "[57:13.70] Are the best Ive ever had", 
    "[68:16.47] I find it hard to tell you", 
    "[73:19.47] Cos I find it hard to take", 
    "[86:22.56] When people run in circles", 
    "[92:25.91] Its a very very"]
s1 = "00:00:20"
r1 = lrc2subRip(l1, s1)
print(r1)
