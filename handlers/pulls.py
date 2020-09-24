#! /usr/bin/env python
import requests
auth = 'xafonya@gmail.com'
passwd = 'CXen40cats'


def request(par):
    response = requests.get(
        'https://api.github.com/repos/alenaPy/devops_lab/pulls', auth=(auth, passwd), params=par)
    test = response.json()
    return test


def result(test):
    res = []
    for i in range(len(test)):
        num = test[i]["number"]
        link = test[i]["html_url"]
        title = test[i]["title"]
        result = {"num": num, "title": title, "link": link}
        res.append(result)
        i += 1
    return res


def get_pulls(state):
    if state == 'open' or state == 'closed':
        par = {'per_page': 100, 'state': state}
        test = request(par)
        res = result(test)
        return res
    else:
        par = {'per_page': 100, 'state': "all"}
        test = request(par)
        if state == 'accepted' or state == 'needs work':
            res = []
            for i in range(len(test)):
                if test[i]["labels"] and test[i]["labels"][0]["name"] == state:
                    num = test[i]["number"]
                    link = test[i]["html_url"]
                    title = test[i]["title"]
                    resul = {"num": num, "title": title, "link": link}
                    res.append(resul)
                    i += 1
            return res
        else:
            res = result(test)
            return res
