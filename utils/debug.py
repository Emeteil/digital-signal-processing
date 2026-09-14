import builtins

try:
    import icecream
    from icecream import install

    icecream.icecream.has_non_ascii_chars = lambda s: False

    install()
except ImportError:
    builtins.ic = lambda *a: None if not a else (a[0] if len(a) == 1 else a)
