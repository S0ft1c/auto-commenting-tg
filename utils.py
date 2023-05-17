def receive_target(db):
    # receive all targets to auto-comment
    targets = db.sql_req("select * from channels").fetchall()
    targets = [el[0] for el in targets]
    return targets
