def time_now(type=None):
    from urllib.request import urlopen
    res = urlopen('http://just-the-time.appspot.com/')
    result = res.read().strip()
    result_str = result.decode('utf-8')
    # res_splitted = result_str.split()
    #
    # if type == "date":
    #     return res_splitted[0]
    #
    # elif type == "time":
    #     return res_splitted[1]

    return result_str

# print(time_now())
# print(time_now("date"))
# print(time_now("time"))
