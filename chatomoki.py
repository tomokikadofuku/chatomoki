class User():
    def __init__(self,name):
        self.name=name

    def response(says): 
        return says+"って何ですか？"   

print("こんにちは")


while True:
    user_name=input("あなたの名前は何ですか?:")
    
    if  user_name is not "":
        user=User(user_name)
        break



print("あなたの名前は"+user.name+"ですね")


while True:
    print(user.name+"さん:(あなた)")
    user_says=input()
    if user_says=="":
        while user_says=="":
            user_says=input("入力してください:")
    print(user_says+"って何ですか？")
    
    

