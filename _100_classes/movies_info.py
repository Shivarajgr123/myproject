''''''
'''
Entity : Movie
Attributes :mid, name, creator, starring, genre, subtitle, language, episode, season, imbd_rating, run_time,awards
Values : prison break, paul T, wentworth miller, action thriller,yes, english, 90, 5,8.3 , 50, best series
Datatype :str,str,str,str,bool,str,int,float,int,int
'''

class Movie:
    def __init__(self, mid, name,  cast, creator, starring, genre, subtitle, lang, epis, season, i_rating,r_time, awards):
        self.mid = mid
        self.name = name
        # ....

    def get_movieinfo(self):
        pass
    def update_runtime(self):
        pass
    def update_awards(self):
        pass
    def update_collecitons(self):
        pass

cast = {"hero": "", "herione":"", "producer":"","director":""}
vikram = Movie(100, "VIKRAM", cast, )
