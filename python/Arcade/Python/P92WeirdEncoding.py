#
# * Python 92. Weird Encoding
# * Medium

# * You've been actively exchanging email with one of your colleagues and noticed 
# * that you can't open his attachments. Unfortunately, he's just went on a vacation 
# * and you need these attached files right now.

# You've spent some time studying his emails and discovered that your colleague 
# used the buggy email client which instead of using proper MIME Base64 encoding 
# for the attachments used other variants differing in characters that represent 
# values 62 and 63.

# Furthermore, different versions of this email client used different variations 
# of the encoding!

# Given the encoding of the email client which was used to send attachment,
# decode it.

# Here is the default Base64 encoding table:

# * Example

# For encoding = "-_" and message = "Q29kZVNpZ25hbA==", the output should be
# weirdEncoding(encoding, message) = "CodeSignal".

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string encoding

#     Two distinct characters used for values 62 and 63 instead of + and /.
#     It's guaranteed that these characters are not equal to '=' or used for encoding values from 0 to 61.

#     Guaranteed constraints:
#     encoding.length = 2,
#     encoding[0] ≠ encoding[1].

#     [input] string message

#     A message to decode.

#     Guaranteed constraints:
#     4 ≤ message.length ≤ 1000.

#     [output] string

#     A decoded message.

#%%

# * Solution 1
# ! base64.base64code() and byte object.decode()
def weirdEncoding(encoding:str, message:str)-> str:
    import base64

    decoded = base64.b64decode(message, altchars=encoding)
    # print(decoded)

    return decoded.decode('utf-8')



e1 = '-_'
m1 = 'Q29kZVNpZ25hbA=='
r1 = weirdEncoding(e1, m1)
print(r1)

e1 = '/+'
m1 = 'U29tZSB2ZXJ5IHN0cmFuZ2UgYW5kIGxvbmcgYXR0YWNobWVudD8+Pw=='
r1 = weirdEncoding(e1, m1)
print(r1)

e1 = '%$'
m1 = 'PyE$ISE$IT8hP2Zlc2VmZXNm'
r1 = weirdEncoding(e1, m1)
print(r1)
