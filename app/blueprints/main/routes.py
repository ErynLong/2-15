from .import bp as main
from app.models import Item
from flask import render_template, request, flash, redirect, url_for
import requests
from flask_login import login_required, current_user


@main.route('/', methods=['GET'])
@login_required
def index():
    return render_template('index.html.j2')

@main.route('/shop', methods=['GET', 'POST'])
@login_required
def shop():
    items = Item.query.all()
    return render_template('shop.html.j2', items=items)

@main.route('item/<int:id>')
@login_required
def get_item(id):
    item = Item.query.get(id)
    return render_template('single_item.html.j2', item=item, view_all=True)

@main.route('/view_cart', methods=['GET', 'POST'])
@login_required
def view_cart():
    display = current_user.user_cart
    return render_template('view_cart.html.j2', user_cart=display)

@main.route('/add_to_cart/<int:id>', methods=['GET', 'POST'])
@login_required
def add_to_cart(id):
    user = current_user
    item = Item.query.get(id)
    user.add_to_user_cart(item)
    return render_template('view_cart.html.j2', user_cart=user.user_cart)

@main.route('/delete_from_cart/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_from_cart(id):
    user = current_user
    item = Item.query.get(id)
    item.delete()
    flash('Your item has been removed from your cart.','danger')
    return redirect(url_for('main.view_cart'))

@main.route('/delete_cart/<int:id>', methods=['GET', 'POST'])
@login_required
def delete_cart(id):
    user = current_user
    item = Item.query.get(id)
    item.delete()
    flash('Your item has been removed from your cart.','danger')
    return redirect(url_for('main.view_cart'))