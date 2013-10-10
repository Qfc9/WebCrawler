print "loading..."
import urllib2, shutil, os, time

def noHTML(definition):
    command = False
    
    while command is False:
        lessOpen = definition.find('<')
        greatClose = definition.find('>')
        if lessOpen > -1 and greatClose > -1:
            definition = definition[0:lessOpen] + definition[greatClose+1:]
        else:
            command = True

    return definition
            
def noQuote(fraze):
    fraze = fraze.replace('"', "'")

    return fraze

def main():
    letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    craw = ['C','r','a','w','l','i','n','g','.','.','.','','']
    x = 0
    dic = dict()

    print "\nCrawling...\n"
    for fourthletter in letters:
        for thirdletter in letters:
            for secletter in letters:
                for letter in letters:
                    try:
                        response = urllib2.urlopen("http://dictionary.reference.com/browse/"+fourthletter+thirdletter+secletter+letter)
                        page_source = response.read()
                        print 'Processing '+fourthletter+thirdletter+secletter+letter

                        beginDef = page_source.find('<div class="dndata">')

                        if beginDef > -1:
                            endDef = page_source[beginDef:beginDef+5000].find('</div>')

                            dic.update({fourthletter+thirdletter+secletter+letter: noQuote(noHTML(page_source[beginDef+20:beginDef+endDef]))})
                            
                            #print secondletter+firstletter+letter+":",noHTML(page_source[beginDef+20:beginDef+endDef])
                            #file = open('diclog.txt', "a")
                            #file.write('INSERT INTO  `Dic` (  `id` ,  `Term` ,  `Def` )VALUES("", "'+thirdletter+secondletter+letter+'","'+noQuote(noHTML(page_source[beginDef+20:beginDef+endDef]))+'");')
                            #file.close()
                            #array.append('INSERT INTO  `Dic` (  `id` ,  `Term` ,  `Def` )VALUES("", "'+thirdletter+secondletter+letter+'","'+noQuote(noHTML(page_source[beginDef+20:beginDef+endDef]))+'");')

                        else:
                            beginDef = page_source.find('</span> <div class="luna-Ent">')

                            if beginDef > -1:
                                endDef = page_source[beginDef:beginDef+5000].find('</div>')

                                dic.update({fourthletter+thirdletter+secletter+letter: noQuote(noHTML(page_source[beginDef+30:beginDef+endDef]))})
                                
                                #print secondletter+firstletter+letter+":",noHTML(page_source[beginDef+30:beginDef+endDef])
                                #file = open('diclog.txt', "a")
                                #file.write('INSERT INTO  `Dic` (  `id` ,  `Term` ,  `Def` )VALUES("", "'+thirdletter+secondletter+letter+'","'+noQuote(noHTML(page_source[beginDef+30:beginDef+endDef]))+'");')
                                #file.close()
                                #array.append('INSERT INTO  `Dic` (  `id` ,  `Term` ,  `Def` )VALUES("", "'+thirdletter+secondletter+letter+'","'+noQuote(noHTML(page_source[beginDef+30:beginDef+endDef]))+'");')

                        if x <= 11:
                            x = x + 1

                        else:
                            x = 0

                    except:
                        time.sleep(5)
                        print 'Waiting for connection...'

    for key, value in dic.iteritems() :
        file = open('diclog.txt', "a")
        file.write('INSERT INTO  `Dic` (  `id` ,  `Term` ,  `Def` )VALUES("", "'+key+'","'+value+'");')
        file.close()
        
    print "\nWriting Items to file..."

    print "DONE!!!"
    raw_input()

main()
