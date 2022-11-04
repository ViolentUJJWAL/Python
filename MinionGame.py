def minion_game(string):
    # your code goes here
    c=len(string)
    kevin=0
    vowel=['A','E','I','O','U']
    for i in range(c):
        if (string[i] in vowel):
            kevin += (c-i)
    stuart = (c*(c+1)//2)-kevin

    print(f"kevin {kevin}\nstuart {stuart}")
            
if __name__ == '__main__':
    with open("word.txt", "r") as word:
        s=word.read()
    minion_game(s)