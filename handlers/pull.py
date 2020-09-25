#! /usr/bin/env python
import requests
auth = 'xafonya@gmail.com'
passwd = 'cxAfonya40cats'


def _request(par):
    response = requests.get(
        'https://api.github.com/repos/alenaPy/devops_lab/pulls', params=par)
    test = response.json()
    return test


def _result(test, state=None):
    if state == 'open' or state == 'closed':
        res = []
        for i in range(len(test)):
            if test[i]["state"] == state:
                num = test[i]["number"]
                link = test[i]["html_url"]
                title = test[i]["title"]
                result = {"num": num, "title": title, "link": link}
                res.append(result)
                i += 1
        return res
    elif state == 'accepted' or state == 'needs work':
        res = []
        for i in range(len(test)):
            if test[i]["labels"] and test[i]["labels"][0]["name"] == state:
                num = test[i]["number"]
                link = test[i]["html_url"]
                title = test[i]["title"]
                result = {"num": num, "title": title, "link": link}
                res.append(result)
                i += 1
        return res
    else:
        res = []
        for i in range(len(test)):
            num = test[i]["number"]
            link = test[i]["html_url"]
            title = test[i]["title"]
            result = {"num": num, "title": title, "link": link}
            res.append(result)
            i += 1
        return res


def get_params(state=None):
    if state == 'open' or state == 'closed':
        par = {'per_page': 100, 'state': state}
    else:
        par = {'per_page': 100, 'state': "all"}
    return par


def get_pulls(state):
    par = get_params(state)
    test = _request(par)
    res = _result(test, state)
    return res


if __name__ == "__main__":
    state = None
    get_pulls(state)
