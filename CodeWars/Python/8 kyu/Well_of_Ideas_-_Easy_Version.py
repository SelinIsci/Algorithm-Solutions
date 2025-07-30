def well(x):
    good_count = x.count("good")
    if good_count == 0:
        return "Fail!"
    elif good_count <= 2:
        return "Publish!"
    else:
        return "I smell a series!"
