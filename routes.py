# routes.py
from flask import render_template, redirect, url_for, request, session, flash
from app import app, db
from models import User
import random

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form.get('username').strip()
        if not username:
            flash('Username cannot be empty.', 'error')
            return redirect(url_for('index'))
        
        # Check if username already exists
        user = User.query.filter_by(username=username).first()
        if user:
            flash('Username already taken. Please choose another one.', 'error')
            return redirect(url_for('index'))
        
        # Add user to the database
        new_user = User(username=username)
        db.session.add(new_user)
        db.session.commit()
        
        # Initialize session
        session['username'] = username
        session['random_number'] = random.randint(1, 100)  # Define range as needed
        session['guess_count'] = 0
        
        flash(f'Welcome, {username}! Let\'s start the game.', 'success')
        return redirect(url_for('game'))
    return render_template('index.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    if 'username' not in session:
        flash('Please enter a username to start the game.', 'error')
        return redirect(url_for('index'))
    
    message = ''
    if request.method == 'POST':
        try:
            guess = int(request.form.get('guess'))
        except ValueError:
            flash('Please enter a valid integer.', 'error')
            return redirect(url_for('game'))
        
        session['guess_count'] += 1
        random_number = session.get('random_number')
        
        if guess < random_number:
            message = 'Higher!'
        elif guess > random_number:
            message = 'Lower!'
        else:
            message = f'Congratulations, {session["username"]}! You guessed it in {session["guess_count"]} attempts.'
            
            # Update user's guess count in the database
            user = User.query.filter_by(username=session['username']).first()
            if user:
                # If the user has previous guess counts, keep the minimum (best score)
                user.guess_count = min(user.guess_count, session['guess_count']) if user.guess_count > 0 else session['guess_count']
                db.session.commit()
            
            # Reset the game
            session['random_number'] = random.randint(1, 100)
            session['guess_count'] = 0
            
            flash(message, 'success')
            return redirect(url_for('game'))
    
    return render_template('game.html', message=message, guess_count=session.get('guess_count', 0))

@app.route('/scoreboard')
def scoreboard():
    users = User.query.order_by(User.guess_count.asc()).all()
    return render_template('scoreboard.html', users=users)

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('index'))