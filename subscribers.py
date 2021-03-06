from flask import (
    Blueprint, flash, g, redirect, render_template, request, url_for
)
from werkzeug.exceptions import abort

from flaskr.auth import login_required
from flaskr.db import get_db

bp = Blueprint('subscribers', __name__)


@bp.route('/subscribers')
def index():
    db = get_db()
    posts = db.execute(
        'SELECT p.id, name, email, address, created, author_id, username'
        ' FROM subscribers p JOIN user u ON p.author_id = u.id'
        ' ORDER BY created DESC'
    ).fetchall()
    return render_template('subscribers/index.html', posts=posts)


@bp.route('/creation', methods=('GET', 'POST'))
@login_required
def create_subscribers():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        address = request.form['address']
        error = None

        if not name:
            error = 'Name is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'INSERT INTO subscribers (name, email, address, author_id)'
                ' VALUES (?, ?, ?, ?)',
                (name, email, address, g.user['id'])
            )
            db.commit()
            return redirect(url_for('subscribers.index'))

    return render_template('subscribers/create.html')


def get_subscribers(id, check_author=True):
    subscribers = get_db().execute(
        'SELECT p.id,  name,  email, address, created, author_id, username'
        ' FROM  subscribers p JOIN user u ON p.author_id = u.id'
        ' WHERE p.id = ?',
        (id,)
    ).fetchone()

    if subscribers is None:
        abort(404, "Post id {0} doesn't exist.".format(id))

    if check_author and subscribers['author_id'] != g.user['id']:
        abort(403)

    return  subscribers
    
    
@bp.route('/subscribers/<int:id>/update', methods=('GET', 'POST'))
@login_required
def update(id):
    subscribers = get_subscribers(id)

    if request.method == 'POST':
        name  = request.form['name']
        email = request.form['email']
        address = request.form['address']
        error = None

        if not name :
            error = 'Name is required.'

        if error is not None:
            flash(error)
        else:
            db = get_db()
            db.execute(
                'UPDATE  subscribers SET name = ?, email = ?, address =?'
                ' WHERE id = ?',
                (name, email, address, id)
            )
            db.commit()
            return redirect(url_for('subscribers.index'))

    return render_template('subscribers/update.html', subscribers=subscribers)


@bp.route('/subscribers/<int:id>/delete', methods=('POST',))
@login_required
def delete(id):
    get_subscribers(id)
    db = get_db()
    db.execute('DELETE FROM subscribers WHERE id = ?', (id,))
    db.commit()
    return redirect(url_for('subscribers.index'))

