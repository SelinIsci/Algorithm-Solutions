def likes(names):
    n = len(names)
    return (
        "no one likes this"
        if n == 0
        else (
            "{} likes this".format(names[0])
            if n == 1
            else (
                "{} and {} like this".format(*names)
                if n == 2
                else (
                    "{}, {} and {} like this".format(*names)
                    if n == 3
                    else "{}, {} and {} others like this".format(
                        names[0], names[1], n - 2
                    )
                )
            )
        )
    )
