import os
from uuid import uuid4

from flask import Flask, request, render_template, send_from_directory


app = Flask(__name__)
# app = Flask(__name__, static_folder="images")



APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
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
    image_names = os.listdir('./images')
    return render_template("complete_display_image.html", image_list=image_names, number = 0, count = 0)

@app.route('/upload/<filename>')
def send_image(filename):
    return send_from_directory("images", filename)


count = 0
@app.route('/gallery/', methods = ["POST"])
def get_gallery():
    global count
    image_names = os.listdir('./images')
    if request.method == 'POST':
        if request.form['category'] == 'overweight':
            source = os.path.join(APP_ROOT, 'images/') + image_names[0]
            destination = os.path.join(APP_ROOT, 'sorted/overweight/') + image_names[0]
            os.rename(source, destination) 
        elif(request.form['category'] == 'normalweight'):
            source = os.path.join(APP_ROOT, 'images/') + image_names[0]
            destination = os.path.join(APP_ROOT, 'sorted/normalweight/') + image_names[0]
            os.rename(source, destination) 
        else:
            source = os.path.join(APP_ROOT, 'images/') + image_names[0]
            os.remove(source)
    image_names = os.listdir('./images')
    count += 1
    if(len(image_names) == 0):
        return render_template("end.html")
    else: 
        return render_template("complete_display_image.html", image_list=image_names, number = 0, count = count)


if __name__ == "__main__":
    app.run(port=4555, debug=True)
