from glimps_custom_modules.action_youpi import Youpi, Arguments


def test_glimps():
    res = Youpi().run(Arguments())
    assert res == {"text": "youpi"}
