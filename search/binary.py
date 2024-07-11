from data_structures.binary_tree import BinaryTree


def binary_search(target, root):
    if root:

        if int(target) == int(root.data):
            return True
        
        if int(target) < int(root.data):
            if binary_search(target, root.left):
                return True
            
        if int(target) > int(root.data):
            if binary_search(target, root.right):
                return True


def search(args):
    bst = BinaryTree()

    print("building tree....")
    bst.create_bst_from_file(args.file)
    print("tree built!")

    # bst.in_order_print(bst.root)

    print("Searching tree....")

    target = args.word

    if binary_search(target, bst.root):
        print("word found!")
        return
    else:
        print("word not found :(")
        return