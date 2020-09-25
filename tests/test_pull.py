from unittest import TestCase

import handlers.pull as pull
j = [
    {
        "number": "1",
        "html_url": "http://",
        "title": "open",
        "state": "open",
        "labels": []

    },
    {
        "number": "2",
        "html_url": "http://",
        "title": "closed",
        "state": "closed",
        "labels": []
    },
    {
        "number": "3",
        "html_url": "http://",
        "title": "open_accepted",
        "state": "open",
        "labels":
            [{"name": "accepted"}]
    },
    {
        "number": "4",
        "html_url": "http://",
        "title": "closed_accepted",
        "state": "closed",
        "labels":
            [{"name": "accepted"}]
    },
    {"number": "5",
        "html_url": "http://",
        "title": "open_needs_work",
        "state": "open",
        "labels":
            [{"name": "needs work"}]
     },
    {
        "number": "6",
        "html_url": "http://",
        "title": "closed_needs_work",
        "state": "closed",
        "labels":
            [{"name": "needs work"}]
    }
]


class Testpull(TestCase):

    def setUp(self):
        """Init"""

    def test_result(self):
        """Test for _result"""
        res_result = [
            {
                "num": "1",
                "title": "open",
                "link": "http://",
            },
            {
                "num": "2",
                "title": "closed",
                "link": "http://",
            },
            {
                "num": "3",
                "title": "open_accepted",
                "link": "http://",
            },
            {
                "num": "4",
                "title": "closed_accepted",
                "link": "http://",
            },
            {
                "num": "5",
                "title": "open_needs_work",
                "link": "http://",
            },
            {
                "num": "6",
                "title": "closed_needs_work",
                "link": "http://",
            },
        ]
        res_result_open = [
            {
                "num": "1",
                "title": "open",
                "link": "http://",
            },
            {
                "num": "3",
                "title": "open_accepted",
                "link": "http://",
            },
            {
                "num": "5",
                "title": "open_needs_work",
                "link": "http://",
            }
        ]
        res_result_closed = [
            {
                "num": "2",
                "title": "closed",
                "link": "http://",
            },
            {
                "num": "4",
                "title": "closed_accepted",
                "link": "http://",
            },
            {
                "num": "6",
                "title": "closed_needs_work",
                "link": "http://",
            },
        ]
        res_result_accepted = [
            {
                "num": "3",
                "title": "open_accepted",
                "link": "http://",
            },
            {
                "num": "4",
                "title": "closed_accepted",
                "link": "http://",
            },
        ]
        res_result_need = [
            {
                "num": "5",
                "title": "open_needs_work",
                "link": "http://",
            },
            {
                "num": "6",
                "title": "closed_needs_work",
                "link": "http://",
            },
        ]

        self.assertEqual(pull._result(j, "open"), res_result_open)
        self.assertEqual(pull._result(j, "closed"), res_result_closed)
        self.assertEqual(pull._result(j, "accepted"), res_result_accepted)
        self.assertEqual(pull._result(j, "needs work"), res_result_need)
        self.assertEqual(pull._result(j), res_result)

    def test_get_params(self):
        """Test for _result"""
        self.assertEqual(pull.get_params("open"), {
                         'per_page': 100, 'state': 'open'})
        self.assertEqual(pull.get_params("closed"), {
                         'per_page': 100, 'state': 'closed'})
        self.assertEqual(pull.get_params("acepted"), {
                         'per_page': 100, 'state': 'all'})
        self.assertEqual(pull.get_params("needs work"), {
                         'per_page': 100, 'state': 'all'})
        self.assertEqual(pull.get_params(
            ""), {'per_page': 100, 'state': 'all'})

    def tearDown(self):
        """Finish"""
