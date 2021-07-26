Dict = {"key1": 1, "key2": "2", "key3": [3, 3, 3], "key4": (4, 4, 4), ('key5', "a"): 5, (0, 1): 6}

print(Dict)
release_year_dict = {"Thriller": "1982", "Back in Black": "1980",
                     "The Dark Side of the Moon": "1973", "The Bodyguard": "1992",
                     "Bat Out of Hell": "1977", "Their Greatest Hits (1971-1975)": "1976",
                     "Saturday Night Fever": "1977", "Rumours": "1977"}

thriller_ = release_year_dict["Thriller"]

print(thriller_)

print(release_year_dict.keys())
print(release_year_dict.values())
print(release_year_dict.items())