def top_scorer(class1):
    top_scorer = class1[0]
    
    for student in class1[1:]: 
        
        if student['score'] > top_scorer['score']:
            top_scorer = student
            if student['score'] == top_scorer['score']:
                if student['age'] < top_scorer['age']:
                    top_scorer = student
                
    return top_scorer



class1= [{"name": "Alice"},{"score": 85},{"age": 20},
          {"name": "Bob"},{"score": 92},{"age": 21},
          {"name": "David"},{"score": 92},{"age": 20}]

          
          
top_scorer = top_scorer(class1)

print(f"Top Scorer: {top_scorer['name']}")
print(f"Age: {top_scorer['age']}")
print(f"Score: {top_scorer['score']}")