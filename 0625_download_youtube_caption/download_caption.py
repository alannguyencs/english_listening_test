from ytcc.download import Download

video_id = 'zIjVbcS02YM'
download = Download()
# Language is optional and default to "en"
# YouTube uses "en","fr" not "en-US", "fr-FR"
captions = download.get_captions(video_id, 'en')

file = open('caption.txt', 'w')
file.write(captions)
