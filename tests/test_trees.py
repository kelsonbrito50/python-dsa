from src.trees.bst import BST


def test_insert_and_inorder():
    bst = BST()
    for val in [5, 3, 7, 1, 4]:
        bst.insert(val)
    assert bst.inorder() == [1, 3, 4, 5, 7]


def test_search():
    bst = BST()
    for val in [5, 3, 7]:
        bst.insert(val)
    assert bst.search(3) is True
    assert bst.search(99) is False
