import pickle


def filter_dump(filename, objects, typename):
    with open(filename, 'wb') as file:
        pickle.dump([obj for obj in objects if type(obj) == typename], file)
