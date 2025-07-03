def domain_name(url):
    url = url.replace("http://", "").replace("https://", "").replace("www.", "")
    url = url.split("/")[0]
    return url.split(".")[0]
