def all_thing_is_obj(object: any) -> int:
    for name, value in globals().items():
        if value is object:
            typ = type(value)
            if "<class 'str'>" in str(typ):
                print(f"{name} is in the kitchen: {typ}")
            else:
                print(f"{name}: {typ}")
    return 42
