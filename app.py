from app import create_app, db
from scheduler.automate_jobs import start as start_scheduler
from flask.cli import with_appcontext
import click

app = create_app()

@app.cli.command("init-db")
@with_appcontext
def init_db():
    # Command to manually initialize the database
    db.create_all()
    click.echo("Initialized the database.")

if __name__ == '__main__':
    # Ensure DB is initialized, start scheduler, and run app
    with app.app_context():
        db.create_all()
    start_scheduler()
    app.run(debug=True)