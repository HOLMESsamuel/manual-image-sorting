# manual-image-sorting
This is a small project to get used to python's library Flask. 
To train a neural network we need a lot of sorted images, this is really painful to sort them by hand if no such dataset already exists. With this app it becomes a lot easier.
You just have to enter the categories you want and then the app will allow you to see the images one by one and sort them with one click only.

# How to use it :

First, make sure you have python installed.

1. Download the whole manual-image-sorting folder.
2. Open a command window inside this folder and run pip install -r requirements.txt
3. Type "python app.py" in your command window.
4. In your web navigator go to localhost:4555 
5. Click on select files and select all the images you want to sort, when you are done click on upload files.
6. Enter the categories you want for your sorting, when you are done click on finished.
7. Now the images appear one by one and you can sort them by clicking on the buttons associated to your categories or delete the image.
8. When there are no more images to sort you can leave the app and your sorted images will be in manual-image-sorting folder in "sorted" with a subfolder per category.
