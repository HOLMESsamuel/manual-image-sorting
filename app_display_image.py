import os, shutil
from uuid import uuid4

from flask import Flask, request, render_template, send_from_directory


app = Flask(__name__)
# app = Flask(__name__, static_folder="images")



APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    folder = 'sorted/'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    folder = 'images/'
    for filename in os.listdir(folder):
        file_path = os.path.join(folder, filename)
        try:
            if os.path.isfile(file_path) or os.path.islink(file_path):
                os.unlink(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path)
        except Exception as e:
            print('Failed to delete %s. Reason: %s' % (file_path, e))
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}".format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist("file"):
        print(upload)
        print("{} is the file name".format(upload.filename))
        filename = upload.filename
        destination = "/".join([target, filename])
        print ("Accept incoming file:", filename)
        print ("Save it to:", destination)
        upload.save(destination)

    # return send_from_directory("images", filename, as_attachment=True)
    return render_template("category.html", category_list = [], len = 0)



@app.route("/category", methods = ["POST"])
def category():
    if request.method == 'POST':
        if request.form['validate'] == 'add category':
            cat = request.form['category']
            folder = 'sorted/'+ cat + '/'
            print(folder)
            newpath = os.path.join(APP_ROOT, folder)
            if not os.path.exists(newpath):
                os.makedirs(newpath)
            category_list = os.listdir('sorted/')
            return render_template("category.html", category_list = category_list, len = len(category_list))
        else:
            image_names = os.listdir('./images')
            category_list = os.listdir('sorted/')
            return render_template("complete_display_image.html", image_list=image_names, number = 0, count = 0, category_list = category_list, len = len(category_list))

             



@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)


count = 0
@app.route('/gallery/', methods = ["POST"])
def get_gallery():
    global count
    image_names = os.listdir('./images')
    category_list = os.listdir('sorted/')
    if request.method == 'POST':
        for category in category_list:
            if request.form['category'] == category:
                source = os.path.join(APP_ROOT, 'images/') + image_names[0]
                destination = os.path.join(APP_ROOT, 'sorted/' + category +'/') + image_names[0]
                os.rename(source, destination) 
        if request.form['category'] == "delete":
            source = os.path.join(APP_ROOT, 'images/') + image_names[0]
            os.remove(source)
    image_names = os.listdir('./images')
    count += 1
    if(len(image_names) == 0):
        return render_template("end.html")
    else: 
        category_list = os.listdir('sorted/')
        return render_template("complete_display_image.html", image_list=image_names, number = 0, count = count, category_list = category_list, len = len(category_list))


if __name__ == "__main__":
    app.run(port=4555, debug=True)
