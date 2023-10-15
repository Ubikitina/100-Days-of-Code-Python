import requests

USERNAME = "maialen"
TOKEN = "enter_your_token_here"

pixela_endpoint = "https://pixe.la/v1/users"

## ========================================================================================
## SECTION 1 - Create our user
## ========================================================================================

# We will create our user by using a post request
# Then we will comment this piece of code, because it's enough to run only once
# user_params = {
#     "token": TOKEN,
#     "username": USERNAME,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
#
# }
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)



## ========================================================================================
## SECTION 2 - Create our graph
## ========================================================================================

# # Now we will create our own graph
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"  # This is the API endpoint to be used for graph creation
#
# # Parameters to create the graph
# graph_config = {
#     "id": "graph1",
#     "name": "Cycling Graph",
#     "unit": "Km",
#     "type": "float",
#     "color": "ajisai"
# }
#
# # Authentication token. By using the header, the authentication is more secure than sending our token via parameters
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# # Post request to create the graph
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#
# # See the result of the post
# print(response.text)  # {"message":"Success.","isSuccess":true}, this means that the graph has been created successfully
#
# # Now we can see the graph created in https://pixe.la/v1/users/maialen/graphs/graph1





## ========================================================================================
## SECTION 3 - Post a pixel in the graph
## ========================================================================================

# pixel_posting_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1"  # This is the API endpoint to be used for pixel posting
#
# # Parameters
# request_body = {
#     "date": "20231009",
#     "quantity": "60.4"
# }
#
# # Authentication token. By using the header, the authentication is more secure than sending our token via parameters
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# # Post request to post a pixel
# response = requests.post(url=pixel_posting_endpoint, json=request_body, headers=headers)
#
# # See the result of the post
# print(response.text)  # {"message":"Success.","isSuccess":true}, this means that the pixel has been posted successfully



## ========================================================================================
## SECTION 4 - Update a pixel in the graph - put request type, https://docs.pixe.la/entry/put-pixel
## ========================================================================================
# pixel_putting_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20231013"  # This is the API endpoint to be used
#
# # Parameters
# request_body = {
#     "quantity": "10.4"
# }
#
# # Authentication token. By using the header, the authentication is more secure than sending our token via parameters
# headers = {
#     "X-USER-TOKEN": TOKEN
# }
#
# # Put request to update a pixel
# response = requests.put(url=pixel_putting_endpoint, json=request_body, headers=headers)
#
# # See the result of the post
# print(response.text)  # {"message":"Success.","isSuccess":true}, this means that the pixel has been updated successfully




## ========================================================================================
## SECTION 5 - Delete a pixel in the graph - delete request type, https://docs.pixe.la/entry/delete-pixel
## ========================================================================================
pixel_deleting_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/graph1/20231013"  # This is the API endpoint to be used

# No parameters needed this time

# Authentication token. By using the header, the authentication is more secure than sending our token via parameters
headers = {
    "X-USER-TOKEN": TOKEN
}

# Delete request to delete a pixel
response = requests.delete(url=pixel_deleting_endpoint, headers=headers)

# See the result of the post
print(response.text)  # {"message":"Success.","isSuccess":true}, this means that the pixel has been deleted successfully
