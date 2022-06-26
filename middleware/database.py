db = {}


def save_item(item_id: int, item: dict):
    db[item_id] = item
    return item


def get_item(item_id: int):
    return db.get(item_id)


def get_all_items():
    return db


def delete_item(item_id: int):
    if item_id in db:
        del db[item_id]
        return True
    return False


def update_item(item_id: int, item: dict):
    if item_id in db:
        db[item_id].update(item)
        return db[item_id]
    return None
