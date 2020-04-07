from flask import Blueprint, request, redirect, render_template, url_for
from flask.views import MethodView
from tumblelog.models import Post, Comment
from flask_mongoengine.wtf import model_form
from tumblelog import cache

posts = Blueprint('posts', __name__, template_folder='templates')

class ListView(MethodView):
    
    form = model_form(Post, exclude=['created_at'])
    @cache.memoize()
    def get(self):
        form = self.form(request.form)
        posts = Post.objects.all()
        return render_template('posts/list.html', posts=posts, form=form)
    @cache.memoize()
    def post(self):
        form = self.form(request.form)

        if form.validate():
            _post = Post()
            form.populate_obj(_post)
            _post.save()
            return redirect(url_for('posts.list'))
        return render_template('posts/list.html', posts=posts, form=form)

class DetailView(MethodView):
    
    form = model_form(Comment, exclude=['created_at'])

    def get_context(self, tag):
        post = Post.objects.get_or_404(tag=tag)
        form = self.form(request.form)

        context = {
            "post": post,
            "form": form
        }
        return context
    @cache.memoize()
    def get(self, tag):
        context = self.get_context(tag)
        return render_template('posts/detail.html', **context)
    @cache.memoize()
    def post(self, tag):
        context = self.get_context(tag)
        form = context.get('form')

        if form.validate():
            comment = Comment()
            form.populate_obj(comment)

            post = context.get('post')
            post.comments.append(comment)
            post.save()

            return redirect(url_for('posts.detail', tag=tag))

        return render_template('posts/detail.html', **context)


# Register the urls
posts.add_url_rule('/', view_func=ListView.as_view('list'))
posts.add_url_rule('/<tag>/', view_func=DetailView.as_view('detail'))