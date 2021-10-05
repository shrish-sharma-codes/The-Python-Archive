    def anagramCheck2(str1,str2):  
        list1 = list(str1)  
        list2 = list(str2)  
        # Sort the list value  
        list1.sort()  
        list2.sort()  
      
        position = 0  
        matches = True  
      
        while position < len(str1) and matches:  
            if list1[position]==list2[position]:  
                position = position + 1  
            else:  
                matches = False  
      
        return matches  
      
    print(anagramCheck2('python','ythonp'))  
