  #GameSound class will implement the sound aspects of the game which will 
  #provide the lasers with sound every time they are activated, will play a 
  #crashing sound when a specific colored laser hits the matching colored 
  #target, will provide a sound specific to the player losing the game as 
  #well as the winning sound once the game has been won.

class GameSound():
    import pygame

    # cdm set to loss for testing purposes
    cmd = "loss"
    
    #we could just get rid of the class and just use this section replacing fire, hit, etc.
    #with key pressed for firing a laser or when a hit/win/loss takes place

    def PlaySound(directory, file):
        import pygame, os
        sound_path = os.path.join(directory, file)
        pygame.mixer.init()
        pygame.mixer.music.load(sound_path)
        pygame.mixer.music.play()
        
    #-- Reference for wav files --
    #Downloaded from freesound.org

    directory = "/Users/meagonGleason/Downloads/"

    if(cmd == "fire"):
        PlaySound(directory, "42106__marcuslee__laser-wrath-4.wav");
    elif(cmd == "hit"):
        PlaySound(directory, "35462__jobro__explosion-5.wav");
    elif(cmd == "loss"):
        PlaySound(directory, "275008__alienxxx__mayday-mayday.wav");
        pygame.time.wait(2700)
        PlaySound(directory, "367622__fxkid2__explosion-with-debris.wav");
    elif(cmd == "win"):
        PlaySound(directory, "270528__littlerobotsoundfactory__jingle-win-00.wav");


   
