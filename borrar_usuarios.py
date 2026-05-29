from app import app, db, User

with app.app_context():
    usernames_a_borrar = ["admin", "venus"]

    for username in usernames_a_borrar:
        usuario = User.query.filter_by(username=username).first()
        if usuario:
            db.session.delete(usuario)
            print(f"Usuario borrado: {usuario.username}")
        else:
            print(f"No existe: {username}")

    db.session.commit()

    print("\nUsuarios restantes:")
    for u in User.query.all():
        print(u.id, u.username)