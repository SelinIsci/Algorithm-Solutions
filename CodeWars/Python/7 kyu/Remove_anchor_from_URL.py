def remove_url_anchor(url):
    new_url = []

    for c in url:
        if c == "#":
            break
        new_url.append(c)
    return "".join(new_url)
