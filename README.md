# README -- CA1, BackEnd, Suzor Antonin

## Buildings app

#### CRUD operations
All 4 CRUD operations have been implemented:
* Create has been implemented using a CreateView at 'buildings/new/'
* Read has been implemented using a DetailView at 'buildings/detail/**[pk]**/'
* Update has been implemented using a UpdateView at 'buildings/modify/**[pk]**/'
* Delete has been implemented using a DeleteView at 'buildings/delete/**[pk]**/'

#### Data Stored
The data stored is information about buildings:
* Name of the building, number of floors
* Main color of the building, whether it is residential or not
* Address of the building, divided in 4 fields 'country', 'city', 'street', and 'number'

#### FrontEnd
Simple front-end has been added:
* Grey background to not burn the user's eyes
* Blue header to liven up the screen
* Black links to contrast with the background

#### Navigation
App navigation can be done through explicit links, or through links inside the web pages.

#### Comments
Not too many comments were added, since code is lightweight and explicit enough.

#### Developing process
Development went through the following stages:
* URL structure
* Creation of 'Building' model
* Creation of 'SortPkView'
* Creation of CRUD views
* Creation of other views
* Commenting
* README writing
