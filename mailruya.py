class UrTube:


    def __init__(self):


    self.videos = []
self.users = []


def add_video(self, video):


    self.videos.append(video)


def add_user(self, user):


    self.users.append(user)


def show_videos(self):


    for video in self.videos:
    print(video)


def show_users(self):


    for user in self.users:
    print(user)


class Video:


    def __init__(self, title, category, duration):


    self.title = title
self.category = category
self.duration = duration


def __str__(self):


    return f
"Title: {self.title}, Category: {self.category}, Duration: {self.duration} minutes"


class User:


    def __init__(self, username, email):


    self.username = username
self.email = email


def __str__(self):


    return f
"Username: {self.username}, Email: {self.email}"

urbantube = UrTube()

video1 = Video("Python Basics", "Programming", 10)
video2 = Video("Web Development Intro", "Web Development", 15)

user1 = User("JohnDoe", "johndoe@example.com")
user2 = User("JaneSmith", "janesmith@example.com")

urbantube.add_video(video1)
urbantube.add_video(video2)

urbantube.add_user(user1)
urbantube.add_user(user2)

print("Videos on UrTube:")
urbantube.show_videos()

print("\nUsers on UrTube:")
urbantube.show_users()
