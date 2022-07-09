def get_save_name(name_str):
    return f'{"_".join(name_str.replace(":", "").replace("-", "").split())}.png'