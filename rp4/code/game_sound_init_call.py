def PlaySound(directory, file):
  sound_path = os.path.join(directory, file)
  pygame.mixer.init()
  pygame.mixer.music.load(sound_path)
  pygame.mixer.music.play()
