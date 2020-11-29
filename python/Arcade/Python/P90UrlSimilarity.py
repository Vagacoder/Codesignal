#
# * Python 90. Url Similarity
# * Medium

# * You've got tired of fixing your relatives' PCs after they visited some phishing 
# * website so you decided to implement a special plug-in for their browsers which 
# * will check if the page they are trying to visit is similar to the one in the 
# * blacklist.

# For that, you've thought of the special algorithm that for two URLs url1 and 
# url2 computes their similarity as following:

#     Initially their similarity is 0
#     Then, it is increased by the following rules:

#     +5, if the same protocol is used in both URLs.
#     +10, if url1 and url2 have the same address.
#     +k, if the first k components of path (delimited by /) are exactly the same 
#       (and in the same order) between the two URLs.
#     +1 if for each varNames common between them. Additional +1 if the respective 
#       values are equal too.

# URLs are given in the following format: protocol://address[(/path)*][?query] 
# (where query = varName=value(&varName=value)*, parts given in [] are optional, 
# and parts in ()* may be repeated several times). Each of the named elements 
# (i.e. protocol, address, path, varName and value) are guaranteed to contain only 
# alphanumeric characters and periods.

# Given the two URLs url1 and url2, compute their similarity using the algorithm described above.

# * Example

# For

# url1 = "https://codesignal.com/home/test?param1=42&param3=testing&login=admin"

# and

# url2 = "https://codesignal.com/home/secret/test?param3=fish&param1=42&password=admin"

# the output should be
# urlSimilarity(url1, url2) = 19.

# Because these URLs have the same protocols, addresses, first path component (home) and two varNames, with one also having the same value in both of them.
# So the resulting similarity is thus 5 + 10 + 1 + 1 + 1 + 1 = 19.

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string url1

#     First URL. It can only contain lowercase English letters, digits and characters '.', '/', ':', '?', '&' and '='.
#     It's guaranteed that each varName is unique.

#     Guaranteed constraints:
#     5 ≤ url1.length ≤ 100.

#     [input] string url2

#     Second URL with the same format as url1.

#     Guaranteed constraints:
#     5 ≤ url2.length ≤ 100.

#     [output] integer

#     The computed similarity.

#%%

# * Solution 1
# ! urllib.parse.urlparse()
def urlSimilarity1(url1, url2):
    from urllib.parse import urlparse
    result = 0
    p1 = urlparse(url1)
    p2 = urlparse(url2)

    if p1.scheme == p2.scheme:
        result += 5
    if p1.netloc == p2.netloc:
        result += 10

    paths1 = p1.path.split('/')
    paths2 = p2.path.split('/')

    for i, path1 in enumerate(paths1):
        if i < len(paths2) and path1 == paths2[i]:
            result += i
    
    # print(p1.query)
    # print(p2.query)

    if p1.query != '' and p2.query != '':
        query1 = p1.query.split('&')
        query2 = p2.query.split('&')

        # print(query1)
        # print(query2)

        qdic1 = {q.split('=')[0]: q.split('=')[1] for q in query1}
        qdic2 = {q.split('=')[0]: q.split('=')[1] for q in query2}
        
        # print(qdic1)

        for key in qdic1.keys():
            if key in qdic2:
                result += 1
                if qdic1[key] == qdic2[key]:
                    result += 1

    return result 



# * Solution 2
# ! urllib.parse.parse_qs()
def urlSimilarity2(url1, url2):
    from urllib.parse import urlparse, parse_qs
    result = 0
    p1 = urlparse(url1)
    p2 = urlparse(url2)

    if p1.scheme == p2.scheme:
        result += 5
    if p1.netloc == p2.netloc:
        result += 10

    paths1 = p1.path.split('/')
    paths2 = p2.path.split('/')

    for i, path1 in enumerate(paths1):
        if i < len(paths2) and path1 == paths2[i]:
            result += i
    
    # print(p1.query)
    # print(p2.query)

    q1 = parse_qs(p1.query)
    q2 = parse_qs(p2.query)

    # print(q1)
    # print(q2)

    for key in q1:
        if key in q2:
            result += 1
            if q2[key] == q1[key]:
                result += 1

    return result




url1 = 'https://codesignal.com/home/test?param1=42&param3=testing&login=admin'
url2 = 'https://codesignal.com/home/secret/test?param3=fish&param1=42&password=admin'
r1 = urlSimilarity2(url1, url2)
print(r1)

url1 = 'ftp://www'
url2 = 'http://anotherexample.com/www?ftp=http'
r1 = urlSimilarity2(url1, url2)
print(r1)
