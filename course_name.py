# your code goes here

d1 = {
      "id1": {

    "name": "Course Name 1",

    "category": "Category1",

    "type": "Type 1"

  },

  "id2": {

    "name": "Course Name 2",

    "category": "Category1",

    "type": "Type 1"

  },

  "id3": {

    "name": "Course Name 3",

    "category": "Category1",

    "type": "Type 1"

  },

  "id4": {

    "name": "Course Name 4",

    "category": "Category1",

    "type": "Type 2"

  },

  "id5": {

    "name": "Course Name 5",

    "category": "Category2",

    "type": "Type 2"

  },

  "id6": {

    "name": "Course Name 6",

    "category": "Category2",

    "type": "Type 3"

  },

  "id7": {

    "name": "Course Name 7",

    "category": "Category2",

    "type": "Type 3"

  }
}
#Output
#[
 # {

 #    "name": "Category1",

 #    "courses": ["Course Name 1", "Course Name 2", "Course Name 3", "Course Name 4"]

 #  },

 #  {

 #    "name": "Category2",

 #    "courses": ["Course Name 5", "Course Name 6", "Course Name 7"]

 #  }
 #]
list3 = []
courseKey = {}
count=0
for x in d1.values() :
    
        if  x['category'] not in courseKey.keys():
            courseKey[x['category']]=count;
            count+=1
            temp_dict2 = dict()
            temp_dict2['name']=x['category']
            temp_dict2['courses']=[x['name']]
            list3.append(temp_dict2)
        else:
            list3[courseKey[x['category']]]['courses'].append(x['name'])
            
print(list3)
