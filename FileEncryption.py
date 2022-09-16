infile = open("info_security.txt", "r")
codes = {"a":"Z","b":"Y","c":"X","d":"W","e":"V","f":"U","g":"T","h":"S","i":"R","j":"Q","k":"P","l":"O","m":"N","n":"M","o":"L","p":"K","q":"J","r":"I","s":"H","t":"G","u":"F","v":"E","w":"D","x":"C","y":"B","z":"A","A":"0","B":"1","C":"2","D":"3","E":"4","F":"5","G":"6","H":"7","I":"8","J":"9","K":"!","L":"@","M":"#","N":"$","O":"%","P":"^","Q":"&","R":"*","S":"(","T":")","U":"-","V":"+","W":"=","X":"?","Y":"<","Z":">"}

for paragraph in infile:
    paragraph = str(paragraph)

result = ''

for i in paragraph:
    if i in codes:
        result = result + codes[i]
    else:
        result = result + i

outfile = open("encrypted.txt","w")
outfile.write(result)
infile.close()
outfile.close()
