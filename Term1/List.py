import random
highScore = [1012,950,850,700,675,550,443,414,395,380]
prices = [9.99, 10.25, 19.99]
topGames = ["The Witness","Ninja Gaiden","Minecraft","Ark Survival Evolved",
            "League of Legends","Dead Rising 3","Dead by Daylight"
            ,"Assassin’s Creed Syndicate","Guitar Hero Live","Forza 5",
            "WarFrame","Fallout 4","Overwatch","Skyrim","Slime Ranchers",
            "Red Dead Redemption 2","Layers of Fear","Dark Souls 3",
            "Castle Crashers","For Honor"
            ]
if "fortnite" in topGames:
    print("fail")
elif topGames[0] == "World of Warcraft":
    print("fail")
else:
    print("Congrants You Have Passed!")
print(len(topGames))
for i in range(0, 4):
    print(topGames[i])
randomnum = random.randint(0,len(topGames))
print(topGames[randomnum])


worstGames = ["FortNite","Smite","COD Infinite Warfare","Apb Reloaded",
              "Halo","Warface","World of Warcraft","Onigiri","Hitman","Star Wars Lego"]
print(worstGames[2:5])
