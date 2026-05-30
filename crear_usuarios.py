from app import app, db, User

with app.app_context():
    db.create_all()

    datos = [
        ("Warcentales", "00149147"),
        ("Ldelacruz", "02153294"),
        ("Hdiaz", "00197038"),
        ("Renciso", "00091832"),
        ("Czuniga", "01037432"),
        ("Cchavez", "prueba123"),
    ]

    for username, password in datos:
        existe = User.query.filter_by(username=username).first()
        if not existe:
            nuevo = User(username=username)
            nuevo.set_password(password)
            db.session.add(nuevo)

    db.session.commit()

    usuarios = User.query.all()
    for u in usuarios:
        print(u.id, u.username)