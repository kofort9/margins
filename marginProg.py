# Margin Code

# Kofi Fort

# input: text file with 2 integers(inches) with other text.
    
def getfile(filname):
  f = open(filname, "r")
  if f.mode == 'r':
    file = f.readlines()
    return file
  
def main():
  file = getfile("Input.TXT")
  # gets the margins puts L + R in a list from the first line
  margins = [int(i) for i in file[0].split(",")]
  fileoutput = open("DAT2.TXT", "w") 
  fileoutput.write("*"*80+"\n")
  del file[0]
  # Assume
  Lmargin = margins[1]*"*"
  Rmargin = margins[0]*"*"
  linelength = 79
  linemax = linelength - margins[1] - margins[0]
  currentlinelen = linemax
  wordlist = []
  fullstring = ""
  
  #_______________________
  # read in words from input file
  for line in file:
  # Store word in list
    wordlist += line.split()
  # for words in list
  formattedstr = Lmargin
  #print(wordlist)
  for word in wordlist:
    if currentlinelen - len(word) < 0:
      formattedstr += Rmargin+"\n"
      currentlinelen = linemax - len(word)+1
      fullstring += formattedstr 
      formattedstr = Lmargin+word+" "


    else:
      # base prints for end of sentences and regular words
      if word[len(word)-1] == ".":
        if currentlinelen - (len(word)+3-margins[0]) < 0:
          formattedword = word
          formattedstr += formattedword
          currentlinelen -= 2+len(word) 
        else:
          formattedword = word+"  "
          formattedstr += formattedword
          currentlinelen -= 2+len(word) 
      else:
      # regular word
        if currentlinelen - len(word)+2-margins[0] < 0:
          formattedword = word
          formattedstr += formattedword
          currentlinelen -=1+len(word)
        else:
          formattedword = word+" "  
          formattedstr += formattedword
          currentlinelen -= 1+len(word)
      # add word to formatted string  


  fileoutput.write(fullstring)
  fileoutput.write(formattedstr)

  

  fileoutput.close()
  
  
  
  
if __name__ =="__main__":
  main()