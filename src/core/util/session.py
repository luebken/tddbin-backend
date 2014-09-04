DEFAULT_SESSION_NAME_PREFIX = 'Untitled '

def generate_session_name(existing_names):
    if len(existing_names) == 0:
        return DEFAULT_SESSION_NAME_PREFIX + '1'

    used_postfixes = []
    for name in existing_names:
        name_left_over = name.replace(DEFAULT_SESSION_NAME_PREFIX, '')
        if name_left_over.isdigit():
            used_postfixes.append(int(name_left_over))
    used_postfixes.sort()
    new_postfix = used_postfixes[-1] + 1
    return DEFAULT_SESSION_NAME_PREFIX + str(new_postfix)

def get_or_generate_session_name(name, existing_names):
    if name:
        return name
    return generate_session_name(existing_names)

