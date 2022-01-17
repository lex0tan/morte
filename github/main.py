from toimport import *


client = TelegramClient("pornhubot", api_id, api_hash)

print (f"{info}Hi {r}{sysname}!{rs}, Remember that this bot is {cy}FREE{rs} to use. {cy}Don't skid this without giving credits.")
time.sleep(5)
clr()
banner()
try:
    client.start()
    print (f"{success}succesfully logged in your account")
    time.sleep(1)
except:
    print(f"{error}{r}Can't connect to telegram!{rs} try to delete session, stop session\nof the bot in telegram and re-log in!")
    
    
#starting pornhub-api to find videos.
try:
    api = PornhubApi()
    print(f"{success}API loaded")
except:
    print(f"{error}{r}Can't run Pornhub API")



f = open("user.txt",encoding="utf-8")
user= json.load(f)
    
    
    
#Printing user id to user.txt to mantain tags between restart    
@client.on(events.NewMessage(outgoing=True, pattern=comm_start))
async def start(event):
    if (len(user)) == 0:
        try:
            entity = await client.get_me()
            usr_id = entity.id
            usr_name = entity.first_name
            user.append({"userid": usr_id, "tags": []})
        except Exception as e:
            await event.respond(f"An error occured!\n{e}")    
            
        try:    
            with open("user.txt", "w") as outfile:
                    json.dump(user, outfile)
        except Exception as e:
            await event.respond(f"An error occured!\n{e}")    
        await event.respond(f"Succesfully registered as {usr_name}!\n see {comm_info} for all the commands you can do")
        
    if (len(user)) == 1:
        await event.respond(f"You already logged in!\nsee {comm_info} for all the commands you can do")
      
      
        
#A list of all the commands you can do
@client.on(events.NewMessage(outgoing=True, pattern=comm_info))
async def info(event):
    if (len(user)) == 1:
        me = await client.get_me()
        name = me.first_name; reply = ""; to_print_comm_list = []
        for command in comm_list:
            reply += f"**·{command}** \n"
        await event.respond(f"**Hi {name}, there are all the commands you can use:**\n{reply}")
    else:
        await event.respond(f"You need to log in first! type **{comm_info}**")
    
    
    
#A list of your active tags    
@client.on(events.NewMessage(outgoing=True, pattern=comm_listtags))
async def listtag(event):
    tags_to_print = []; reply = ""
    for usr in user:
        print (usr)
        for tags in usr['tags']:
            tags_to_print.append(tags)
            
    for tag in tags_to_print:
        reply += f"**·{tag}** \n"
        
    await event.respond(f"Your active tags: \n{reply}")
    
    
    
#adding tags    
@client.on(events.NewMessage(outgoing=True, pattern=r".addtag (\w+)"))      
async def addtag(event):
    tag_to_add= event.pattern_match.group(1)
    for usr in user:
        try:    
            usr["tags"].append(tag_to_add)
            with open("user.txt", "w") as outfile:
                json.dump(user, outfile)
            await event.respond(f"Added succesfully {tag_to_add}")
        except Exception as e:
            await event.respond(f"an error occured\n{e}")

#Send video by set id   
@client.on(events.NewMessage(outgoing=True, pattern=comm_vidbytag))    
async def vidbytag(event):
    i = 0
    my_id = await client.get_me()
    tag_list = []; tags_to_search_list=[]; ordering_text=["featured","newest","mostviewed","rating"]; vid_list = []
    #try:
    while i < 1:
        for tags in user:
            for tag in tags["tags"]:
                tag_list.append(tag)
        final_ordering = random.choice(ordering_text)         
        category_list = random.choice(tag_list)
        final_tag = random.choice(tag_list)
        print (f"{info}{lg}Searching video for: {rs}\n{r}tag: 'teen' ordering: '{final_ordering}' category: '{category_list}'{rs}")
        tag_list.append("teen")
    
        try:
            data = api.search.search(
            ordering = final_ordering,
            tags =["teen"],
            category=category_list,
                                    )
            i = 1
            break
        except:
            print ("unknown error")
    if data.videos:   
        for vid in data.videos:
            print (vid.title, vid.video_id, vid.duration)
            image = vid.default_thumb
            vid_list.append(vid.video_id)
        id_pornazzo = random.choice(vid_list)   
            
        link_pornazzo = (f"https://it.pornhub.com/view_video.php?viewkey={id_pornazzo}")
        print(link_pornazzo)
        chrome_options = Options()
        #chrome_options.add_argument("--headless")
        #chrome_options.add_argument("--disable-gpu")
        driver = webdriver.Chrome(executable_path="C:\\Users\\imfireh\\Desktop\\git\\ChromeDriver.exe", options=chrome_options)
        driver.get(f"{link_pornazzo}")
        await asyncio.sleep(5)
        print("scemo")
        titolo_pagina = driver.title
        try:
            startVid = driver.find_element(By.XPATH, "//div[@id='playerDiv_395997721']/div[6]/div/div")
            startVid.click()
            await asyncio.sleep(5)
        except:
            print("Video already started")
            await asyncio.sleep(5)
        try:
            button18 = driver.find_element(By.XPATH, "//div[@id='modalWrapMTubes']/div/div/button")
            button18.click()
            await asyncio.sleep(1)
        except:
            print("No 18 years button")
            await asyncio.sleep(1)
        try: 
            skipPub = driver.find_element(By.XPATH, "//div[@id='playerDiv_398811571']/div[9]/div")
            skipPub.click()
            await asyncio.sleep(1)                
        except:
            print ("No ads")
            await asyncio.sleep(1)                
        try:
            startVid = driver.find_element(By.XPATH, "//div/div[6]/div/div")
            startVid.click()
            await asyncio.sleep(1)
        except:
            print("Video already started")
            await asyncio.sleep(1)
        try: 
            skipPub = driver.find_element(By.XPATH, "//div[@id='playerDiv_398811571']/div[9]/div")
            skipPub.click()
            await asyncio.sleep(1)            
        except:
            print ("No ads")
            await asyncio.sleep(1)

        thumbnail = urllib.request.urlretrieve(image, "thumb.png")
        for request in driver.requests:
            if request.response:
                if "master.m3u8" in request.url:
                    test = str(request.response.body).split('\\n')
                    qualities = []
                    for link in test:
                        if "index" in link:
                            qualities.append(link)
                    url_dir = str(request.url).split("master.m3u8")       
                    final_url = url_dir[0] + qualities[0] 
                    os.chdir('/Users/imfireh/Desktop/git')
                    print(final_url)
                    
                    subprocess.call(['ffmpeg.exe', '-y', '-i', f'{final_url}', '-bsf:a', 'aac_adtstoasc', '-vcodec', 'copy', '-c', 'copy', '-crf', '50', f'C:/Users/imfireh/Desktop/git/vid/video.mp4'])
                    print("done")
        await client.send_file(thumb = "thumb.png", caption = f"{titolo_pagina}", entity = "me" , file=("C:/Users/imfireh/Desktop/git/vid/video.mp4"), progress_callback=callback)                    
# except IndexError:        
    #     await event.respond(message = f"**Before searching a video in this mode, you need to set tags first!**\n`see {comm_info}`") 
    # except Exception as e:
    #     await event.respond(message= f"Another type of error occured!\n{e}")
    

    
client.run_until_disconnected()