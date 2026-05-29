from app import app, db, User

with app.app_context():
    db.create_all()

    datos = [
        ("oyola", "00149147"),
        ("luis", "01137414"),
        ("prueba", "prueba123"),
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