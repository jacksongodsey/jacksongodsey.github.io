def quality_control(num, original_thresh):
    list_item = []
    for x in range(num):
        qa_list = input()
        thresh = int(input())
        if thresh < original_thresh:
            print(qa_list)
            list_item.append(qa_list[x])
    print(len(list_item), 'failed.')
    print(len(list_item))
    return len(list_item)

if __name__ == '__main__':
    original_thresh = int(input())
    num = int(input())
    quality_control(num, original_thresh)