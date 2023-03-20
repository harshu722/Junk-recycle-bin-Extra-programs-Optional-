import re  
line = "Learn Python through tutorials on javatpoint"  
match_object = re.match( r'.w* (.w?) (.w*?)', line, re.M|re.I)  
  
if match_object:  
    print ("match object group : ", match_object.group())  
    print ("match object 1 group : ", match_object.group(1))  
    print ("match object 2 group : ", match_object.group(2))  
else:  
    print ( "There isn't any match!!" )
