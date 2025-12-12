from abc import ABC, abstractmethod  # Soyut sınıf ve soyut method

class VideoBase(ABC):
   
   VALID_VISIBILITIES = {"public", "private", "unlisted"}
   VALID_STATUSES = {"uploaded", "processing", "published", "blocked", "removed"}
   
   def __init__(self, video_id, channel_id, title, duration_seconds, visibility, status):
     
     self.video_id = video_id
     self.channel_id = channel_id
     self.title = title
     self.duration_seconds = duration_seconds
     self.visibility = visibility
     self.status = status

 # ----- Abstract methods -----
 

 