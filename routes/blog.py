from flask import Flask, Blueprint, render_template, request, redirect, url_for
import csv 

blog_blueprint = Blueprint('blog', __name__)

@blog_blueprint.route('/blog')
def index():
    return render_template('blog.html')

def read_posts():
    posts = []
    with open('posts.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            posts.append(row)
    return posts

def write_post(post):
    with open('posts.csv', mode='a', newline='') as file:
        fieldnames = ['id', 'title', 'content', 'author']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writerow(post)

@blog_blueprint.route('/blog')
def blog():
    posts = read_posts()
    return render_template('blog.html', posts=posts)

@blog_blueprint.route('/post/<int:post_id>')
def post(post_id):
    posts = read_posts()
    post = next((p for p in posts if int(p['id']) == post_id), None)
    if post:
        return render_template('posts.html', post=post)
    else:
        return "Post not found", 404
    
@blog_blueprint.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        author = request.form['author']
            
            
        posts = read_posts()
        new_id = max([int(post['id']) for post in posts]) + 1 if posts else 1
            
            
        new_post = {
                'id': new_id,
                'title': title,
                'content': content,
                'author': author
        }
            
            
        write_post(new_post)
            
            
        return redirect(url_for('index'))

        return render_template('create.html')
