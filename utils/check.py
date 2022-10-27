def check_username_valid(username):
    """
    判断用户名是否合法
    """
    flags = set('1234567890abcdefghijklmnopqrstuvwxyz')
    if not 4 <= len(username) <= 8:
        return False
    if (set(username.lower()) - flags):
        return False
    return True


if __name__ == '__main__':
    print(check_username_valid("hello."))
