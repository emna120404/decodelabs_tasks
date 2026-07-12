print("🎬 MOVIE TIME!!! 🎬")

print(" Hey! What is the genre of movie you are looking for? or type -exit- to quit. ")

# Topics
movie_genres = {
    "action": "You should check out Mad Max: Fury Road or John Wick. Non stop excitement!",
    "comedy": "If you want a good laugh, watch Superbad or The Hangover tonight! ",
    "horror": "In the mood for a scare? Go watch The Conjuring or Hereditary. ",
    "sci-fi": "If you like mind bending space stuff, Interstellar or Inception are perfect.",
    "drama": "For a really powerful story, check out The Shawshank Redemption or Whiplash."
}

while True:
    #the qs
    user_genre = input("You: ")
    
    #Clean the input text
    clean_text = user_genre.lower().strip()
    
    #Check for the exit command
    if clean_text == "exit":
        print("Bot: Goodbye! Enjoy your movie night.")
        break
        
    #Find the recommendation
    movie_recommendation = movie_genres.get(clean_text, "Bot: I don't have recommendations for that genre yet! Try typing 'action', 'comedy', 'horror', 'sci-fi', or 'drama'.")
    
    #Print the recommendation
    print(movie_recommendation)