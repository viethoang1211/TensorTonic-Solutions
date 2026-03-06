def text_chunking(tokens, chunk_size, overlap):
    """
    Split tokens into fixed-size chunks with optional overlap.
    """
    # Write code here
    n = len(tokens)
    l = 0
    r =chunk_size
    stride = chunk_size - overlap
    ans = []
    if n == 0:
        return ans
    while l < n:
        if r >= n and l < n:
            ans.append(tokens[l:])
            return ans
        ans.append(tokens[l:r])
        l += stride
        r += stride