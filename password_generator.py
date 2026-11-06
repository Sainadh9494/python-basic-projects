import string 
import random

class PasswordGenerator:
    def chartacters(self):
        ascii_characters=string.ascii_letters
        digits=string.digits
        special_characters=string.punctuation
        all_characters=ascii_characters+digits+special_characters
        return all_characters
    def genreate_password(self,length):
        all_characters=self.chartacters()
        characters=list(all_characters)
        characters=random.shuffle(characters)
        password=""
        self.l=length
        for i in range(length):
            password+=random.choice(all_characters)
        return password
    def run(self):
        try:
            print("========== PASSWORD GENERATOR ==========")
            length=int(input("ENTER THE LENGTH OF THE PASSWORD : "))
            if(length<=2):
                print("the length of the password should at least 1")
                return
            else:
                password=self.genreate_password(length)
                print(f"GENERATED PASSWORD : {password}")
        except  ValueError:
            print("enter the valid numerical value")

p1=PasswordGenerator()
p1.run()


