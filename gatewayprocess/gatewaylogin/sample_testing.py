import random
class FamilyDetails(object):
    def __init__(self,node_range=1):
        self.graph = { "a" : ["c"]
              # "b" : ["c", "e"],
              # "c" : ["a", "b", "d", "e"],
              # "d" : ["c"],
              # "e" : ["c", "b"]
              # "f" : []
            }       
        self.node_range = node_range

    def details(self):
        """ to create final result with pair relationship """
        edges = []         
        for node in self.graph:
           for neighbour in self.graph[node]:
                node1 = ""
                neighbour1 = ""
                for data in self.generating(self.node_range):            
                    if neighbour in data.keys() :
                        neighbour1 = data[neighbour]                        
                    if node in data.keys() :
                        node1 = data[node]
                edges.append((node1, neighbour1))                
        return edges    

    def generating(self,*args):
        ''' to generate dynamic content in dictionary format '''        
        data_list  =  []        
        for i in range(args[0]):
            result_dict = {}
            dict1 = {}
            alphabet = []            
            for letter in range(97,97+args[0]):
                alphabet.append(chr(letter))
                      
            dict1['Name'] = alphabet[i]
            dict1['age'] = random.randint(1,90)

            result_dict[alphabet[i]] = dict1
            data_list.append(result_dict)            

        return data_list

'''Here node_range is to generate number of nodes dynamically '''

familyGraph = FamilyDetails(node_range=2)
print familyGraph.details()