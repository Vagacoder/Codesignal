#%%

from html.parser import HTMLParser

class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print('Start tag', tag)
        return None

    def handle_endtag(self, tag):
        print('End tag', tag)
        return None

    def handle_data(self, data):
        print('Data', data)
        return None

'''
Note: self-closing tag, such as <img />, is detected in both 
handle_startag() and handle_endtag()
'''
parser = MyParser()
parser.feed('<html><head><title>Test</title></head><body><h1>Parse me!</h1><img /></body></html>')

# %%
# * my rotation function for Core 158
# * rotating a m x n matrix clockwise 90 degree
# * e.g 
# [1, 2 ,3] => [4, 1]
# [4, 5 ,6]    [5, 2]
#              [6, 3]
def rotate(matrix: list)-> list:
    return list(zip(*(matrix[::-1])))

m1 = [[1,2,3], [4,5,6]]
print(rotate(m1))
