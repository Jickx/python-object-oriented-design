from collection import Collection


raw = [{'name': 'istambul', 'country': 'turkey'},
       {'name': 'Moscow ', 'country': ' Russia'},
       {'name': 'iStambul', 'country': 'tUrkey'},
       {'name': 'antalia', 'country': 'turkeY '},
       {'name': 'samarA', 'country': '  ruSsiA'}]


def format(raw):
    c = Collection(raw)
    return c.map_(lambda row: {'name': row['country'].lower().strip(), 'country': row['name'].lower().strip()}).unique().group_by(lambda row: (row['name'], row['country'])).sort_by(lambda row: sorted(list(row.keys()))).all()


expected = [{'russia': ['moscow', 'samara']},
            {'turkey': ['antalia', 'istambul']}]


def test_format():
    print(format(raw))
    print(expected)
    assert format(raw) == expected

test_format()
