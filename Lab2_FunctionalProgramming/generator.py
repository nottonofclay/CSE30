# items_original = [1, 2, 3, 4]

# def permute(items):
#     if len(items) <= 1:
#         print('stop')
#     else:
#         yield items

# print(permute(items_original))

# def anagram_generator(items_original):
#     for items_permuted in permute(items_original[1:]):
#         for i in range(len(items_original)):
#             yield items_permuted[:i] + items_original[0:1] + items_permuted[i:]


# print(list(anagram_generator(items_original)))


def all_perms(elements):
    print(f'These are the elements: {elements}')
    if len(elements) <=1:
        yield elements
    else:
        print(all_perms(elements[1:]))
        for perm in all_perms(elements[1:]):
            print(f'all_perms:{perm}')
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]

print (list(all_perms([1, 2, 3])))
