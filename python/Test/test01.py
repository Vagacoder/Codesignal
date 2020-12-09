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
