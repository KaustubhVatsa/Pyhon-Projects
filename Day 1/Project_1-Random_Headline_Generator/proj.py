import datetime
import random

subjects = [
    "My goldfish",
    "A confused programmer",
    "That one pigeon",
    "The Wi-Fi router",
    "My sleep schedule",
    "An angry potato",
    "A dancing robot",
    "The neighbour’s cat",
    "A suspicious avocado",
    "My alarm clock",
    "The invisible man",
    "A dramatic toaster",
    "The office chair",
    "My math teacher",
    "A ninja turtle",
    "The vending machine",
    "A lost sock",
    "My inner child",
    "A philosophical banana",
    "The ghost in my code"
]

actions = [
    "hacked into",
    "danced around",
    "screamed at",
    "fell in love with",
    "debugged",
    "started a fight with",
    "took a selfie with",
    "accidentally deleted",
    "rebooted",
    "sneezed on",
    "wrote poetry about",
    "painted graffiti on",
    "did yoga on",
    "uploaded memes to",
    "tried to eat",
    "argued with",
    "tripped over",
    "sent an email to",
    "proposed marriage to",
    "started worshipping"
]

objects = [
    "the fridge",
    "a microwave oven",
    "the moon",
    "the printer",
    "my last brain cell",
    "the university server",
    "a TikTok dance",
    "a haunted USB drive",
    "the cafeteria samosa",
    "a PowerPoint presentation",
    "the AI overlord",
    "a traffic cone",
    "the class whiteboard",
    "a broken keyboard",
    "the Wi-Fi signal",
    "a Minecraft pig",
    "a pile of laundry",
    "the exam paper",
    "a mysterious QR code",
    "the coffee machine"
]
print("Welcome to headline generator :")
with open("headline.txt","w", encoding="utf-8" , buffering=1) as file:
   while True:
      subject = random.choice(subjects)
      action = random.choice(actions)
      object = random.choice(objects)

      #ask for user input for next headline
      user_input = input("Would you like a headline ? (y/n): ")
      if user_input == "n":
         print ("Thanks for using headline generator :) ")
         break
      print(subject + " " + action + " " + object + ".")
      #save this to a text file with time stamp : 
      time_to_save = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
      to_save = f"{time_to_save} : BREAKING NEWS :: This just in {subject} {action} {object}.\n"
      file.write(str(to_save))
      file.flush()

