from app import app, db, User
from sqlalchemy import inspect, text

with app.app_context():
    inspector = inspect(db.engine)
    cols = [c['name'] for c in inspector.get_columns('user')]
    if 'role' not in cols:
        db.session.execute(text('ALTER TABLE user ADD COLUMN role VARCHAR(20) NOT NULL DEFAULT "user"'))
        db.session.commit()

    datos = [
        ('Warcentales', '00149147'),
        ('Ldelacruz', '02153294'),
        ('Hdiaz', '00197038'),
        ('Renciso', '00091832'),
        ('Czuniga', '01037432'),
        ('Cchavez', 'prueba123'),
    ]

    for username, password in datos:
        username = username.lower()
        existe = User.query.filter_by(username=username).first()
        if not existe:
            nuevo = User(username=username, role='user')
            nuevo.set_password(password)
            db.session.add(nuevo)

    db.session.commit()
    print('Usuarios creados correctamente')