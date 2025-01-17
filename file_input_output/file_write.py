content = "hey Dushyant ! you are amazing"
txt = "\n this is a text"

f = open("/home/dushyant_new/python/file_input_output/file.txt", "w") #add "w" to open file in write mode
f.write(content)
f.write(txt)
f.close()
