import requests
import json
#This script can be used to search for all files in a single folder
#and display the name ane the nodeid
#version 1.0
#4/10/2022
#author: Robert Wilds

url = "http://ec2-54-87-74-170.compute-1.amazonaws.com/alfresco/api/-default-/public/search/versions/1/search"

#search in face recognition reference images with node id: 7798dbc4-563a-4dfc-b26a-db3c1a3d7586
# any files that are already uploaded to S3 bucket won't return in the list (handled by seperate routine)
# the description will have FCref added if it's uploaded and excluded from the search (see query)
folderRequestDat = "{  \"query\": {    \"query\": \"SELECT cmis:name FROM cmis:document WHERE IN_FOLDER('7798dbc4-563a-4dfc-b26a-db3c1a3d7586') AND cm:description != 'FCref'\",    \"language\": \"cmis\"  }}"

temp = requests.post(url, data = folderRequestDat, auth = ('demo', 'demo'))

responseData = temp.json()
#print(responseData)

if "list" in responseData:  
        for item in responseData["list"]["entries"]:
            #dictval = json.dumps(item['entry']['properties'])
            print ('name -->' + item['entry']['name'])
            print ('node -->' + item['entry']['id'] + '\n') #this is a good spot to call a function to process each image
else:
    print('no items to process')
