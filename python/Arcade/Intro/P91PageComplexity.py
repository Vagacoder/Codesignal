#
# * Python 91. Page Complexity
# * Medium

# * You are creating a new website about HTML parsing. You don't want your page 
# * to be too simple, so you would like to estimate the complexity of the main 
# * page of your site. In order to measure the complexity of the page, you need 
# * to find a set of all tags located on the deepest level of a tree correponsing 
# * to HTML document. Given a valid HTML document, find all distinct tags located 
# * on the deepest level.

# * Example

# For
# document = "<!DOCTYPE html><html> <body> <h1>The best heading ever</h1> <p>The worst paragraph ever.</p> </body></html>"
# the output should be
# pageComplexity(document) = ["h1", "p"].

# * Input/Output

#     [execution time limit] 4 seconds (py3)

#     [input] string document

#     Correct HTML document.

#     Guaranteed constraints:
#     10 ≤ document.length ≤ 900.

#     [output] array.string

#     List of all distinct tags on the deepest level sorted lexicographically.

#%%

# * Solution 1
def pageComplexity1(document:str)-> list:
    from html.parser import HTMLParser

    tags = {}

    class MyParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.depth = 1

        def handle_starttag(self, tag, attrs):
            self.depth +=1
            if tag in tags:
                tags[tag] = max(tags[tag], self.depth)
            else:
                tags[tag] = self.depth


        def handle_endtag(self, tag):
            self.depth -= 1


    parser = MyParser()
    parser.feed(document)

    print(tags)

    deepest = max(tags.values())
    
    print(deepest)

    result = []
    for k, v in tags.items():
        if v == deepest:
            result.append(k)

    return sorted(result)


document1 = '<!DOCTYPE html><html> <body> <h1>The best heading ever</h1> <p>The worst paragraph ever.</p> </body></html>'
r1 = pageComplexity1(document1)
print('r1 is:',r1)

document1 = '<!DOCTYPE html><html><body><h2>Polular russian drinks</h2><ul>  <li>Coffee</li>  <li>Tea    <ul>    <li>Black tea</li>    <li>Green tea      <ul>      <li>China</li>      <li>Africa</li>      </ul>    </li>    </ul>  </li>  <li>Milk</li>  <li>Vodka</li>  <li>Vodka</li>  <li>Vodka</li>  <li>Vodka</li></ul></body></html>'
r1 = pageComplexity1(document1)
print('r1 is:',r1)
# %%
