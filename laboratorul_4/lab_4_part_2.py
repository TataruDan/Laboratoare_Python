# main class / Parent class
class player:
    def __init__(self,name,size,model):
        self.name = name # the name of the player
        self.size = size # size of the player
        self.model = model # model of the player

    def start(self): # method to start the player
        print("Player has started!")

    def stop(self): # method to stop the player
        print("Player just stopped")

    def mute_on(self): # to mute
        print("Mute On")

    def mute_off(self): # to unmute
        print("Mute Off")
#inherited class
class audio_player(player):

    song_list = [] # save the song's name
    pos = 0 # position of the song in the playlist

    def pause(self): # pause the song
        print("Pause")

    def add_song(self,song_name): # add a new song
        self.song_list.append(song_name)

    def next_song(self): # change to next song
        if(self.pos > len(self.song_list)):
            self.pos = 0
        else:
            self.pos += 1

    def current_song(self): # info about the current song
        print("Current Song : " + self.song_list[self.pos])

    def prev_song(self): # change cu previous song
        if(self.pos < 0):
            self.pos = len(self.song_list)
        else:
            self.pos -= 1

    def show_playlist(self): # get info about all songs in the playlist
        return self.song_list

    def repeat(self): # put the song on repeat
        print("The song is on repeat")
#inherited class
class video_player(player):

    video_name = "" # save the name of the video
    resolution = 140 # initial resolution of the video

    def resolution(self,resolution): # change the resolution of the video
        self.resolution = resolution
        print("The resolution was changed to " + str(self.resolution) + "px")

    def autostart(self): # autostart the video
        print("Auto start is ON")

    def start_video(self,video_name): # start the video
        self.video_name = video_name

    def video_info(self): # get the video's info
        return "The name of the video : " + self.video_name

    def speed(self, speed): # set the speed of the video
        if(speed < 0):
            print("The speed is slowed")
        if speed > 2:
            print("We do not support such video playback ")
        print("New speed is" + speed)
# inherited class
class dvd_player(player):
    disk_name = "" # save the name of the disk

    def insert_disk(self,disk_name): # insert the disk
        self.disk_name = disk_name
        print("----DISK WAS READ SUCCESSFULLY----")

    def receive_disk(self): # get the disk from port
        self.disk_name = ""
        print('----DISK PORT IS EMPTY----')

    def info_disk(self): # information about what is on disk
        print("Film name : " + self.disk_name)

# set a new audio player
Yamaha = audio_player("Mono","Medium","Pro")
print("Audio")
Yamaha.start()
Yamaha.add_song("You are the winner")
Yamaha.add_song("Shape of my life")
Yamaha.add_song("Never gonna give you up")
Yamaha.current_song()
Yamaha.next_song()
Yamaha.current_song()
print("Playlist : ")
print(Yamaha.show_playlist())
Yamaha.stop()

#set a new video player
Dell = video_player("Amore","Big","Standart")
print("\n\n")
print("Video")
Dell.start()
Dell.start_video("How to build a house in 80 days")
Dell.resolution(1080)
print(Dell.video_info())
Dell.stop()

print("\n\n")
print("DVD info")

# set a new dvd player
Sony = dvd_player("Sony","Big","Standart")
Sony.start()
Sony.insert_disk("Jumanji")
Sony.info_disk()
Sony.receive_disk()
Sony.stop()
