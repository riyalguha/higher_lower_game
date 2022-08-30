from art import logo, vs
import random
from game_data import data
from replit import clear

def get_random_account():
  """Get data from random account"""
  return random.choice(data)

def format_data(account):
  """Format account into printable data:name,description,country"""
  name=account["name"]
  description=account["description"]
  country=account["country"]
  return f"{name},a {description},from {country} "

def check_answer(guess,a_followers,b_followers):
  """checks followers against users guess and returns TRUE if they got it right else return FALSE"""
  if a_followers>b_followers:
    return "a"
  else:
    return "b"

def game():
  print(logo)
  score=0
  account_a=get_random_account()
  account_b=get_random_account()
  while(2>1):
    account_a=account_b
    account_b=get_random_account()
    while account_a==account_b:
      account_b=get_random_account()
      print(f"Compare A: {format_data(account_a)}")
      print(vs)
      print(f"Compare B: {format_data(account_b)}")

      guess=input("Enter your guess type 'a' for A and type 'b' for B ").lower()
      a_follower=account_a["follower_count"]
      b_follower=account_b["follower_count"]
      is_correct=check_answer(guess, a_follower, b_follower)
      
      clear()
      print(logo)
      
      
      if is_correct==guess:
        score+=1
        print(f"You are right, your score {score}")
      else:
        print("Game Over")
        print(f"Here is your final score {score}")
        score=0
        break
      
game()     
      

  
# print(art.logo)
# score =0
# data_game=[]
# data_game=data
# len=len(data_game)
# j=random.randint(0,len)
# for i in data_game:
#   print(f"Compare A: {data_game[i]['name']}, a {data_game[i]['description']},and a {data_game[i]['country']}")
#   print(art.vs)
