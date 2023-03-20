List = ["Python", "Data", "Structures", "Tutorial"]  
print("The created Python list is: ")  
print(List)  
    
# Creating a multi-dimensional list using nested lists (list inside a list)  
List_ = [["Python", "Data"], ["Structures", "Tutorial"]]  
print("The multi-Dimensional list is: ")  
print(List_)  
    
# We can access the list of elements using the index of the element  
print("Single element: ", List[1])  
print("Multiple elements (slicing): ", List[0:2])  
print("For nested lists: ", List_[1][0])  
    
# We can access elements using negative indices also  
        
# printing the last element of the list  
print("Last element: ", List_[-1])  
        
# Slicing the list using negative indexing  
print("Last two elements: ", List[-1:-3:-1]) # Last first order  
