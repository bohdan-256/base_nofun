import wget
import os

base_url = "https://github.com/bohdan-256/test_stie/blob/main/JopaForum.html" 
print("start download...")
wget.download(url = base_url , out = "test.html" )
    

