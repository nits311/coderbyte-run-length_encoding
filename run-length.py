'''Question:Have the function RunLength(str) take the str parameter being passed
and return a compressed version of the string using the Run-length 
encoding algorithm. This algorithm works by taking the occurrence of 
each repeating character and outputting that number along with a single 
character of the repeating sequence. For example: "wwwggopp" would return 3w2g1o2p. 
The string will not contain any numbers, punctuation, or symbols.'''


def StringChallenge(strParam):

  ctr = 0;
  output = "";
  data = strParam[0];

  for i in range(0, len(strParam)):  
    if(strParam[i] == data):
        ctr = ctr+1
    else:
      output += (str(ctr)+data)
      data = strParam[i]
      ctr = 1
       
  temp = str(ctr)+data
  output += temp
  return output

  # code goes here
  #return strParam

# keep this function call here 
print StringChallenge(raw_input())
