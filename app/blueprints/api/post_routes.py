# from . import bp as api
# from app.models import Post
# from flask import request, make_response, g, abort
# from app.blueprints.auth.auth import token_auth


# # return all the posts the user follows
# @api.get('/posts')
# @token_auth.login_required()
# def get_posts():
#     user = g.current_user
#     posts = user.followed_posts()
#     response_list=[]
#     for post in posts:
#         response_list.append(post.to_dict())
#     return make_response({"posts":response_list},200)

# # returns a single post from its id
# @api.get('/posts/<int:id>')
# @token_auth.login_required()
# def get_single_post(id):
#     user = g.current_user
#     post = Post.query.get(id)
#     if not post:
#         abort(404)
#     # check to make sure the user has access to the post
#     if not user.is_following(post.author) and not post.author.id == user.id:
#         abort(403, description="No No No not in my House")
#     return make_response(post.to_dict(),200)


# # {
# #     "body": "the post body"
# # }

# # create a new post
# @api.post('/posts')
# @token_auth.login_required()
# def post_post():
#     posted_data = request.get_json() #retrieves the payload
#     u=g.current_user
#     post = Post(**posted_data)
#     post.save()
#     u.posts.append(post)
#     u.save()
#     return make_response(f"Post id: {post.id} created",200)

# # {
# #     "body": "the post body",
# #     "id":2
# # }
# @api.put('/posts')
# @token_auth.login_required()
# def put_post():
#     posted_data = request.get_json()
#     post = Post.query.get(posted_data['id'])
#     if not post:
#         abort(404)
#     if not post.author.id == g.current_user.id:
#         abort(403)
#     post.edit(posted_data['body'])
#     return make_response(f"Post id: {post.id} has been changed",200)

# # returns a single post from its id
# @api.delete('/posts/<int:id>')
# @token_auth.login_required()
# def delete_post(id):
#     user = g.current_user
#     post = Post.query.get(id)
#     if not post:
#         abort(404)
#     # check to make sure the user has access to the post
#     if not post.author.id == user.id:
#         abort(403, description="No No No not in my House")
#     post.delete()
#     return make_response(f"Success Post with id: {id} was deleted",200)
