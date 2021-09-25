def merge(l_left, l_right):
    final_lst = []
    while len(l_left) > 0 and len(l_right) > 0:
        a = l_left[0]
        b = l_right[0]
        if a <= b:
            final_lst.append(l_left.pop(0))
        else:
            final_lst.append(l_right.pop(0))
    final_lst += l_left + l_right
    return final_lst

def m_s_asc(lst): 
    l_len = len(lst)
    if l_len == 0:
        raise ValueError
    elif l_len == 1:
        return lst
    elif l_len == 2:
        if lst[0] <= lst[1]:
            return lst
        elif lst[0] > lst[1]:
            lst[0], lst[1] = lst[1], lst[0]
            return lst
    else:
        l_left = lst[:l_len//2] 
        l_right = lst[l_len//2:]
        l_left = m_s_asc(l_left)
        l_right = m_s_asc(l_right)
        merged = merge(l_left, l_right)
        return merged

def merge_sort(lst, reversed = False):
    if reversed:
        return m_s_asc(lst)[::-1]
    else:
        return m_s_asc(lst)