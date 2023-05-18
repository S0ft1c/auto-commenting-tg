def receive_target(db):
    # receive all targets to auto-comment
    targets = db.sql_req("select * from channels").fetchall()
    targets = [el[0] for el in targets]
    return targets


def receive_phrase(db):
    # receive all phrases that now on use
    phrases = db.sql_req("select * from phrases").fetchall()
    phrases = [el[0] for el in phrases]
    return phrases
