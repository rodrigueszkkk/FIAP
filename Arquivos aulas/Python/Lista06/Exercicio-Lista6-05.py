String = ("Gabriel", "Amanda", "Jonathan", "Lucas", "Ana")
def maior_string(tupla):
    return max(tupla, key=len)

print(maior_string(String))
