import json 
f = open("input/chapter.json","r")
chapters = json.load(f)
f.close()
args = ["ffmpeg -y -i gt.mp4"]
for i, chapter in enumerate(chapters):
    arg = "-vcodec copy -acodec copy -ss {st} -to {et} -sn \"{i} - {title}.mp4\" ".format(i=i + 1,st=chapter["start_time"],et=chapter["end_time"],title=chapter["title"])
    print(arg)
    args.append(arg)

cmd = "^\n ".join(args)

ot = open("output/ff.cmd","w")
ot.write(cmd)
ot.close()
