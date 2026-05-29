from app import app, db, User

with app.app_context():
    db.create_all()

    admin = User.query.filter_by(username="superadmin").first()
    if admin:
        db.session.delete(admin)
        db.session.commit()

    admin = User(username="superadmin", role="superadmin")
    admin.set_password("Z0p0rt32026*")
    db.session.add(admin)
    db.session.commit()
    print("Superadmin creado correctamente")