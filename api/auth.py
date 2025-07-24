import os

def is_authorized(is_group, from_id: int, user_name: str, chat_id, group_name) -> bool:
    if os.getenv("AUCH_ENABLE", "0") == "0":
        return True

    allowed_users = os.getenv("ALLOWED_USERS", "").split(",")
    allowed_groups = os.getenv("ALLOWED_GROUPS", "").split(",")

    if is_group:
        if str(group_name).lower() in [g.lower() for g in allowed_groups] or str(chat_id) in allowed_groups:
            return True
    else:
        if str(user_name).lower() in [u.lower() for u in allowed_users] or str(from_id) in allowed_users:
            return True

    return False


def is_admin(from_id: int) -> bool:
    return str(from_id) == os.getenv("ADMIN_ID", "")