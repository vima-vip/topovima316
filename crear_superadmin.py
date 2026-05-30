from app import app, db, User
from sqlalchemy import inspect, text

with app.app_context():
    inspector = inspect(db.engine)
    cols = [c['name'] for c in inspector.get_columns('user')]
    if 'role' not in cols:
        db.session.execute(db.text('ALTER TABLE user ADD COLUMN role VARCHAR(20) NOT NULL DEFAULT "user"'))
        db.session.commit()

    admin = User.query.filter_by(username='superadmin').first()
    if admin:
        db.session.delete(admin)
        db.session.commit()

    admin = User(username='superadmin', role='superadmin')
    admin.set_password('Z0p0rt32026*')
    db.session.add(admin)
    db.session.commit()
    print('Superadmin creado correctamente')