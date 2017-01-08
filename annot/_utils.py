import hashlib


def _annotations_to_script(annotations, post_init):
    """
    Return a script of an initializer for *annotations*.
    """
    def fmt_setter(attr_name):
        # TODO: need to asign into another way, not ir works only with build in types
        return f"self.{attr_name!s} = {attr_name!s}"

    def fmt_args(attr_name, type):
        return f"{attr_name!s}: {type.__name__!s}"

    args, lines = [], []

    for attr_name, attr_type in annotations.items():
        args.append(fmt_args(attr_name, attr_type))
        lines.append(fmt_setter(attr_name))

    if post_init:
        lines.append("self.__annots_post_init__()")

    return """\
def __init__(self, {args}):
    {lines}
""".format(args=", ".join(args),
           lines="\n    ".join(lines) if lines else "pass")


def _annotations_to_init(cls):
    """
    Add a variables from __annotations__ to __init__ method.
    """
    annotations = getattr(cls, '__annotations__', {})

    sha1 = hashlib.sha1()
    sha1.update(repr(annotations).encode("utf-8"))
    unique_filename = "<annots generated init {0}>".format(
        sha1.hexdigest()
    )

    script = _annotations_to_script(
        annotations,
        getattr(cls, "__annots_post_init__", False),
    )

    locs = {}
    bytecode = compile(script, unique_filename, "exec")
    eval(bytecode, None, locs)
    return locs["__init__"]
