from src.hashmaps.hashmap import HashMap


def test_put_and_get():
    hm = HashMap()
    hm.put("a", 1)
    hm.put("b", 2)
    assert hm.get("a") == 1
    assert hm.get("b") == 2


def test_missing_key():
    hm = HashMap()
    assert hm.get("missing") is None


def test_overwrite():
    hm = HashMap()
    hm.put("x", 10)
    hm.put("x", 20)
    assert hm.get("x") == 20
